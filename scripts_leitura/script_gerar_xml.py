import os
import xml.etree.ElementTree as xml


def gerar_xml(dir_name):
    root = xml.Element('root')

    for file in os.listdir(dir_name):
        filepath = os.path.join(dir_name, file)
        f = open(filepath, 'r')
        xml.SubElement(root, 'file', id=file).text = f.read()
        f.close()
        tree = xml.ElementTree(root)
        tree.write('data.xml',  encoding='UTF-8', xml_declaration=True)
