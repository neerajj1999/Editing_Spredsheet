
import pandas as pd

#reading the file and sheet name
wb = pd.read_excel('RegData.xlsx', sheet_name='Call Detail')

#deleting the sno coloumn in spreadsheet
del wb['SNO']
#changing the  value with another value
# wb.PINCODE = wb.PINCODE.replace({"": "-"})
wb.STATUS = wb.STATUS.replace({"INVALID":"-", "VALID":"IVR"})
wb.Duration = wb.Duration.add(2)

#saving the file at specific location with a new name
wb.to_excel(r'F:\New folder\mobile.xlsx', index=False)



