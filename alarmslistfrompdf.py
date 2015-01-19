# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 15:49:00 2015

@author: Eolica
"""

import pdfquery

pdf = pdfquery.PDFQuery("\\\\cerebro\\PMS\Documentos\\VESTAS\\V82 Operations Manual (Extractions)\\NM82 Error and Log List (Alarm_475) 070816.pdf")
pdf.load()
label = pdf.pq('LTTextLineHorizontal:contains("Turbine No./Id:")')
left_corner = float(label.attr('x0'))
bottom_corner = float(label.attr('y0'))
alarmno = np.matrix('143 182; 78 328; 144 361; 78 509; 143 542; 78 690')
pdf.extract([
    ('upper_code', ':in_bbox("78,328,143,182")'),
    ('middle_code', ':in_bbox("78,509,144,361")'),
    ('bottom_code', ':in_bbox("78,690,143,542")'),
    ('upper_name', ':in_bbox("143,199,331,182")'),
    ('middle_name', ':in_bbox("143,337,334,362")'),
    ('bottom_name', ':in_bbox("144,556,334,542")'),
 ])
