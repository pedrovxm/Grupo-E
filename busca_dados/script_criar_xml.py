
import pandas as pd
import xml.etree.ElementTree as xml

import os

## directory = nome da pasta

def open_directory(directory):

    ## verifica a existência do diretório, se existir, cria o caminho a partir da pasta onde está

    if os.path.isdir(directory):

        return os.getcwd() + '/' + directory

    else:

        return "Directory not found"



def GenerateXML(df, root,filename):

    root = xml.Element(root)

    tags = df.columns

    for raws in df.iterrows():


        raw = xml.SubElement(root, "raw")

        i = 0
        print(len(raws[1]))
        print(raws[1].iloc[2])

        for columns in tags:

            subElement = xml.SubElement(raw, columns, name = columns)
            subElement.text = str(raws[1].iloc[i])

            i = i +1

    tree = xml.ElementTree(root)

    with open(filename, "wb") as file:
        tree.write(file)

df = pd.read_csv("sao_paulo.csv")

GenerateXML(df,"tag", "dataframe.xml")