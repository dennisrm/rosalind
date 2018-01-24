# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 13:46:46 2018

@author: Dennis
"""


def fasta(filename):
    file = open(filename).read().split()

    first = True
    names = []
    strings = []
    
    for string in file:
        if string[0] == ">":
            names += [string[1:]]
            if first:
                first = False
            else:
                strings += [s]
            s = ""
        else:
            s += string
    strings += [s]
    return (names,strings)