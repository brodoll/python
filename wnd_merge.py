# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 09:21:57 2014

@author: Eolica
"""

import glob

read_files = glob.glob("*.wnd")

with open("Result.wnd", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
                outfile.write(infile.read())
                print f+"updated"