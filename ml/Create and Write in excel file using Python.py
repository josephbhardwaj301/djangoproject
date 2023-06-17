import xlwt
from xlwt import Workbook

wb=Workbook() #Workbook is crated
sheet1=wb.add_sheet('Sheet 1') #add_sheet is used to create a sheet
sheet1.write(1,0,'BNB VARANASI')
sheet1.write(2,0,'BNB VARANASI')
sheet1.write(3,0,'BNB VARANASI')
sheet1.write(4,0,'BNB VARANASI')
wb.save('xlwt example.xls')