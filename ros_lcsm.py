# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 22:18:01 2018

@author: Dennis
"""

#For finding the longest common substring

from datetime import datetime
startTime = datetime.now()
####
from fasta import fasta
import numpy as np

names,strings = fasta("rosalind_lcsm.txt")

s = strings[0]
t = strings[1]
m = len(s)
n = len(t)

csarray = np.zeros((m,n))

for i in range(0,m):
    for j in range(0,n):
        if s[i] == t[j]:
            if i == 0 or j == 0:
                csarray[i,j] = 1
            else:
                csarray[i,j] = csarray[i-1,j-1]+1

cslens = ([max(csarray[i,]) for i in range(0,m)])


cslist = []
for i in range(0,m):
    start = int(i-cslens[i]+1)
    cslist += [s[start:i+1]]
    

    
substrlen = max(cslens)
found = False
while substrlen > 0 and found == False:
    tocheck = [cslist[i] for i in range(0,len(cslist)) if len(cslist[i]) == substrlen]
    for i in range(2,len(strings)):
        newcheck = []
        for check in tocheck:
            if strings[i].find(check) >= 0:
                newcheck += [check]
        tocheck = newcheck
    if len(tocheck) > 0:
        found = True
    substrlen -= 1
    
print(tocheck)
##
print(datetime.now() - startTime)
