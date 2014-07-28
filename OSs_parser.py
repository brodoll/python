# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:28:36 2014

@author: Eolica
"""
import pdfquery

pdf = pdfquery.PDFQuery("\\\\cerebro\\PMS\\OSs\\WTG12-52238631.pdf")
pdf.load()
label = pdf.pq('LTTextLineHorizontal:contains("Turbine No./Id:")')
left_corner = float(label.attr('x0'))
bottom_corner = float(label.attr('y0'))
name = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (left_corner, bottom_corner-30, left_corner+150, bottom_corner)).text()
