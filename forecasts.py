# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 17:53:22 2014

@author: Eolica
"""
import csv, sqlite3, os

# Begin of the program

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
    
def DropTables(conn,tbls,park):
    database="C:\\Database\\" + park + ".db"
    conn = sqlite3.connect( database )
    conn.text_factory = str #bugger 8-bit bytestrings
    cur = conn.cursor()
    for tbl in tbls:
        try:
            cur.execute("DROP TABLE "+tbl)
        except ValueError:
            print "Table "+tbl+" does not exist in the databse!"

def forecastupdate(files):
    tables = ('de','ate','p','v','dir')
    included_cols = [2,3,5,6,7]
        
    for f in files:
        full_f_path =  os.path.join(raw_data_folder,f)
        date = [int(s) for s in f.split('-') if s.isdigit()][0]
        parkstr = s.split('.')[0]      
        
        if parkstr == 'AlegriaI':
            park = 'AL1'
        else:
            park = 'AL2'
        
        # Defining db file location, initializing connection and cursor
        database="C:\\Database\\" + park + ".db"
        conn = sqlite3.connect( database )
        conn.text_factory = str #bugger 8-bit bytestrings
        cur = conn.cursor()
        
        for tbl in tables:
            # Initializing variables
            if tbl in ['de','ate']:
                ctag = ColumnArgs(ColumnTags(tbl,721),'TEXT')
            else:
                ctag = ColumnArgs(ColumnTags(tbl,721),'FLOAT')
            interrog = ','.join(['?' for _ in range(721+1)])
            ctine = 'CREATE TABLE IF NOT EXISTS '+ tbl +' (date INTEGER, ' + ctag +')'
            cur.execute(ctine)
            
            # Checking if date has been already updated to db, if not updates file
            #se= "SELECT EXISTS(SELECT 1 FROM "+ tbl+ " WHERE date = ?)"
            se= "SELECT rowid FROM "+ tbl+ " WHERE date =" + str(date)
            cur.execute(se)
            data = cur.fetchone()
            
            if data is None:
                
                # Only reads file once (when working with the first table)
                # and stores all the necessary data in the xxx variable
                if tbl == tables[0]:
                    # Reading csv file
                    csvfile = open(full_f_path, "rb")
                    reader = csv.reader(csvfile)
                    
                    # Skipping header lines
                    next(reader,None)
                    next(reader,None)
                    
                    # Retrieving useful columns and writing to sqlite
                    rawlist = []
                    for row in reader:
                        rowlist = row[0].split(';')
                        selected_cols = list(rowlist[i] for i in included_cols)
                        rawlist.append(selected_cols)
                    
                    # Closing csv file
                    csvfile.close()
                    
                    # Transposing data (lines in the csv are columns in the db)
                    transposed_rawlist = zip(*rawlist)
                    
                # Extracting correct column to be updated
                aux_list_col = list(transposed_rawlist[tables.index(tbl)])
                toupdate = [date]+aux_list_col
                
                # Writing files
                insert = "INSERT INTO "+tbl+" VALUES ("+interrog+")"
                cur.execute(insert,tuple(toupdate))                
                
                # Commiting inserts
                conn.commit()
                
            else:
                print "File already updated."

####### Begginin of the update process ########

# Raw data location
raw_data_folder = "C:\\FORECAST_RAW_DATA\\"

# Retrieving file names        
for root, dirs, filenames in os.walk(raw_data_folder):
    
    # Separated into 2 sets so same connection is used throughout update
    al1files = filter(lambda x: 'AlegriaI' in x, filenames)
    al2files = filter(lambda x: 'Alegria II' in x, filenames)
    
    # Updating sqlite db
    forecastupdate(al1files)
    forecastupdate(al2files)
    
    
        

        