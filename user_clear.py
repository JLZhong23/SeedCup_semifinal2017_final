# -*- coding:utf-8 -*-
import time
import pandas as pd
import csv


def time_change():
    info1 = pd.read_csv('behavior_info1.csv')
    f = open('behavior_info11.csv', 'wb')
    title = ['用户', '商品', '时间', '类型', ]
    writer = csv.writer(f)
    writer.writerow(title)
    for x in range(0, 1048575):
        row = info1.loc[x]
        timestamp = row[2]
        time_local = time.localtime(timestamp)
        target = time.strftime("%m%d", time_local)
        int(target)
        row[2] = target
        writer.writerow(row)
        if (x % 1000) == 0:
            print x


def behavior_clear():
    title = ['用户', '商品', '时间', '类型', ]
    info1 = pd.read_csv('behavior_info11.csv')
    info2 = pd.read_csv('behavior_info22.csv')
    info3 = pd.read_csv('behavior_info33.csv')
    info4 = pd.read_csv('behavior_info44.csv')
    info5 = pd.read_csv('behavior_info55.csv')
    target1 = open('behavior_info111.csv', 'wb')
    target2 = open('behavior_info222.csv', 'wb')
    target3 = open('behavior_info333.csv', 'wb')
    target4 = open('behavior_info444.csv', 'wb')
    target5 = open('behavior_info555.csv', 'wb')
    writer1 = csv.writer(target1)
    writer2 = csv.writer(target2)
    writer3 = csv.writer(target3)
    writer4 = csv.writer(target4)
    writer5 = csv.writer(target5)
    writer1.writerow(title)
    writer2.writerow(title)
    writer3.writerow(title)
    writer4.writerow(title)
    writer5.writerow(title)
    flag1 = flag2 = flag3 = flag4 = flag5 = 0
    for x in range(1, 62246):
        if (x % 5) == 1:
            while info1.loc[flag1][0] == x:
                writer1.writerow(info1.loc[flag1])
                flag1 += 1
            while info2.loc[flag2][0] == x:
                writer1.writerow(info2.loc[flag2])
                flag2 += 1
            while info3.loc[flag3][0] == x:
                writer1.writerow(info3.loc[flag3])
                flag3 += 1
            while info4.loc[flag4][0] == x:
                writer1.writerow(info4.loc[flag4])
                flag4 += 1
            while info5.loc[flag5][0] == x:
                writer1.writerow(info5.loc[flag5])
                flag5 += 1
        elif (x % 5) == 2:
            while info1.loc[flag1][0] == x:
                writer2.writerow(info1.loc[flag1])
                flag1 += 1
            while info2.loc[flag2][0] == x:
                writer2.writerow(info2.loc[flag2])
                flag2 += 1
            while info3.loc[flag3][0] == x:
                writer2.writerow(info3.loc[flag3])
                flag3 += 1
            while info4.loc[flag4][0] == x:
                writer2.writerow(info4.loc[flag4])
                flag4 += 1
            while info5.loc[flag5][0] == x:
                writer2.writerow(info5.loc[flag5])
                flag5 += 1
        elif (x % 5) == 3:
            while info1.loc[flag1][0] == x:
                writer3.writerow(info1.loc[flag1])
                flag1 += 1
            while info2.loc[flag2][0] == x:
                writer3.writerow(info2.loc[flag2])
                flag2 += 1
            while info3.loc[flag3][0] == x:
                writer3.writerow(info3.loc[flag3])
                flag3 += 1
            while info4.loc[flag4][0] == x:
                writer3.writerow(info4.loc[flag4])
                flag4 += 1
            while info5.loc[flag5][0] == x:
                writer3.writerow(info5.loc[flag5])
                flag5 += 1
        elif (x % 5) == 4:
            while info1.loc[flag1][0] == x:
                writer4.writerow(info1.loc[flag1])
                flag1 += 1
            while info2.loc[flag2][0] == x:
                writer4.writerow(info2.loc[flag2])
                flag2 += 1
            while info3.loc[flag3][0] == x:
                writer4.writerow(info3.loc[flag3])
                flag3 += 1
            while info4.loc[flag4][0] == x:
                writer4.writerow(info4.loc[flag4])
                flag4 += 1
            while info5.loc[flag5][0] == x:
                writer4.writerow(info5.loc[flag5])
                flag5 += 1
        else:
            while info1.loc[flag1][0] == x:
                writer5.writerow(info1.loc[flag1])
                flag1 += 1
            while info2.loc[flag2][0] == x:
                writer5.writerow(info2.loc[flag2])
                flag2 += 1
            while info3.loc[flag3][0] == x:
                writer5.writerow(info3.loc[flag3])
                flag3 += 1
            while info4.loc[flag4][0] == x:
                writer5.writerow(info4.loc[flag4])
                flag4 += 1
            while info5.loc[flag5][0] == x:
                writer5.writerow(info5.loc[flag5])
                flag5 += 1


def firsttry_screen():
    info1 = pd.read_csv('825_3.csv')
    info2 = pd.read_csv('825_4.csv')
    f = open('first.csv', 'wb')
    writer = csv.writer(f)
    for x in range(0, 18187):
        flag = 1
        row1 = info1.loc[x]
        for y in range(0, 4082):
            row2 = info2.loc[y]
            if row2[0] == row1[0] and row2[1] == row1[1]:
                flag = 0
                break
            if row2[0] > row1[0]:
                break
        if (x % 10) == 0:
            print x
        if flag == 1:
            writer.writerow(row1)


