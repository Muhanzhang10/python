#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 15:59:11 2021

@author: zhangmuhan
"""

#第一题
fruits = ['appled', 'banana', 'kiwi', 'peach']
'''
1 列表在末尾加入菠萝
2 注意：苹果拼错了，改成正确的拼写（两种方法：1直接赋值 2切片）
3 调换菠萝和猕猴桃的位置
4 删除香蕉
5 逐个打印出所有水果（循环）
'''



#第二题
Barcelona = {'Players': ['Messi', 'Griezmann', 'Sergio', 'Dembele'], 'Color': ['Red', 'Blue'], 'UCLtrophies': 5, 'isFirst': False}
'''
弄清楚Barcelona的数据结构和存储的内容，以及其结构。 注： 'Players'四个球员，'Color'存储主队颜色，'UCLtrophies'存储欧冠冠军次数，'isFirst'存储是否当前在榜首
实施一下操作：
1 加入球队新转会球员 'Halland'
2 球队当前赛季将赢得欧冠冠军，更新冠军次数
3 球队当前赛季将会赢得西甲冠军，因此，将会处在积分榜榜首，就此情况更新
4 球队队员 'Dembele' 因为表现不佳离队，因此不再是球队一员，将其删掉
5 效仿此数据结构，任选一支足球队创造此数据结构（Barcelona object所有的键必须涵盖）。内容可以随便编写，不过建议根据实际情况更新
6 将新球队的第一名球员转会至Barcelona，就此情况更新
'''



#第三题
'''
写一个函数，对于任意两个列表，找出他们拥有共同的元素个数并返还
例如：
    a =  [1, 2, 3, 4, 5]
    b = [2, 3, 6, 7, 8]
    c = [1, 2, 3, 4, 6]
    count_duplicates(a, b)应返还 2
    count_duplicates(a, c)应返还 4
如果同一个列表中有重复的元素，应先删除任何多余的元素
例如:
    a = [1, 2, 3, 4, 5, 4]
    b = [1, 2, 3, 3, 3]
    数以下两个列表的重复元素
    c = [1, 2, 3, 4, 5]
    d = [1, 2, 3]
    因此， count_duplicates(a, b)应返还 3

提示：这个函数分为两个部分，1剔除每个列表中的多余元素（上节课内容，参考is_injective(list1)函数）， 2数剔除多余元素后两个列表重复元素的个数(通过两个循环将所有元素都进行对比)
  
'''
def count_duplicates(list1, list2):
    pass #开始写后将其删掉




#第四题
import matplotlib.pyplot as plt
import numpy as np
'''
请画出sine函数和cosine函数在-2pi到2pi区间的图
使用讲过的画图package
要求必须有x轴y轴名称，图片名称，并将其存储在桌面
'''



#第五题
import xlrd
'''
学习如何使用xlrd pachage来读取excel文件
参考soccer.py中的读取方式，将所有球队的所属足联依次打印出来（excel表格倒数第二列）
'''


