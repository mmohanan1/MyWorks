import csv
import os
import gspread

#Login credentials
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('Mah-Sheets-Cred.json', scope)
gc = gspread.authorize(credentials)

#Remove existing output csv files
os.remove("Mahesh_Merge_1.csv")
os.remove("Mahesh_Merge_2.csv")

# List all the file names to be processed
Total_Sheets=['Mahesh_1','Mahesh_2']

#run the loop for all existing files one by one
for sheet in Total_Sheets:
	print sheet
	wks_1 = gc.open(sheet).worksheet("Sheet1").get_all_values()
	wks_2 = gc.open(sheet).worksheet("Sheet2").get_all_values()
	
	i=0
	list=[]
	# Remove Null records in Sheet 1
	for i in range (0,len(wks_1)):
	    list.append(filter(None,wks_1[i])) #recreate list after removing null records
	    wks_sheet1 = [x for x in list if x != []] #remove null lists
	
	#Load the not null records into output csv file
	with open("Mahesh_Merge_1.csv", "a") as f:
		writer = csv.writer(f)
		writer.writerows(wks_sheet1)
	
	j=0
	list2=[]

	# Remove Null records in Sheet 1
	for j in range (0,len(wks_2)):
	    list2.append(filter(None,wks_2[j])) #recreate list after removing null records
	    wks_sheet2 = [x for x in list2 if x != []] #remove null lists
	
	#Load the not null records into output csv file
	with open("Mahesh_Merge_2.csv", "a") as g:
		writer = csv.writer(g)
		writer.writerows(wks_sheet2)
	
