import xml.etree.ElementTree as ET
import requests

arquivo = "curriculo.xml"
tree = ET.parse(arquivo)
root = tree.getroot()
filtro = "*"

for child in root.iter(filtro):
    print(child.attrib)
    for subchild in child.iter(filtro):
        print(subchild.attrib)