def data_num(y):
    info1 = pd.read_csv('data/behavior_info111.csv')
    info2 = pd.read_csv('data/behavior_info222.csv')
    info3 = pd.read_csv('data/behavior_info333.csv')
    info4 = pd.read_csv('data/behavior_info444.csv')
    info5 = pd.read_csv('data/behavior_info555.csv')
    len1 = info1.shape[0]
    len2 = info2.shape[0]
    len3 = info3.shape[0]
    len4 = info4.shape[0]
    len5 = info5.shape[0]
    f = open('test2.csv', 'wb')
    writer = csv.writer(f)
    total_num = 0
    date = 825
    while 1:
        for x in range(0, len1):
            if info1.loc[x][2] == date and info1.loc[x][3] == 3:
                row = info1.loc[x]
                writer.writerow(row)
                total_num += 1
            if total_num == y:
                break
        if total_num == y:
            break
        for x in range(0, len2):
            if info2.loc[x][2] == date and info2.loc[x][3] == 3:
                row = info2.loc[x]
                writer.writerow(row)
                total_num += 1
            if total_num == y:
                break
        if total_num == y:
            break
        for x in range(0, len3):
            if info3.loc[x][2] == date and info3.loc[x][3] == 3:
                row = info3.loc[x]
                writer.writerow(row)
                total_num += 1
            if total_num == y:
                break
        if total_num == y:
            break
        for x in range(0, len4):
            if info4.loc[x][2] == date and info4.loc[x][3] == 3:
                row = info4.loc[x]
                writer.writerow(row)
                total_num += 1
            if total_num == y:
                break
        if total_num == y:
            break
        for x in range(0, len5):
            if info5.loc[x][2] == date and info5.loc[x][3] == 3:
                row = info5.loc[x]
                writer.writerow(row)
                total_num += 1
            if total_num == y:
                break
        if total_num == y:
            break
        print ('日期：%d月%d日 组数：%d' %(date/100, date%100, total_num))
        date -= 1


def firsttry_cut():                                                                 # 重复删除
    info1 = pd.read_csv('825_4_1.csv')
    f = open('825_4_2.csv', 'wb')
    writer = csv.writer(f)
    writer.writerow(info1.loc[0])
    for x in range(1, 13173):
        if info1.loc[x][0] == info1.loc[x - 1][0] and info1.loc[x][1] == info1.loc[x - 1][1]:
            continue
        else:
            writer.writerow(info1.loc[x])
        print x


def csv_to_txt():                                                                   # 格式转化
    test = pd.read_csv('825_4_2.csv').values
    # print test
    f = open('825_4_2.txt', 'wb')
    for i in range(len(test)):
        f.write(str(test[i][0]))
        f.write('\t')
        f.write(str(test[i][1]))
        f.write('\n')
    f.close()


def train_data_get():
    info1 = pd.read_csv('data/behavior_info111.csv')
    info2 = pd.read_csv('data/behavior_info222.csv')
    info3 = pd.read_csv('data/behavior_info333.csv')
    info4 = pd.read_csv('data/behavior_info444.csv')
    info5 = pd.read_csv('data/behavior_info555.csv')
    len1 = info1.shape[0]
    len2 = info2.shape[0]
    len3 = info3.shape[0]
    len4 = info4.shape[0]
    len5 = info5.shape[0]
    f = open('train_data.csv', 'wb')
    writer = csv.writer(f)
    for x in range(0, len1):
        if 820 <= info1.loc[x][2] <= 822 and info1.loc[x][3] == 4:
            row = info1.loc[x]
            writer.writerow(row)
        if (x % 1000) == 0:
            print x
    for x in range(0, len2):
        if 820 <= info2.loc[x][2] <= 822 and info2.loc[x][3] == 4:
            row = info2.loc[x]
            writer.writerow(row)
        if (x % 1000) == 0:
            print x
    for x in range(0, len3):
        if 820 <= info3.loc[x][2] <= 822 and info3.loc[x][3] == 4:
            row = info3.loc[x]
            writer.writerow(row)
        if (x % 1000) == 0:
            print x
    for x in range(0, len4):
        if 820 <= info4.loc[x][2] <= 822 and info4.loc[x][3] == 4:
            row = info4.loc[x]
            writer.writerow(row)
        if (x % 1000) == 0:
            print x
    for x in range(0, len5):
        if 820 <= info5.loc[x][2] <= 822 and info5.loc[x][3] == 4:
            row = info5.loc[x]
            writer.writerow(row)
        if (x % 1000) == 0:
            print x


def test_clear():
    test = pd.read_csv('train_data.csv', header=None)
    a = []
    for x in range(0, 62245):
        a.append([])
    for x in range(0, test.shape[0]):
        num = test.loc[x][0]
        a[num-1].append(test.loc[x][1])
    f = open('train_data2.csv', 'wb')
    writer = csv.writer(f)
    writer.writerows(a)


'''
def test():
    test_data = pd.read_csv('train_data2.csv', header=None)
    data_total = 14004                                          # |B|=14004
    # data_file = pd.read_csv('test.csv', header=None)            # 自己改
    file_total = data_file.shape[0]                             # |A|=file_total
    num = 0                                                     # |A n B|=num
    for i in range(0, file_total):
        user = data_file.loc[i][0]                              # 第i条用户ID
        product = data_file.loc[i][1]                           # 第i条产品ID
        list = test_data.loc[user-1]
        length = len(list)
        for j in range(0, length):
            if product = list[j]:
                num += 1
                break
    pre = num*1.0/file_total
    recall = num*1.0/14004
    f1 = 2*pre*recall*1.0/(pre + recall)
    print ('准确率： %f' % pre)
    print ('召回率： %f' % recall)
    print ('f1： %f' % f1)'''

if __name__=='__main__':
    data_num(50000)