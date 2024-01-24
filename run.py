# This Windows Python program automatically opens the Excel (actually .csv) file that's 
#	in the program's directory, and finds the min and max pH and flow values.

import pandas # To read the Excel file
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
	print(the_spreadsheet)
	

	# The spreadsheet that was pasted in will now be deleted unless the user objects.
	input_var = input("\nProgram done. Press ENTER to quit or type \"N\" to quit while keeping the spreadsheet file saved.\n")
	if ( input_var != "N" ) and ( input_var != "n" ):
		os.system("del " + the_spreadsheet)
else:
	exit("Incorrect number of spreadsheets found (" + str(len(spreadsheets_found))+" instead of 1).")
