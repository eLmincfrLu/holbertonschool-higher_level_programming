#!/usr/bin/python3
"""ghjk"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")

    for key, value in dictionary.items():
        item = ET.SubElement(root, "item")

        key_element = ET.SubElement(item, "key")
        key_element.text = str(key)

        value_element = ET.SubElement(item, "value")
        value_element.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}

    for item in root.findall("item"):
        key = item.find("key").text
        value = item.find("value").text

        if value.isdigit():
            value = int(value)

        result[key] = value

    return result
