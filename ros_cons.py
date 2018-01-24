# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 22:47:41 2018

@author: Dennis
"""

file = open("rosalind_cons.txt").read().splitlines()
import numpy as np
first = True
for n in range(0,len(file)):
    if file[n][0] == ">":
        if first:
            first = False
            strings = []
        else:
            strings += [string]
        string = ""
        
    else:
        string += file[n]
strings += [string]
           
lenS = len(strings[0])
lenL = len(strings)

basecountarray = np.zeros((4,lenS),dtype = "int")
bases = {0:"A",1:"C",2:"G",3:"T"}

cons = ""
for i in range(0,lenS):
    for j in range (0,lenL):
        if strings[j][i] == "A":
            basecountarray[0,i] += 1
        elif strings[j][i] == "C":
             basecountarray[1,i] += 1
        elif strings[j][i] == "G":
             basecountarray[2,i] += 1
        elif strings[j][i] == "T":
             basecountarray[3,i] += 1

A = "A: "+" ".join(str(i) for i in basecountarray[0])
C = "C: "+" ".join(str(i) for i in basecountarray[1])
G = "G: "+" ".join(str(i) for i in basecountarray[2])
T = "T: "+" ".join(str(i) for i in basecountarray[3])

winners = np.argmax(basecountarray,axis=0)
cons = "".join(str(bases[i]) for i in winners)

f = open("xx.txt","w")
f.write(cons+"\n"+A+"\n"+C+"\n"+G+"\n"+T)
f.close()