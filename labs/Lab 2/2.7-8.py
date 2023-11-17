#Test this by running the program and seeing if the CSV file you made stores all
#the traincodes.
#The problem asked for all the properties in the XML file, so we could just repeat
#the append line for each of the properties, this will work, but it makes the code
#long and I am lazy so:
#a. At the top of the program make an array called retrieveTags that will
#store all the names of the tags we want to retrieve.
from xml.dom.minidom import parseString
import requests
import csv 

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)

retrieveTags=['TrainStatus',
            'TrainLatitude',
            'TrainLongitude',
            'TrainCode',
            'TrainDate',
            'PublicMessage',
            'Direction'
            ]

with open('week03_train.csv', mode='w') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()
        dataList = []
        dataList.append(traincode)
        train_writer.writerow(dataList)

