import xml.etree.ElementTree as ET
def set(name):
    tree = ET.parse(name)
    root = tree.getroot()

    for child in root:
        print(child.tag, ':  ', child.attrib)
        for subchild in child:
            print(subchild.tag, ':  ', subchild.text)
