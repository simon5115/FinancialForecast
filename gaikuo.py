# -*- coding: utf-8 -*-
# 时间    : 2018/10/18 9:59
# 作者    : xcl



import numpy as np
import pandas as pd
inputfile = 'C:\\Users\\Administrator\\Desktop\\FinancialForecast\\data\\data1.csv' #输入的数据文件
data = pd.read_csv(inputfile) #读取数据
r = [data.min(), data.max(), data.mean(), data.std()] #依次计算最小值、最大值、均值、标准差
r = pd.DataFrame(r, index = ['Min', 'Max', 'Mean', 'STD']).T  #计算相关系数矩阵
np.round(r, 2) #保留两位小数
print(r)