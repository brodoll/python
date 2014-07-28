# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 13:51:02 2014

@author: Eolica
"""

import csv, sqlite3, os

#indir = 'C:\\FORECAST_RAW_DATA\\'

indir = 'C:\\Test\\Forecasts\\'
db = 'C:\\FORECAST_RAW_DATA\\'
settings={}

class sqlite:

    def __init__(self,database="C:\\FORECAST_RAW_DATA\\Forecasts.db"):
        self.database = database
        self.conn = sqlite3.connect( database )
        self.conn.text_factory = str #bugger 8-bit bytestrings
        self.cur = self.conn.cursor()
        self.tables = ('v','p','dir')
        
    def update(self,tbl,date):      
        print 'asd'
            
    def checktable(self,tbl):
        if tbl in self.tables:
            ctag = ColumnArgs(ColumnTags(tbl,721),'FLOAT')
            statement = 'CREATE TABLE IF NOT EXISTS '+ tbl +' (date INTEGER, ' + ctag +')'
            self.cur.execute(statement)
            ct = True
        else:
            print 'Database does not contain the specified table.'
            ct = False
        return ct
        
    def checkdate(self, tbl, date):
        cur = self.cur
        if isinstance(date,int) and (tbl in self.tables):
            statement = "SELECT EXISTS(SELECT 1 FROM "+ tbl+ " WHERE date=" + str(date)+ ")"
            cur.execute(statement)
            if cur.fetchone() is None:
                print("File already updated!")
                cd = True
            
            else:
                print("Updating file...")
                cd = False
        else:
            print("Invalid entry format.")
        return cd
        
        
def ColumnTags(colid,colnum):
    list1 = [colid for _ in range(colnum)]
    list2 = map(str, range(1,colnum+1))
    list3 = [a + b for a, b in zip(list1, list2)]
    return list3
    
def ColumnArgs(coltag,vartype):
    typelist = [vartype for _ in range(len(coltag))]
    arg = [a +' '+ b for a, b in zip(coltag,typelist)]
    colarg = ','.join(arg)
    return colarg
    
# Begin of the program
db = sqlite()

for root, dirs, filenames in os.walk(indir):
    for f in filenames:
        date = [int(s) for s in f.split('-') if s.isdigit()][0]
        parkstr = s.split('.')[0]        
        if parkstr == 'AlegriaI':
            park = 'AL1'
        else:
            park = 'AL2'
        
            
#        conn = sqlite3.connect( "path/to/file.db" )
#        conn.text_factory = str  #bugger 8-bit bytestrings
#        cur = conn.cur()
#        cur.execute('CREATE TABLE IF NOT EXISTS mytable (field2 VARCHAR, field4 VARCHAR)')
#        
#        reader = csv.reader(open(filecsv.txt, "rb"))
#        for field1, field2, field3, field4, field5 in reader:
#          cur.execute('INSERT OR IGNORE INTO mytable (field2, field4) VALUES (?,?)', (field2, field4))