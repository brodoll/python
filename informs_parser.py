# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 18:04:05 2014

@author: Eolica
"""

import unicodedata
import OutlookLib

def classifier(clnbody):
    headers = ['1.','2.','3.','4.','5.','Yours']
    indexes = list()
    for header in headers:
        aux = [i for i, s in enumerate(clnbody) if header in s]
        indexes = indexes + aux
        
    #return indexes
        

    
outlook = OutlookLib.OutlookLib()
messages = outlook.get_messages('guilherme@eolica.com.br','Esteban','Sender','Esteban')
for msg in messages:
    print msg.Subject
    
body = unicodedata.normalize('NFKD', msg.Body).encode('ascii','ignore')
body = body.splitlines()
body = filter(bool, body)
clnbody = [ v for v in body if not v.startswith(' ') ]

classifier(clnbody)


