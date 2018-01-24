# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 22:11:10 2018

@author: Dennis
"""

exper = [2, 2, 2, 1.5, 1, 0]

data = [19432, 18664, 17298, 16456, 16326, 19748]

expected = 0

for i in range(0,len(data)):
    expected += data[i]*exper[i]
    
print(expected)