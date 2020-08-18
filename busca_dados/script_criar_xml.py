import pandas as pd
import xml.etree.ElementTree as xml

import os

def open_directory(directory):

    ## verifica a existência do diretório, se existir, cria o caminho a partir da pasta onde está

    if os.path.isdir(directory):

        return os.getcwd() + '/' + directory

    else:

        return "Directory not found"


def get_all_files(dir_name):
    folder_content = os.listdir(dir_name)
    all_files = list()
    for entry in folder_content:
        entry_path = os.path.join(dir_name, entry)
        if os.path.isdir(entry_path):
            all_files = all_files + get_all_files(entry_path)
        else:
            all_files.append(entry_path)
    return all_files

def identify_extension(file):

    return  os.path.splitext(file)[-1].lower()


def createXML(df,root,file):

    file = xml.SubElement(root, file)

    tags = df.columns

    for raws in df.iterrows():


        raw = xml.SubElement(file, "raw")

        i = 0

        for columns in tags:

            subElement = xml.SubElement(raw, columns, name = columns)
            subElement.text = str(raws[1].iloc[i])

            i = i +1

    return  root

def generate_allXML(path):

    list_files = get_all_files(path)
    root = xml.Element('file_csv')

    for file in list_files:

        if identify_extension(file) == ".csv":

            df = pd.read_csv(file)
            root = createXML(df,root,file.split('/')[-1])


    tree = xml.ElementTree(root)

    with open("dataframe.xml", "wb") as file:
        tree.write(file)



dir_name = open_directory("git_hub/dados/dados_squad_9")
generate_allXML(dir_name)


