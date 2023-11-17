#Comment out the print and modify the program so that it prints out the latitudes
#uncomment the print row 17 to see
# Same code as before but Train Codes are replaced to find that Latitude

from xml.dom.minidom import parseString
import requests
import csv 

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)

objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionsNode in objTrainPositionsNodes:
    trainclatnode = objTrainPositionsNode.getElementsByTagName("TrainLatitude").item(0)
    trainlat = trainclatnode.firstChild.nodeValue.strip()
    #print (trainlat)
