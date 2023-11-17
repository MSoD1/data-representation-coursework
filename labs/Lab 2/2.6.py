#Ok. Let’s now store this one property into a CSV:
#a. Before the for loop open the CSV file, I am using with, so make sure that
#you indent the for loop so that it is in the with block.

#This fails to load the data into a csv since the url is an xml file
# an empty csv is created
from xml.dom.minidom import parseString
import requests
import csv 

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)

with open('week03_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()
