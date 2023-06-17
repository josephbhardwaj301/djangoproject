import pandas as pd
import openpyxl
df=pd.DataFrame([[11,21,31],[12,22,32],[31,32,33]],index=['Physics','Chemistry','Maths'],columns=['Sudhanshu','Kuldeep','Adarsh'])
print(df)
df.to_excel('pandas_to_excel.xlsx',sheet_name='new_sheet_name')
