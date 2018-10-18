# -*- coding: utf-8 -*-
# 时间    : 2018/10/18 10:06
# 作者    : xcl

import numpy as np
import pandas as pd
inputfile ='C:\\Users\\Administrator\\Desktop\\FinancialForecast\\data\\data1.csv' #输入的数据文件
data = pd.read_csv(inputfile) #读取数据
c=np.round(data.corr(method = 'pearson'), 2) #计算相关系数矩阵，保留两位小数
print(c)