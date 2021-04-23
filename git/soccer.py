#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 14:14:49 2021

@author: zhangmuhan
"""

import xlrd
import matplotlib.pyplot as plt
import numpy as np

#读取Excel表格
#path 要填写本地存储的路径
path = '/Users/zhangmuhan/Desktop/杂项/Python课程/git/country rating.xlsx' 
ExcelFile = xlrd.open_workbook(path)
sheet = ExcelFile.sheet_by_name('Sheet1')

rank = []
country = []
country_abbrv = []
total = []
prev = []
change = []


for row in range(0, 1000):
    try:
        rank.append(sheet.cell(row, 0).value)
        country.append(sheet.cell(row, 1).value)
        country_abbrv.append(sheet.cell(row, 2).value)
        total.append(sheet.cell(row, 3).value)
        prev.append(sheet.cell(row, 4).value)
        change.append(sheet.cell(row, 5).value)
    except BaseException:
        break


#改变截取长度
def cut(start = 0, end = -1):
    return np.array(rank[start:end:]), np.array(country[start:end:]), np.array(country_abbrv[start:end:]), np.array(total[start:end:]), np.array(prev[start:end:]), np.array(change[start:end:])

#截取任意排名的球队
cut1 = cut(0, 20)
rank1 = cut1[0]
country1 = cut1[1]
country_abbrv1 = cut1[2]
total1 = cut1[3]
prev1 = cut1[4]
change1 = cut1[5]


fig, ax = plt.subplots()
ax.barh(country_abbrv1, total1)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Points')
ax.set_title('Country')
fig.set_size_inches(30, 10, forward=True)
#fig.savefig('/Users/zhangmuhan/Desktop/Top_10_Rank.png')
        