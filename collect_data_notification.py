# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:31:54 2013

@author: Eolica
"""
import smtplib, datetime

def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='eolica.com.br:25'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
    
    to_addrs = to_addr_list+cc_addr_list
    server = smtplib.SMTP(smtpserver)
    server.login(login,password)
    server.sendmail(from_addr, to_addrs, message)
    server.quit()
    
data = datetime.datetime.now().strftime("%b %Y")
message_Marrison = (u"Marrison,\n " +
u"\t    Gostaria de lembra-lo da coleta dos dados de vento das torres de AL1 e "+
u"AL2 para confeccao dos relatorios mensais de performance. \n"+
u"Atte.,\n"
u"\t Eolica PMS")
message_Eduardo = (u"Eduardo,\n " +
u"\t    Gostaria de lembra-lo de solicitar a coleta dos dados de vento das torres de GVT, "+
u"XVT e PIR para confeccao dos relatorios mensais de performance. \n"+
u"Atte.,\n"
u"\t Eolica PMS")
sendemail(from_addr    = 'pms@eolica.com.br', 
          to_addr_list = ['eduardo@eolica.com.br'],
          cc_addr_list = ['camila@eolica.com.br','guilherme@eolica.com.br','tania@eolica.com.br'], 
          subject      = "Coleta de dados da Torre - " + data,
          message      = message_Eduardo,
          login        = 'pms',
          password     = 'pms2013@')

sendemail(from_addr    = 'pms@eolica.com.br', 
          to_addr_list = ['marrison.souza@neog.com.br'],
          cc_addr_list = ['franciele@eolica.com.br','camila@eolica.com.br','guilherme@eolica.com.br','tania@eolica.com.br'], 
          subject      = "Coleta de dados da Torre - " + data,
          message      =  message_Marrison,
          login        = 'pms',
          password     = 'pms2013@')




