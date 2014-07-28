# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 18:48:58 2014

@author: Eolica
"""
import win32com.client

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