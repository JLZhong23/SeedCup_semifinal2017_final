# -*- coding:UTF-8 -*-
'''文件作用：特征提取，最终生成相应文件。
特征：用户行为特征：距离预测日期的前一天，两天，三天，七天，十天，两周的行为特征
     商品特征：商品id，品牌id,类别id,店铺id，价格，这一个月里的浏览，收藏，加购，购买总次数
     用户特征：用户id,用户性别，年龄，会员等级，宝宝性别，宝宝年龄'''
import csv
import pandas as pd
import os
import numpy as np
import random
from infodata import info_product

'''用户行为信息路径'''
user_behavior_path_1='data/behavior_info111.csv'
user_behavior_path_2='data/behavior_info222.csv'
user_behavior_path_3='data/behavior_info333.csv'
user_behavior_path_4='data/behavior_info444.csv'
user_behavior_path_5='data/behavior_info555.csv'

'''获取从startdata到enddata的用户行为信息，返回DataFrame'''
def get_data(startdata,enddata):
    ub1 = pd.read_csv(user_behavior_path_1)
    ub2 = pd.read_csv(user_behavior_path_2)
    ub3 = pd.read_csv(user_behavior_path_3)
    ub4 = pd.read_csv(user_behavior_path_4)
    ub5 = pd.read_csv(user_behavior_path_5)
    ub = pd.concat([ub1, ub2, ub3, ub4, ub5])
    ub = ub[(ub.time >= startdata) & (ub.time <= enddata)]
    return ub

'''获取从stardata到enddata期间的用户行为特征，并写到data/user_behavior_%stardata_%endata.csv中'''
def get_user_behavior(stardata,enddata):
    write_path='data/user_behavior_%s_%s.csv'%(stardata,enddata)
    ub=get_data(stardata,enddata)
    ub=ub.values
    i=0
    result=[]
    while(i<len(ub)):
        type=[0,0,0,0]
        type[ub[i][3]-1]=type[ub[i][3]-1]+1
        i=i+1
        while(i<len(ub) and ub[i][0]==ub[i-1][0] and ub[i][1]==ub[i-1][1] ):
            type[ub[i][3]-1] = type[ub[i][3]-1] + 1
            i=i+1
        res=ub[i-1].tolist()+type
        del res[3]
        del res[2]
        result.append(res)
    f=open(write_path,'wb')
    write = csv.writer(f)
    write.writerow(['user','product','type1','type2','type3','type4'])
    write.writerows(result)
    f.close()

    a = pd.read_csv(write_path)
    a = a.groupby(['user', 'product'], as_index=False).sum()
    a = a.values
    f = open(write_path, 'wb')
    print 'writecsv:%s'%write_path
    write = csv.writer(f)
    write.writerow(['user', 'product', 'type1', 'type2', 'type3', 'type4'])
    write.writerows(a)
    f.close()

'''获取enddata前1,2,3,4,7,10,14天的用户行为特征并写如相应的文件当中'''
def get_time_behavior(enddata):
    for i in (1,2,3,7,10,14):
        a=enddata-i
        get_user_behavior(a,enddata)

'''将上面的用户行为特征信息合并在一起作为用户行为总特征'''
def get_behavior_prestart(stardata):
    path=[]
    for i in (1,2,3,7,10,14):
        a=stardata-1
        b=a-i
        path1='data/user_behavior_%s_%s.csv'%(b,a)
        path.append(path1)

    for i in path:
        if not os.path.exists(i):
            get_time_behavior(stardata-1)
    usb1 = pd.read_csv(path[0])
    usb2 = pd.read_csv(path[1])
    usb3 = pd.read_csv(path[2])
    usb4 = pd.read_csv(path[3])
    usb5 = pd.read_csv(path[4])
    usb6=pd.read_csv(path[5])
    usb6 = pd.merge(usb6, usb5, how='left', on=['user', 'product'])
    usb6 = pd.merge(usb6, usb4, how='left', on=['user', 'product'])
    usb6 = pd.merge(usb6, usb3, how='left', on=['user', 'product'])
    usb6 = pd.merge(usb6, usb2, how='left', on=['user', 'product'])
    usb6 = pd.merge(usb6, usb1, how='left', on=['user', 'product'])
    usb6 = usb6.fillna(0)
    write_path='data/user_behavior_%s.csv'%(stardata)
    print 'writecsv:%s' % write_path
    usb6.to_csv(write_path, index=False, index_label=False)

