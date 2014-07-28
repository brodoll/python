# -*- coding: utf-8 -*-
"""
Created on Wed Jan 08 18:30:42 2014

@author: Eolica
"""

import xml.etree.ElementTree as et

#with open('C:\\Test\\xml\\0000104542_SP-27646-001_36613_52238625_20131223_20131223.xml', 'rt') as f:
with open('C:\\Test\\xml\\Alegria01 20_30_05_2014.xmd', 'rt') as f:
    tree = et.parse(f)
#    print tree

#for node in tree.iter():
##    print node.tag, node.attrib
#    name = node.attrib.get('text')
#    url = node.attrib.get('LINE')
#    if name and url:
#        print '  %s :: %s' % (name, url)
#    else:
#        print name

out = open('titles.txt', 'w')

root = tree.getroot()
for child in root:
    out.write('%s\n' % child.tag)
    #print child.tag,child.attrib

out.close()

#for MeasDate in root.iter(tag='MeasDate'):
#      print MeasDate.tag,MeasDate