# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 07:09:32 2014

@author: Eolica
"""

import glob
import os
from os import listdir

#for filename in glob.glob('C:\\FTP_RAW_DATA\\temp\*.csv'):
#    if len(filename) > 3:
#        new_filename = 'C:\\FTP_RAW_DATA\\temp\\DailyDataAL2_Alegria_AL2_01_-_30_Turbs_2014-'+filename[49:]
#        os.rename(filename, new_filename)
        
#for filename in glob.glob('C:\\FTP_RAW_DATA\\temp\*.csv'):
#    if len(filename) > 3:
#        new_filename = 'C:\\FTP_RAW_DATA\\temp\\DailyDataAL2_Alegria_AL2_31_-_61_Turbs_2014-'+filename[50:]
#        os.rename(filename, new_filename)


fnames = listdir('C:\\Users\\Eolica\\Desktop\\Documentos\\Fase1\\')

raw = glob.glob('C:\\Users\\Eolica\\Desktop\\Documentos\\Fase1\\*.*')

path = 'C:\\Users\\Eolica\\Desktop\\Documentos\\Fase1\\'

for filename in fnames:
    if filename.startswith('Anexo 7_'):
        new_filename = '14-'+filename[8:]
        os.rename(path+filename, path+new_filename)