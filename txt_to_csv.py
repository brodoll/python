# -*- coding: utf-8 -*-
"""
Created on Thu Jan 09 09:52:51 2014

@author: Eolica
"""

#import csv
#
#txt_file = r"C:\\Test\\txttocsv\\txtfile2.txt"
#csv_file = r"mycsv.csv"
#
#in_txt = csv.reader(open(txt_file, "rb"), delimiter = '\t')
#out_csv = csv.writer(open(csv_file, 'wb'))
#
#out_csv.writerows(in_txt)

import csv

# Read comma delimited file
with open('C:\\Test\\txttocsv\\TXTFILE.txt','rb') as fin:
    cr = csv.reader(fin,delimiter=';')
    filecontents = [line for line in cr]
    
with open('yourfile16.csv','wb') as fou:
    cw = csv.writer(fou, delimiter='\t')
    cw.writerows(filecontents)

## read tab-delimited file
#with open('C:\\Test\\txttocsv\\TXTFILE.txt','rb') as fin:
#    cr = csv.reader(fin, delimiter='\t')
#    filecontents = [line for line in cr]
#
## write comma-delimited file (comma is the default delimiter)
#with open('yourfile.csv','wb') as fou:
#    cw = csv.writer(fou, quotechar='', quoting=csv.QUOTE_NONE)
#    cw.writerows(filecontents)