# -*- coding: utf-8 -*-
# 时间    : 2018/10/18 13:34
# 作者    : xcl
import numpy as np
import pandas as pd
inputfile ='C:\\Users\\Administrator\\Desktop\\FinancialForecast\\data\\data1.csv' #输入的数据文件

data = pd.read_csv(inputfile) #读取数据
# GM模型，预测
def GM11(x0): #自定义灰色预测函数
  import numpy as np
  x1 = x0.cumsum() #1-AGO序列
  x1 = pd.DataFrame(x1)
  z1 = (x1 + x1.shift())/2.0 #紧邻均值（MEAN）生成序列
  z1 = z1[1:].values.reshape((len(z1)-1,1))  # 转成矩阵
  B = np.append(-z1, np.ones_like(z1), axis = 1)  # 列合并-z1和形状同z1的1值矩阵  19X2
  Yn = x0[1:].reshape((len(x0)-1, 1))  # 转成矩阵 19
  [[a],[b]] = np.dot(np.dot(np.linalg.inv(np.dot(B.T, B)), B.T), Yn) #计算参数，基于矩阵运算，np.dot矩阵相乘，np.linalg.inv矩阵求逆
  f = lambda k: (x0[0]-b/a)*np.exp(-a*(k-1))-(x0[0]-b/a)*np.exp(-a*(k-2)) #还原值
  delta = np.abs(x0 - np.array([f(i) for i in range(1,len(x0)+1)]))  # 残差绝对值序列
  C = delta.std()/x0.std()
  P = 1.0*(np.abs(delta - delta.mean()) < 0.6745*x0.std()).sum()/len(x0)
  return f, a, b, x0[0], C, P #返回灰色预测函数、a、b、首项、方差比、小残差概率

#x0=data_1['x3'][:-2].values


l=['x3','x5','x7','x11','y']
data_1=data[l].copy()
data_1.index=range(1994,2014)
data_1.loc[2014]=None  # 添加预测行
data_1.loc[2015]=None

outputfile = 'C:\\Users\\Administrator\\Desktop\\data1_GM11.xls' #灰色预测后保存的路径

for i in l:  # 列计算，预测每列2014、2015预测值
    f=GM11(data_1[i][:-2].values)[0]  # 利用返回的灰色预测函数，仅和对对应期数及位置有关
    data_1[i][2014]=f(len(data_1)-1)
    data_1[i][2015]=f(len(data_1))
    data_1[i]=data_1[i].round(2)
    #print(data_1)
    data_1.to_excel(outputfile, "a+")


print(data_1["x3"][:-2].values)