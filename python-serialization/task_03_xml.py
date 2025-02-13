#!/usr/bin/python3
""""Serialize and Deserialize with XML"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionnary, filename):
    """Serialize a Python dictionnary to XML"""
    try:
        root = ET.Element("data")
        for key, value in dictionnary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
    except Exception as e:
        print(f"Error: {e}")


def deserialize_from_xml(filename):
    """Deseralize XML to a Python dictionnary"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        dictionnary = {child.tag: child.text for child in root}

        return dictionnary

    except FileNotFoundError:
        print("Error: the file {} was not found".format(filename))
        return None
    except ET.ParseError as e:
        print("Error: {} can't parsing to XML".format(e))
        return None
