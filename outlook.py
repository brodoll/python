# -*- coding: utf-8 -*-
"""
Created on Wed Jan 08 11:46:38 2014

@author: Eolica
"""

import win32com.client

session = win32com.client.gencache.EnsureDispatch ("MAPI.Session")

#
# Leave blank to be prompted for a session, or use
# your own profile name if not "Outlook". It is also
# possible to pull the default profile from the registry.
#
session.Logon ("Outlook")
messages = session.Inbox.Messages

#
# Although the inbox_messages collection can be accessed
# via getitem-style calls (inbox_messages[1] etc.) this
# is the recommended approach from Microsoft since the
# Inbox can mutate while you're iterating.
#
message = messages.GetFirst ()
while message:
  print message.Subject
  message = messages.GetNext ()
  
class Folder (object):
  def __init__ (self, folder):
    self._folder = folder
  def __getattr__ (self, attribute):
    return getattr (self._folder, attribute)
  def __iter__ (self):
    #
    # NB You *must* collect a reference to the
    # Messages collection here; otherwise GetFirst/Next
    # resets every time.
    #
    messages = self._folder.Messages
    message = messages.GetFirst ()
    while message:
      yield message
      message = messages.GetNext ()

if __name__ == '__main__':
  import win32com.client
  session = win32com.client.gencache.EnsureDispatch ("MAPI.Session")
  constants = win32com.client.constants
  session.Logon ()
  
  sent_items = Folder (session.GetDefaultFolder (constants.CdoDefaultFolderSentItems))
  for message in sent_items:
    print message.Subject