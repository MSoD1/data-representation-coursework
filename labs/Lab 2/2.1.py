#. Go to the URL and check that it works, have a quick look at the format of the
XML.#
import requests
page = requests.get("http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML")
print(page)
print("-------------------")
print(page.content)
