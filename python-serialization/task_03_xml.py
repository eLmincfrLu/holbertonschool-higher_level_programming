#!/usr/bin/python3
"""fvbnm"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """fghj"""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding="utf-8", xml_declaration=True)
    except Exception:
        return False


def deserialize_from_xml(filename):
    """dfghjm"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        deserialized_dict = {}
        for child in root:
            deserialized_dict[child.tag] = child.text

        return deserialized_dict
    except FileNotFoundError:
        return None
    except Exception:
        return None