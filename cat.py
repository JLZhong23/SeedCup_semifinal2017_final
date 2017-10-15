# -*- coding:UTF-8 -*-
import csv
import pandas as pd
import os
import numpy as np
import random

def get_prefinnally():
    a = pd.read_csv('1.csv').values.tolist()
    b = pd.read_csv('2.csv').values.tolist()

    c = b
    i = 0
    while (len(c) < 85000):
        if a[i] not in b:
            c.append(a[i])
            print a[i]
        i = i + 1
        print i
    f = open('pre.csv', 'wb')
    write = csv.writer(f)
    write.writerows(c)

def get_pretxt():
    test = pd.read_csv('pre.csv').values
    print test
    f = open('pre.txt', 'wb')
    for i in range(len(test)):
        f.write(str(test[i][0]))
        f.write('\t')
        f.write(str(test[i][1]))
        f.write('\n')
    f.close()

if __name__=='__main__':
    get_prefinnally()
    get_pretxt()