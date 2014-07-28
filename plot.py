# -*- coding: utf-8 -*-
"""
Created on Fri May 02 08:17:28 2014

@author: Eolica
"""

from xml.dom import minidom

file = open('C:\\Test\\xml\\xmd\\AL1_22  Planetary Radial (Lss) Acell 05 e 06_05_2014.xmd', 'rt')
xmldoc = minidom.parse(file)

DateNodeList = xmldoc.getElementsByTagName('RawData')
Date = DateNodeList.item(0).firstChild.nodeValue
#IDNodeList = xmldoc.getElementsByTagName('MeasDate')
#ID = IDNodeList.item(0).firstChild.nodeValue
#print Date
#print ID
valores = []
for node in DateNodeList:
     valores.append(node.firstChild.nodeValue)

print DateNodeList.length

#plot(valores)

xmldoc.unlink()
file.close()
