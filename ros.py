# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:31:02 2018

@author: Dennis
"""

file = open("codons.txt").read().split()

even,odd = [], []

for i in range(0,len(file)):
    if i % 2 == 0:
        even += [i]
    else:
        odd += [i]

codons = dict(zip([file[i] for i in even],[file[i] for i in odd]))

rna = open("rosalind_prot.txt").read().strip()


j=0
protein = ""
aa = ""
while aa != "Stop" or j < len(rna):
    protein += aa
    aa = codons[rna[j:j+3]]
    j += 3
    
print(protein)