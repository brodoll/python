# -*- coding: utf-8 -*-
"""
Created on Tue May 13 08:56:00 2014

@author: Eolica
"""

file = open('C:\\Test\\mdesc\\santaclara.txt', 'rt')
txt = file.read()

# Solution for positive integers only
#[int(s) for s in txt.split() if s.isdigit()]

l = []
for t in txt.split():
    try:
        l.append(float(t))
    except ValueError:
        pass

file.close()