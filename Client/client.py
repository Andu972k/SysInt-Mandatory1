from lxml import etree
import requests
import time


while True:

    data = etree.Element("Data")
    number = etree.SubElement(data, "Number", type="int")
    number.text = "100"


    contentType = 'xml'
    numberAsXML = '<?xml version="1.0" encoding="UTF-8"?>\n<Data>\n<Number type="int">10</Number></Data>'
    numberAsJSON = '{"number": 20}'
    r = requests.post("http://127.0.0.1:3333/server1/calculate", headers={"Content-Type": f"text/{contentType}"}, data=etree.tostring(data))
    print(r.text)
    time.sleep(3)