# This Windows Python program automatically opens the Excel (actually .csv) file that's 
#	in the program's directory, and finds the min and max pH and flow values.
#	To test the program, copy the "sample-spreadsheet-file.csv" file into the main folder.

import csv # To read the Excel file
from pathlib import Path  # To find the Excel file in the current directory
import os # To open File Explorer

# Tell the user what to do
unused_var = input("\n\n\nPlease place a copy of the Excel file into the folder that pops up.")

# Open File Explorer so that user can either paste in a copy of the Excel file, or the user
#	can copy the path of it with Ctrl+L so that they can easily save the file to the 
#	correct place with another program (i.e. Microsoft Outlook, when saving an email
#	attachment).
os.system("start.")

# Pause so the user has time to paste in the Excel file.
unused_var = input("\nPress ENTER when done.\n")

# Get list of files in current directory
files = [file.name for file in Path.cwd().rglob('*')]

# The final file in this list should be the sample file (which is inside another directory
#	and should be excluded). Let's make sure it's there, then exclude it from the list
#	so the program doesn't read it (it's only there to let the user know what kind of 
#	wastewater controller file format this program can process).
if files[-1] == "sample-spreadsheet-file.csv":
	# print("sample file found.")
	files = files[:-1]
else:
	exit("Error: Sample file (\"Sample\\sample-spreadsheet-file\") was not found.\n")

# Find the name of the spreadsheet file(s). Hopefully only 1 is found.
spreadsheets_found = []	
for current_file in files:
	if current_file[-4:] == ".csv":
		spreadsheets_found = spreadsheets_found + [current_file]
if len(spreadsheets_found) == 1:
	# operations on the spreadsheet will now be done
	the_spreadsheet = spreadsheets_found[0]
	print("Now operating on: ",the_spreadsheet)
	
	# move the csv contents into the "data" list
	import csv
	with open(the_spreadsheet, newline='') as csvfile:
		data = list(csv.reader(csvfile))
	
	# initiate 4 different lists with the following 4 properties:
	date_list = []
	pH_list = []
	flow_list = []
	total_flow_list = []

	# move the "data" contents into those 4 lists (as VALUES and not strings), and remove space characters
	for row in range(4,len(data)):
		# print(data[row])
		date_list = date_list+[data[row][0].replace(" "," ")] #The date string shouldn't actually have its spaces deleted		
		pH_list = pH_list + [eval(data[row][1].replace(" ",""))]
		flow_list = flow_list + [eval(data[row][2].replace(" ",""))]
		total_flow_list = total_flow_list + [eval(data[row][3].replace(" ",""))]
	# print(ph_list)
	
	# Initiate the min and max placeholder values in the pH, flow, and total_flow lists
	pH = [pH_list[0],pH_list[0]] # note that we will make this list, pH[] = [minimum pH , maximum pH]
	pH_indices = [0,0] # these are the indices that the min and max occurred at
	flow = [flow_list[0],flow_list[0]]
	flow_indices = [0,0]
	total_flow = [total_flow_list[0],total_flow_list[0]]
	total_flow_indices = [0,0]

	# Now actually find those true min and max values
	for index in range(0,len(date_list)):
		if pH_list[index] < pH[0]:
			pH[0] = pH_list[index]
			pH_indices[0] = index
		if pH_list[index] > pH[1]:
			pH[1] = pH_list[index]
			pH_indices[1] = index
		if flow_list[index] < flow[0]:
			flow[0] = flow_list[index]
			flow_indices[0] = index
		if flow_list[index] > flow[1]:
			flow[1] = flow_list[index]
			flow_indices[1] = index
		if total_flow_list[index] < total_flow[0]:
			total_flow[0] = total_flow_list[index]
			total_flow_indices[0] = index
		if total_flow_list[index] > total_flow[1]:
			total_flow[1] = total_flow_list[index]
			total_flow_indices[1] = index

	# Show results
	print("\nRESULTS_____________________\n")
	print("Minimum pH is ",pH[0]," at ",date_list[pH_indices[0]])
	print("Maximum pH is ",pH[1]," at ",date_list[pH_indices[1]])

	print("Minimum flow is ",flow[0]," at ",date_list[flow_indices[0]])
	print("Maximum flow is ",flow[1]," at ",date_list[flow_indices[1]])

	print("Minimum total flow is ",total_flow[0]," at ",date_list[total_flow_indices[0]])
	print("Maximum total flow is ",total_flow[1]," at ",date_list[total_flow_indices[1]])


	# The spreadsheet that was pasted in will now be deleted unless the user objects.
	input_var = input("\nProgram done. Press ENTER to quit or type \"N\" to quit while keeping the spreadsheet file saved.\n")
	if ( input_var != "N" ) and ( input_var != "n" ):
		os.system("del " + the_spreadsheet)
else:
	exit("Incorrect number of spreadsheets found (" + str(len(spreadsheets_found))+" instead of 1).")
