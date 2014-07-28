# -*- coding: utf-8 -*-
"""
Created on Tue Jan 07 08:31:17 2014

@author: Eolica
"""

import win32com.client
import os.path
import unicodedata
import re
import urllib

class OutlookLib:
        
    def __init__(self, settings={}):
        self.settings = settings
        
    def get_messages(self, user, folder="Caixa de Entrada", match_field="all", match="all"):      
        outlook = win32com.client.Dispatch("Outlook.Application")
        myfolder = outlook.GetNamespace("MAPI").Folders[user] 
        inbox = myfolder.Folders[folder] # Inbox
        if match_field == "all" and match =="all":
            return inbox.Items
        else:
            messages = []
            for msg in inbox.Items:
                try:
                    if match_field == "Sender":
                        if msg.SenderName.find(match) >= 0:
                            messages.append(msg)
                    elif match_field == "Subject":
                        if msg.Subject.find(match) >= 0:
                            messages.append(msg)
                    elif match_field == "Body":
                        if msg.Body.find(match) >= 0:
                            messages.append(msg)
                    #print msg.To
                    #msg.Attachments
                        # a = item.Attachments.Item(i)
                        # a.FileName
                except:
                    pass
            return messages
        
    def get_body(self, msg):
        return msg.Body
    
    def get_subject(self, msg):
        return msg.Subject
    
    def get_sender(self, msg):
        return msg.SenderName
    
    def get_recipient(self, msg):
        return msg.To
    
    def get_attachments(self, msg):
        return msg.Attachments
        
def save_attachments(msg,path):
    attachments = msg.Attachments
    for i in range(attachments.Count):
        attachment = attachments.Item(i + 1) # indexes are 1 based
        filename = os.path.join(path,attachment())
        
        try:
            filename.decode('utf-8')
        except:
            filename = unicodedata.normalize('NFKD', filename).encode('ascii','ignore')    
        
        if os.path.isfile(filename):
            print 'File already exists.'
        else:
            attachment.SaveASFile(filename)
            print filename + ' saved.'

outlook = OutlookLib()
clipping_path = 'C:\\Clipping\\'
#messages = outlook.get_messages('guilherme@eolica.com.br','Clipping','Sender','A. J. Orlando')
#for msg in messages:
#    save_attachments(msg,clipping_path)
    
#forecasts_path = 'C:\\Test\\Forecasts\\'
#forecasts_messages = outlook.get_messages('pms@eolica.com.br','Caixa de Entrada','Sender','Meteologica')
#for msg in forecasts_messages:
#    save_attachments(msg,forecasts_path)

messages = outlook.get_messages('guilherme@eolica.com.br','Clipping','Subject','Di')
for msg in messages:
    print msg.Subject
    
body = unicodedata.normalize('NFKD', msg.Body).encode('ascii','ignore')

# Splitting string method. 
#start = 'HYPERLINK "'
#end = '"'
#print((body.split(start))[1].split(end)[0])

# 1 occurrence (1st) only with regexp
#r = re.compile('HYPERLINK "(.*?)"')
#m = r.search(body)

# Retrieving all links from e-mail body using regexp
r = re.findall('HYPERLINK "(.*?)"',body)
dlink = r[1] # 2nd link is the pdf attachment
tlink = 'http://diariodosventos.com.br/wp-content/uploads/2014/07/Di%C3%A1rio-dos-Ventos-20140707-1341.pdf'
urllib.urlretrieve(tlink,'teste.pdf')


