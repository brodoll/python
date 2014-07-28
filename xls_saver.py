import os, xlwt, xlrd

path = 'C:\\Annual_SCADA_Data\\'
outputfolder = 'C:\\Test\\Cami\\'
list_of_files = {}
for (dirpath, dirnames, filenames) in os.walk(path):
    for filename in filenames:
        if filename[-4:] == '.xls':
            #print filename
            if filename[0:3] == 'AL1' or filename[0:3] == 'AL2':
                list_of_files[filename] = os.sep.join([dirpath, filename])

                
                workbook = xlrd.open_workbook(os.sep.join([dirpath,filename]))
                sheet = workbook.sheet_by_index(0)
                
                for row in range(sheet.nrows): # or max_tag_row_index + 1
                    for col in range(sheet.ncols):
                        data = [sheet.cell_value(row, col)] 
                #data = [sheet.cell_value(0, col) for col in range(sheet.ncols)]
                        
                print data
                print '---------------------------------------------------------'

#                workbook = xlwt.Workbook()
#                sheet = workbook.add_sheet('Plan1')
#
#                for index, value in enumerate(data):
#                    sheet.write(0, index, value)
#
#                workbook.save(os.sep.join([outputfolder,filename]))
#                print filename + ' transcribed.'


#for file in list_of_files:
#    print file
