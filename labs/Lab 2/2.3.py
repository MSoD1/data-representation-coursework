# Once you are happy this works, comment out the print statement

from xml.dom.minidom import parseString
import requests
import csv 


url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)
# check it works
#print (doc.toprettyxml()) #output to console comment this out once you know it works

# if I want to store the xml in a file. You can comment this out later
with open("trainxml.xml","w") as xmlfp:
    doc.writexml(xmlfp)
