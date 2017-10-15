# -*- coding:UTF-8 -*-
import csv
import pandas as pd

'''提取商品特征，写如csv文件'''
def info_product(product_path,write_path):
    f=open(product_path,'r')
    temp=[]
    while(1):
        lines=f.readlines(10000)
        if not lines:
            break
        else:
            for line in lines:
                a=line.split()
                b=[]
                for i in (0,1,2,3,4,5,6,-1):
                    if i<len(a)-1:
                        b.append(a[i])
                    else:
                        b.append('-999')
                #print b
                temp.append(b)
    f.close()
    ff=open(write_path,'wb')
    write=csv.writer(ff)
    write.writerow(['product','id2','id3','id4','mod1','mod2','mod3','price'])
    write.writerows(temp)
    ff.close()

#info_product('data/product_info.txt','data/product_info.csv')

