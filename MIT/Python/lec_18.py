#-*- encoding: utf-8 -*-
'''
Created on 2016-06-20 17:41:59

@author: Srgzyq
'''
from pylab import *
import random

#plot([1, 2, 3, 4])
#plot([5, 6, 7, 8])
plot([1, 2, 3, 4], [1, 4, 9, 16])  # x，y
figure()

plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')  # r:红色 o:表示点
axis([0, 6, 0, 20])  # 一个坐标是0到6 一个坐标是0到20
title('Earnings')
xlabel('Days')
ylabel('Dollars')
figure()

xAxis = array([1, 2, 3, 4])  # array 在Numpy中表示行列式
print xAxis
test = arange(1, 5)
print test
print test == xAxis
yAxis = xAxis**3
print yAxis
plot(xAxis, yAxis, 'ro')
figure()
vals = []
dieVals = [1, 2, 3, 4, 5, 6]
for i in range(10000):
    vals.append(random.choice(dieVals) + random.choice(dieVals))
hist(vals, bins=11)
show()
