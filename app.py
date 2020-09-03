import requests

xml = "https://www.boi.org.il/currency.xml"
r = requests.get(xml)

print(r.text)
