# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 18:04:05 2014

@author: Eolica
"""

import unicodedata
import OutlookLib
import re
import dateutil.parser as dparser

def classifier(clnbody,dList,keys):
    # Getting Data and Date off e-mail body dd/mm/yyyy
    dateobject = dparser.parse(clnbody[0],fuzzy=True,dayfirst=True)
    data = dateobject.strftime("%d/%m/%Y")
    date = dateobject.strftime("%Y%m%d")
    
    # E-mail classifier delimiters
    email_headers = ['1.','2.','3.','4.','5.','Yours']
    indexes = list()
    
    # Splitting into categories (PL, NP, P, S)
    for header in email_headers:
        aux = [i for i, s in enumerate(clnbody) if header in s]
        indexes = indexes + aux
    
    for j in range(len(indexes)-1):
        interventions = clnbody[indexes[j]+1:indexes[j+1]]
        
        # Category coding        
        if j==0:
            cat = 'PL'
        elif j==1:
            cat = 'NP'
        elif j==2:
            cat = 'P'
        elif j==3:
            cat = 'S'
        else:
            cat = 'O'
   
        
        # Check if list is empty. If not writes to dict
        if interventions:
            for item in interventions:
                try:
                    # Park
                    idx1 = item.index('AL')
                    wf = item[idx1:idx1+3]
                    
                    #Turbine
                    aux = re.search('WTG(.*)AL', item)
                    wtg = aux.group(1).strip()
                    
                    # Description
                    desc = item[idx1+4:].strip()
                    
                    # Writing to dictionary
                    ipt = [data,date,wf,wtg,desc,cat]
                    dList.append(dict(zip(keys,ipt)))
                    
                except:
                    if 'Sem' not in item:
                        if 'sem' not in item:
                            print 'Error! Invalid String found ' + data +'!'
                            print item
                
    return dList
            
# Dict keys (column headers of output file / db)
keys = ['Data','Date','Wind Farm','WTG','Description','Category']
dList = []
    
outlook = OutlookLib.OutlookLib()
messages = outlook.get_messages('guilherme@eolica.com.br','Esteban','Sender','Esteban')
for msg in messages:
    if 'Rela' in msg.Subject:
        # Cleaning / Formatting message
        body = unicodedata.normalize('NFKD', msg.Body).encode('ascii','ignore')
        body = body.splitlines()
        body = filter(bool, body)
        clnbody = [ v for v in body if not v.startswith(' ') ]
        
        classifier(clnbody,dList,keys)




