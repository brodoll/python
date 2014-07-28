# -*- coding: utf-8 -*-
"""
Created on Fri May 02 09:05:14 2014

@author: Eolica
"""

from lxml import etree

def fast_iter(context, func):
    for event, elem in context:
        func(elem)
        elem.clear()
        while elem.getprevious() is not None:
            del elem.getparent()[0]
    del context
    
def prt2f(elem,out):
    out.write( '%s\n' % elem.text.encode('utf-8'))
     #print '%s\n' % elem.text.encode('utf-8')

def prt(elem):
    print elem.tag
    
def cont(n):
    n=n+1
    return n
    #print '%s\n' % elem.text.encode('utf-8')
     
infile = 'C:\\Test\\xml\\Al1_02 03 a 05_05_2014.xmd'

doc = etree.parse(infile)

context = etree.iterparse(infile, events=('end',), tag='TrendMultiple')
count = 0
#out = open('C:\\Test\\xml\\titles.txt', 'w')
fast_iter(context,
          lambda elem:
              prt(elem))
#out.close()

########################################################
# Explicit loop for solution above (instead of function)

#out = open('titles.txt', 'w')
#
#for event, elem in context:
#    print '%s\n' % elem.text.encode('utf-8')
#    #out.write('%s\n' % elem.text.encode('utf-8'))
#     # It's safe to call clear() here because no descendants will be accessed
#    elem.clear()
#    # Also eliminate now-empty references from the root node to <Title> 
#    while elem.getprevious() is not None:
#         del elem.getparent()[0]
#       
#out.close()

########################################################
# Another way to handle iterparsing

## get an iterable
#context = etree.iterparse(infile, events=("start", "end"))
#
## turn it into an iterator
#context = iter(context)
#
## get the root element
#event, root = context.next()
#
##for event, elem in context:
##    if event == "start":
##        print root.tag
##	root.clear()
#
#for parent in root:
#    print parent.tag
    
########################################################