#get_behavior_prestart(823)
'''获取从stardata到enddata期间的用户行为的目标，最终购买则为1,否则为0'''
def get_label(startdata,enddata):
    write_path='data/label_%s_%s.csv'%(startdata,enddata)
    actions=get_data(startdata,enddata)
    actions = actions[actions['type'] == 4]
    actions = actions.groupby(['user', 'product'], as_index=False).sum()
    actions['label'] = 1
    actions = actions[['user', 'product', 'label']]
    actions=actions.values
    f=open(write_path,'wb')
    print 'writecsv:%s'%write_path
    write=csv.writer(f)
    write.writerow(['user','product','label'])
    write.writerows(actions)
    f.close()


'''加入相应的用户静态特征和商品的特征，startdata,enddata为需要预测的开始日期和结束日期'''
def get_train_data(startdata,enddata):
    be_path='data/user_behavior_%s.csv'%(startdata)
    label_path='data/label_%s_%s.csv'%(startdata,enddata)
    if not os.path.exists(be_path):
        get_behavior_prestart(startdata)
    if not os.path.exists(label_path):
        get_label(startdata,enddata)
    ub=pd.read_csv(be_path)
    label=pd.read_csv(label_path)
    user=pd.read_csv('data/user_info.csv')
    if not os.path.exists('data/product_info.csv'):
        info_product('data/product_info.txt','data/product_info.csv')
    product=pd.read_csv('data/product_info.csv')
    ub=pd.merge(ub,user,how='left',on='user')
    ub=pd.merge(ub,product,how='left',on='product')
    ub=pd.merge(ub,label,how='left',on=['user','product'])
    ub=ub.fillna(0)
    write_path='data/train_%s.csv'%startdata
    print 'writecsv:%s'%write_path
    ub.to_csv(write_path,index=False, index_label=False)


def get_train_data_windows(startdata, windows):
    train_path=[]
    for i in range(windows):
        sta=startdata-i
        path1= 'data/train_%s.csv' % sta
        if not os.path.exists(path1):
            get_train_data(sta,sta+2)
        train_path.append(path1)
    ub=pd.read_csv(train_path[0])
    for i in range(1,len(train_path)):
        ub2=pd.read_csv(train_path[i])
        ub=pd.concat([ub,ub2])
    write_path='data/train_window_%s.csv'%windows
    print 'writecsv:%s'%write_path
    ub.to_csv(write_path,index=False,index_label=False)


'''将总样本分为正样本，负样本并存入相应文件'''
def divison_pos_neg(startdata,enddata):
    trainpath='data/train_%s.csv'%startdata
    if not os.path.exists(trainpath):
        get_train_data(startdata,enddata)
    ub=pd.read_csv(trainpath)
    ub1=ub[ub['label']==1]
    ub2=ub[ub['label']==0]
    train_pos_path='data/train_%s_pos.csv'%startdata
    train_neg_path='data/train_%s_neg.csv'%startdata
    print 'writecsv:%s'%train_pos_path
    print 'wtirecsv:%s'%train_neg_path
    ub1.to_csv(train_pos_path,index=False, index_label=False)
    ub2.to_csv(train_neg_path,index=False,index_label=False)


#for i in range(8):
    #divison_pos_neg(823-i,825-i)
'''减少负样本比例，平滑总数据'''
def down_neg(startdata,enddata,rate):
    pos_path='data/train_%s_pos.csv'%startdata
    neg_path='data/train_%s_neg.csv'%startdata
    if not os.path.exists(pos_path):
        divison_pos_neg(startdata,enddata)
    if not os.path.exists(neg_path):
        divison_pos_neg(startdata,enddata)
    pos=pd.read_csv(pos_path)
    neg=pd.read_csv(neg_path)
    len1=pos.shape[0]*rate

    rand_index = random.sample(range(len(neg)),len1)
    rand_neg=neg.values[rand_index]

    downpath='data/train_%s_neg_down.csv'%startdata
    f=open(downpath,'wb')
    print 'writecsv:%s'%downpath
    write=csv.writer(f)
    a=neg.columns.tolist()
    write.writerow(a)
    write.writerows(rand_neg)
    f.close()

