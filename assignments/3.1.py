<!-- 
Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json".
Upload this program to the same repository you used for the XML assignment
Save this assignment as "assignment03-cso.py"
This program should not be a long one
I don't need you to reformat or analyse the data in any way
It should be about 10ish lines long (I have not counted)
You will need to find the dataset in CSO.ie, try economic and then finance, then finance indicators. yes it is difficult to find, that is part of the task, actually the easiest way to find it is search for it.
...>
import requests
req = requests.get("https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/CSV/1.0/")
url_content = req.content
csv_file = open('cso.json.csv', 'wb')
csv_file.write(url_content)
csv_file.close()
