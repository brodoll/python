# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 18:08:39 2014

@author: Eolica
"""

import argparse
import pandas as pd
import numpy as np 

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers (default: find the max)')

args = parser.parse_args()
print args.accumulate(args.integers)