# -*- coding: utf-8 -*-
# 时间    : 2018/10/18 10:13
# 作者    : xcl

import pandas as pd
inputfile ='C:\\Users\\Administrator\\Desktop\\FinancialForecast\\data\\data1.csv' #输入的数据文件
data = pd.read_csv(inputfile) #读取数据

#该方法已被python弃用
#导入AdaptiveLasso算法，要在较新的Scikit-Learn才有。
#from sklearn.linear_model import AdaptiveLasso
#model = AdaptiveLasso(gamma=1)
#model.fit(data.iloc[:,0:13],data['y'])
#model.coef_ #各个特征的系数



#最基本的
from sklearn import linear_model
clf = linear_model.LassoLars(alpha=1)
clf.fit(data.iloc[:,0:13],data['y'])
coef=clf.coef_
print(coef)


