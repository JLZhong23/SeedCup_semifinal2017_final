import pandas as pd
import csv


def data_num():
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
    f = open('data/test2.csv', 'wb')
    writer = csv.writer(f)
    for x in range(0, len1):
        if 822 <= info1.loc[x][2] <= 825 and info1.loc[x][3] == 3:
            row = info1.loc[x]
            writer.writerow(row)
    for x in range(0, len2):
        if 822 <= info2.loc[x][2] <= 825 and info2.loc[x][3] == 3:
            row = info2.loc[x]
            writer.writerow(row)
    for x in range(0, len3):
        if 822 <= info3.loc[x][2] <= 825 and info3.loc[x][3] == 3:
            row = info3.loc[x]
            writer.writerow(row)
    for x in range(0, len4):
        if 822 <= info4.loc[x][2] <= 825 and info4.loc[x][3] == 3:
            row = info4.loc[x]
            writer.writerow(row)
    for x in range(0, len5):
        if 822 <= info5.loc[x][2] <= 825 and info5.loc[x][3] == 3:
            row = info5.loc[x]
            writer.writerow(row)
    info1 = pd.read_csv('data/test2.csv', header=None)
    f = open('2.csv', 'wb')
    writer = csv.writer(f)
    writer.writerow(info1.loc[0])
    for x in range(1, info1.shape[0]):
        if info1.loc[x][0] == info1.loc[x - 1][0] and info1.loc[x][1] == info1.loc[x - 1][1]:
            continue
        else:
            writer.writerow(info1.loc[x])
        print x


if __name__=='__main__':
    data_num()
