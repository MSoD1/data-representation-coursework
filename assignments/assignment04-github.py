import pandas as pd

assignment04 = 'https://github.com/MSoD1/data-representation-coursework/blob/main/assignments/assignment04-csv.py'

# creating a variable and storing the text 
# that we want to search 
search_text = "Andrew"

# creating a variable and storing the text 
# that we want to add 
replace_text = "Megan"

# Opening our text file in read only 
# mode using the open() function 
with open(r'assignment04.csv', 'r') as file: 

	# Reading the content of the file 
	# using the read() function and storing 
	# them in a new variable 
	data = file.read() 

	# Searching and replacing the text 
	# using the replace() function 
	data = data.replace(search_text, replace_text) 

# Opening our text file in write only 
# mode to write the replaced content 
with open(r'assignment04.csv', 'w') as file: 

	# Writing the replaced data in our 
	# text file 
	file.write(data) 

# Error - it's reading the csv file saved not the link
