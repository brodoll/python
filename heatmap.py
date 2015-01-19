# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 09:32:10 2015

@author: Eolica
"""

from collections import OrderedDict

from bokeh.sampledata.unemployment1948 import data
from bokeh.charts import HeatMap
import pandas as pd


xl = pd.ExcelFile(u'Z:\Routines\CONTROLE\REGRESSION v03\AL-2013-2014.xls')
logbook = xl.parse(xl.sheet_names[0])
s2=logbook.groupby('Unit').Code.value_counts()

# pandas magic
df = data[data.columns[:-2]]
df2 = df.set_index(df[df.columns[0]].astype(str))
df2.drop(df.columns[0], axis=1,level=None)
df3 = df2.transpose()

cols = df3.columns.tolist()
index = df3.index.tolist()

#prepare some inputs
to_odict = lambda v: OrderedDict((kk, v[kk]) for kk in index)

# Create an ordered dict (or ordered dicts) with the data from the DataFrame
datadict = df3.to_dict()
data = OrderedDict(sorted((k, to_odict(v)) for k, v in datadict.items()))

# any of the following commented line is a valid HeatMap input
#data = df3
#data = df3.values.T
#data = list(df3.values.T)

hm = HeatMap(data, title="categorical heatmap", filename="cat_heatmap.html")
hm.width(1000).height(400).show()