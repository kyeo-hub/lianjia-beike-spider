#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :concact_csv.py
@说明        :拼接拉取的二手房结果。
@时间        :2024/03/27 09:57:59
@作者        :跳跃的🐸
@版本        :1.0
'''

print(__name__)
print(__package__)



import os
import pandas as pd
from lib.utility.path import DATA_PATH
from lib.spider.base_spider import SPIDER_NAME

city='wh'
date='20240329'

# 指定要读取的文件夹路径
dir = "{0}/{1}/ershou/{2}/{3}".format(DATA_PATH, SPIDER_NAME, city, date)

xlsx_file = "{0}/{1}/ershou/{2}/{3}/total.xlsx".format(DATA_PATH, SPIDER_NAME, city, date)



#新建列表，存放文件名（可以忽略，但是为了做的过程能心里有数，先放上）
filename_excel = []

#新建列表，存放每个文件数据框（每一个excel读取后存放在数据框）
frames = []

for root, dirs, files in os.walk(dir):
    for file in files:
        # print(os.path.join(root,file))
        filename_excel.append(os.path.join(root,file))
        try:
            df = pd.read_excel(os.path.join(root,file)) #excel转换成DataFrame
            # df['pic'] = df['pic'].astype(str) 
            df.drop('pic', axis=1, inplace=True)
            frames.append(df)
        except:
            print(os.path.join(root,file))
#打印文件名
# print(filename_excel)   
 #合并所有数据
result = pd.concat(frames)    
# result = result.dropna(axis=0, subset=["钩捆号"]) #删除指定列中有缺失值的那一行数据


#查看合并后的数据
# result.head(5)
# result.shape[0]
# print(result)
result.to_excel(xlsx_file,index=False)
# result.to_csv('D:\\1988\\a12.csv',sep=',',index = False)#保存合并的数据到电脑D盘的merge文件夹中，并把合并后的文件命名为a12.csv