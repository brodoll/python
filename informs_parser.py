# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 18:04:05 2014

@author: Eolica
"""

import unicodedata
import OutlookLib
import re
import dateutil.parser as dparser
import csv
from operator import itemgetter


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
        aux = [i for i, s in enumerate(clnbody) if s.startswith(header)]
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
                    nwtg = len(wtg.split(','))
                    
                    # Description
                    desc = item[idx1+4:].strip()
                    desc = desc.replace('-','')
                    desc = desc.replace('=','')
                    
                    # Writing to dictionary
                    if nwtg==1:
                        ipt = [data,date,wf,wtg,desc,cat]
                        dList.append(dict(zip(keys,ipt)))
                    else:
                        for turb in wtg.split(','):
                            ipt = [data,date,wf,turb,desc,cat]
                            dList.append(dict(zip(keys,ipt)))
                    
                except:
                    checks = ['Sem','sem','Sen','sen','DDS','Visita','visita',\
                    'Reuni','reuni']
                    if any(check in item for check in checks):
                        continue
                    else:
                        print item
                        print data
       
    return dList
    
def miverifier(list_of_lists, substring):
    count = 0.0
    for item in list_of_lists:
        if substring in item:
            count += 1
    return count
    
# Dict keys (column headers of output file / db)
keys = ['Data','Date','Wind Farm','WTG','Description','Category']
dList = []

outlook = OutlookLib.OutlookLib()
#messages = outlook.get_messages('guilherme@eolica.com.br','Esteban','Sender','Esteban')
##messages = outlook.get_messages('Guilherme Pedrosa','Caixa de entrada','Sender','Esteban')
#for msg in messages:
#    if 'Rela' in msg.Subject:
#        # Cleaning / Formatting message
#        body = unicodedata.normalize('NFKD', msg.Body).encode('ascii','ignore')
#        body = body.splitlines()
#        body = filter(bool, body)
#        clnbody = [ v for v in body if not v.startswith(' ') ]
#        
#        #Verify multiple informs in single e-mail
#        ni = miverifier(clnbody,'Informe')
#        
#        if ni>1:
#            # Divinding body message into different informs
#            aux = [i for i, s in enumerate(clnbody) if 'Informe' in s]
#            aux.append(len(clnbody))
#            for j in range(len(aux)-1):
#                singleclnbody = clnbody[aux[j]:aux[j+1]]
#                classifier(singleclnbody,dList,keys)
#                
#        else:
#            classifier(clnbody,dList,keys)
#
#with open('C:\\test\\informs_output.csv', 'wb') as f:  # Just use 'w' mode in 3.x
#    w = csv.DictWriter(f, keys)
#    w.writeheader()
#    ord_dList = sorted(dList,key=itemgetter('Date'))
#    w.writerows(ord_dList)

messages = outlook.get_messages('Guilherme Pedrosa','Caixa de entrada','Sender','Esteban')
for msg in messages:
    if 'Rela' in msg.Subject:
        # Cleaning / Formatting message
        body = unicodedata.normalize('NFKD', msg.Body).encode('ascii','ignore')
        body = body.splitlines()
        body = filter(bool, body)
        clnbody = [ v for v in body if not v.startswith(' ') ]
        
        #Verify multiple informs in single e-mail
        ni = miverifier(clnbody,'Informe')
        
        if ni>1:
            # Divinding body message into different informs
            aux = [i for i, s in enumerate(clnbody) if 'Informe' in s]
            aux.append(len(clnbody))
            for j in range(len(aux)-1):
                singleclnbody = clnbody[aux[j]:aux[j+1]]
                classifier(singleclnbody,dList,keys)
                
        else:
            classifier(clnbody,dList,keys)

with open('C:\\test\\informs_output.csv', 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, keys)
    w.writeheader()
    ord_dList = sorted(dList,key=itemgetter('Date'))
    w.writerows(ord_dList)