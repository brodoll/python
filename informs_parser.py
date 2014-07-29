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
        aux = [i for i, s in enumerate(clnbody) if s.startswith(header)]
#        aux = [i for i, s in enumerate(clnbody) if header in s]
#        if len(aux)>1:
#            # Check for tac 84/85
#            tac = '8'+header
#            tacaux = [i for i, s in enumerate(clnbody) if tac in s]
#            s = set(tacaux)
#            temp = set(aux)-set(tacaux)
#            aux = list(temp)
        
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
                    checks = ['Sem','sem','Sen','sen','DDS','Visita','visita',\
                    'Reuni','reuni']
                    for check in checks not in item:
                        if j==5:
                        #print 'Error! Invalid String found ' + data +'!'
                            print item
                        else:
                            #print 'Error! Please check item.'
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
messages = outlook.get_messages('guilherme@eolica.com.br','Esteban','Sender','Esteban')
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



## Test with simulated 2 informs mail
#
#bbody = ['Informe diario do dia 22/07/2014', ' ', '1.     Servicos planejados: ', ' ', 'a.        WTG 41 AL2  Service B 1,5 year.', 'b.       WTG 37 AL2  Service B 1,5 year.', 'c.        WTG 22 AL2  Service B 1,5 year.', ' ', '2.     Trabalhos nao planejados / manutencao corretiva:', ' ', 'a.       WTG 22 AL1   Alarme Hub computer com Fault,  pin  solto na caixa conexao AK4  do hub.', 'b.      WTG 17 AL2 -  Alarme Hub valve supply test fault,  fonte alimentacao con defeito no Hub.', 'c.       WTG 34 AL2  Alarme Blade 1 not at stop defeito na valvula proporcional.', 'd.      WTG 55 AL2  Alarme Hub pump inlet pressure low defeito na bomba feeder pump do  Sistema Hidraulico do pitch.', ' ', ' ', '3.     Turbinas paradas:', '                      Sem item.', ' ', '4.     Seguranca:', 'Sem Item ', ' ', '5.     Outros:', ' ', ' ', 'Yours sincerely / Atenciosamente', 'Esteban Jose Montoro Lopez', 'Supervisor Service', 'Service Brazil', ' ', 'Vestas Do Brazil', 'M +55 (84) 9847-1221', 'HYPERLINK "mailto:esmlo@vestas.com"esmlo@vestas.com', 'HYPERLINK "http://www.vestas.com/"http://www.vestas.com', ' ', 'Informe diario do dia 25/07/2014', ' ', '1.     Servicos planejados: ', ' ', 'a.        WTG 41 AL2  Service B 1,5 year.', 'b.       WTG 37 AL2  Service B 1,5 year.', 'c.        WTG 22 AL2  Service B 1,5 year.', ' ', '2.     Trabalhos nao planejados / manutencao corretiva:', ' ', 'a.       WTG 22 AL1   Alarme Hub computer com Fault,  pin  solto na caixa conexao AK4  do hub.', 'b.      WTG 17 AL2 -  Alarme Hub valve supply test fault,  fonte alimentacao con defeito no Hub.', 'c.       WTG 34 AL2  Alarme Blade 1 not at stop defeito na valvula proporcional.', 'd.      WTG 55 AL2  Alarme Hub pump inlet pressure low defeito na bomba feeder pump do  Sistema Hidraulico do pitch.', ' ', ' ', '3.     Turbinas paradas:', '                      Sem item.', ' ', '4.     Seguranca:', 'Sem Item ', ' ', '5.     Outros:', ' ', ' ', 'Yours sincerely / Atenciosamente', 'Esteban Jose Montoro Lopez', 'Supervisor Service', 'Service Brazil', ' ', 'Vestas Do Brazil', 'M +55 (84) 9847-1221', 'HYPERLINK "mailto:esmlo@vestas.com"esmlo@vestas.com', 'HYPERLINK "http://www.vestas.com/"http://www.vestas.com', ' ']
#if 'Rela' in msg.Subject:
#    # Cleaning / Formatting message
#
#    body = filter(bool, bbody)
#    clnbody = [ v for v in body if not v.startswith(' ') ]
#    
#    #Verify multiple informs in single e-mail
#    ni = miverifier(clnbody,'Informe')
#    
#    if ni>1:
#        # Divinding body message into different informs
#        aux = [i for i, s in enumerate(clnbody) if 'Informe' in s]
#        aux.append(len(clnbody))
#        for j in range(len(aux)-1):
#            singleclnbody = clnbody[aux[j]:aux[j+1]]
#            classifier(singleclnbody,dList,keys)
#            
#    else:
#        classifier(clnbody,dList,keys)