#for i in range(7):
#    down_neg(822-i,824-i,10)
'''设置时间滑动窗口，获取相应训练数据'''
def get_train_csv(startdata,enddata,windows):
    pos_path=[]
    neg_path=[]
    for i in range(windows):
        sta=startdata-i
        path1='data/train_%s_pos.csv'%sta
        if not os.path.exists(path1):
            divison_pos_neg(sta,sta+2)
        path2='data/train_%s_neg_down.csv'%sta
        if not os.path.exists(path2):
            down_neg(sta,sta+2,10)
        pos_path.append(path1)
        neg_path.append(path2)
    pos = pd.read_csv(pos_path[0])
    neg=pd.read_csv(neg_path[0])
    for i in range(1, len(pos_path)):
        pos2 = pd.read_csv(pos_path[i])
        pos = pd.concat([pos, pos2])
        neg2=pd.read_csv(neg_path[i])
        neg=pd.concat([neg,neg2])
    write_path1='data/train_%s_pos.csv'%windows
    write_path2='data/train_%s_neg.csv'%windows
    print 'writecsv:%s'%write_path1
    print 'writecsv:%s'%write_path2
    pos.to_csv(write_path1,index=False,index_label=False)
    neg.to_csv(write_path2,index=False,index_label=False)

#get_train_csv(823,825,8)

'''将正负样本合并，并打乱数据'''
def make_train_data(startdata,enddata,windows):
    train_pos_path = 'data/train_%s_pos.csv' % windows
    train_neg_path = 'data/train_%s_neg.csv' % windows
    if not os.path.exists(train_neg_path):
        get_train_csv(startdata,enddata,windows)
    if not os.path.exists(train_pos_path):
        get_train_csv(startdata,enddata,windows)
    train_pos=pd.read_csv(train_pos_path)
    train_neg=pd.read_csv(train_neg_path)
    train=pd.concat([train_pos,train_neg])
    train=train.values
    np.random.seed(2)
    np.random.shuffle(train)

    write_path='data/train_%s.csv'%windows
    f=open(write_path,'wb')
    print 'writecsv:%s'%write_path
    write=csv.writer(f)
    write.writerow(train_pos.columns.tolist())
    write.writerows(train)
    f.close()

#make_train_data(823,825,8)
'''获取训练数据，“用户，商品”，“特征”，“期望结果"'''
def train_data_get(startdata,enddata,windows):
    trainpath='data/train_%s.csv'%windows
    if not os.path.exists(trainpath):
        make_train_data(startdata,enddata,windows)

    traindata = pd.read_csv(trainpath)
    user = traindata[['user', 'product']].copy()
    label = traindata['label'].copy()
    del traindata['user']
    del traindata['product']
    del traindata['label']
    del traindata['mod1']
    del traindata['mod2']
    del traindata['mod3']
    return user,traindata,label


'''获取相应的预测特征信息'''
def getfecture(startdata):
    be_path = 'data/user_behavior_%s.csv' % (startdata)
    if not os.path.exists(be_path):
        get_behavior_prestart(startdata)

    ub = pd.read_csv(be_path)
    user = pd.read_csv('data/user_info.csv')
    if not os.path.exists('data/product_info.csv'):
        info_product('data/product_info.txt','data/product_info.csv')
    product = pd.read_csv('data/product_info.csv')
    ub = pd.merge(ub, user, how='left', on='user')
    ub = pd.merge(ub, product, how='left', on='product')
    ub = ub.fillna(0)
    user1=ub[['user','product']].copy()
    del ub['user']
    del ub['product']
    del ub['mod1']
    del ub['mod2']
    del ub['mod3']
    return user1,ub

