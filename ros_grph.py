# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 13:29:35 2018

@author: Dennis
"""

from fasta import fasta

names,strings = fasta("rosalind_grph.txt")

ajlist = []
k = 3

for i in range(0,len(strings)):
    for j in range(0,len(strings)):
        if i != j:
            match = True
            for n in range(0,k):
                if match and strings[i][-k+n] == strings[j][n]:
                    match = True
                else:
                    match = False
            if match:
                ajlist += [(i,j)]

f = open("output.txt","w")       
output= ""         
for aj in ajlist:
    output += names[aj[0]] + " " + names[aj[1]] + "\n"

f.write(output)
f.close()