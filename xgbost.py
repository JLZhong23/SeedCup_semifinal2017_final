#!/usr/bin/env python2
# -*- coding:UTF-8 -*-
'''文件作用，xgboost模型搭建，训练并预测结果'''
import pandas as pd
import csv
from get_feature import *
from sklearn.model_selection import train_test_split
import xgboost as xgb


'''模型搭建训练，最终将训练好的模型存入0001.model当中'''
def XGB():
    startdata=823
    enddata=825
    user,traindata,label=train_data_get(startdata,enddata,8)
    x_train,x_test,y_train,y_test=train_test_split(traindata.values,label.values,test_size=0.2,random_state=0)

    dtrain = xgb.DMatrix(x_train, label=y_train)
    dtest = xgb.DMatrix(x_test, label=y_test)
    param = {'learning_rate': 0.1, 'n_estimators': 1000, 'max_depth': 3,
             'min_child_weight': 5, 'gamma': 0, 'subsample': 1.0, 'colsample_bytree': 0.8,
             'scale_pos_weight': 1, 'eta': 0.05, 'silent': 1, 'objective': 'binary:logistic'
             , 'nthread': 4, 'eval_metric': "auc"}
    num_round = 50000
    plst = param.items()
    plst += [('eval_metric', 'logloss')]
    evallist = [(dtest, 'eval'), (dtrain, 'train')]
    bst = xgb.train(plst, dtrain, num_round, evallist)
    bst.save_model('0001.model')

'''模型使用，生成预测每个用户购买某件商品的概率，写入temp文件当中'''
def use_model():
    bst = xgb.Booster({'nthread': 4})  # init model
    bst.load_model("0001.model")  # load data
    pre_user,pre_data=getfecture(826)
    pre = xgb.DMatrix(pre_data.values)
    y = bst.predict(pre)

    print len(pre_user)
    pre_user['y'] = y
    print len(y)
    pre_user.to_csv('temp.csv',index=False, index_label=False)

    '''
    pre_user.sort_index(['y'],ascending=False)

    pred = pre_user.head(4000)
    pred = pred[['user', 'product']]
    print len(pred)
    pred['user'] = pred['user'].astype(int)
    pred['product'] = pred['product'].astype(int)
    pred.to_csv('pre820.csv', index=False, index_label=False)'''

'''获取概率前85000的数据，写入pre926.csv当中'''
def getpre():
    pre=pd.read_csv('temp.csv')
    pre=pre.sort_values(by='y',ascending=False)
    print pre
    pred=pre.head(85000)
    print pred
    pred = pred[['user', 'product']]

    pred['user'] = pred['user'].astype(int)
    pred['product'] = pred['product'].astype(int)
    pred.to_csv('1.csv', index=False, index_label=False)

def getpre2():
    pre = pd.read_csv('temp.csv')
    pred=pre[pre['y']>0.5]
    print pred
    pred = pred[['user', 'product']]
    pred['user'] = pred['user'].astype(int)
    pred['product'] = pred['product'].astype(int)
    pred.to_csv('pre826.csv', index=False, index_label=False)


if __name__ == '__main__':
    XGB()
    use_model()
    getpre()