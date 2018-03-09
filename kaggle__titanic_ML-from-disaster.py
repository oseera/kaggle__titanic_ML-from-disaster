# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 11:23:52 2018

@author: Om
"""

import pandas as pd

train=pd.read_csv("../../Datasets/kaggle__titanic_ML-from-disaster/train.csv",)
test=pd.read_csv(("../../Datasets/kaggle__titanic_ML-from-disaster/test.csv"))

from matplotlib import pyplot as plt


x1 = [1, 2, 3, 4, 7]
y1 = [1, 4, 9, 16,25]

x2=[-35,-59,-55,63,70]
y2=[-41,30,51,7,9]

if True :
    x3=[1,3,4,5],[23,1,10,14],[14,9,12,16]
    y3=[7,-8,12,2],[0,15,20,22],[5,7,9,10]
else:
    x3=[1,2,3,4,5,23,2,1,10,14,14,1,9,12,16]
    y3=[7,9,-8,12,2,0,5,15,20,22,5,15,7,9,10]

plt.axis([0, 5, 0, 20])
plt.title("Test Plot")
plt.xlabel("X Test")
plt.ylabel("Y Test")

plt.legend()
plt.show()

plt.axis([0, 8, 0, 30])
plt.title("Plot 1")
plt.xlabel("X1")
plt.ylabel("Y1")

plt.bar(x1, y1, label="1", color="cyan")
plt.legend()
plt.show()

plt.axis([-80,80,-80,80])
plt.title("Plot 2")
plt.xlabel("X2")
plt.ylabel("Y2")

plt.bar(x2,y2,label="2", color="red")
plt.legend()
plt.show()

plt.axis([-10,30,-10,30])
plt.title("Plot 3")
plt.xlabel("X3")
plt.ylabel("Y3")

plt.plot(x3,y3,'r*',label="3")
plt.legend()
plt.show()

