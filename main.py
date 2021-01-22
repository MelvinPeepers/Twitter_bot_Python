import gspread

gc = gspread.service_account('credentials.json')

# Open a sheet from a spreadsheet in one go
wks = gc.open("covid-tips").sheet1

# Update a range of cells using the top left corner address
wks.update('A1', [[2, 3], [4, 5]])
