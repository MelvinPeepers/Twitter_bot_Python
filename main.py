import gspread

gc = gspread.service_account('credentials.json')

# Open a sheet from a spreadsheet in one go
wks = gc.open("covid-tips").sheet1

# Update a range of cells using the top left corner address

next_tweet = wks.acell('A2').value


# post tweet through twitter API


# delete row from Sheet on success
wks.delete_rows(2)