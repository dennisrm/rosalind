# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:06:46 2018

@author: Dennis
"""

s,t = open("rosalind_subs.txt").read().splitlines()



output = []

for i in range(0,len(s)):
    match = False
    if s[i] == t[0]:
        match = True
        for j in range(0,len(t)):
            if s[i+j] != t[j]:
                match = False
    if match:
        output += [i+1]
        
print(output)