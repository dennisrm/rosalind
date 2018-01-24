# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 00:03:39 2018

@author: Dennis
"""
import numpy as np

n = 87
m = 19

rabbits = np.zeros((n,m),dtype = np.int64)
rabbits[0,0] = 1
pairs = [1]
for i in range(1,n):
    rabbits[i,0] = np.sum(rabbits[i-1,1:],dtype=np.int64)
    for j in range(1,m):
        rabbits[i,j]=rabbits[i-1,j-1]
    pairs += [np.sum(rabbits[i,],dtype=np.int64)]
       
       