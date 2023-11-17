#Modify the program to print out each of the trainscodes. I.e. find the listings and
#iterate through them to print each traincode out. Check it works

from xml.dom.minidom import parseString
import requests
import csv 

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)
#objTrainPositions is the first grouping
objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionsNode in objTrainPositionsNodes:
    traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
    # Finds TrainCode within the group and excludes everything else but the value between that node
    traincode = traincodenode.firstChild.nodeValue.strip()
    print (traincode)
