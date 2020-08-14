import os

## directory = nome da pasta 

def open_directory(directory):

    ## verifica a existência do diretório, se existir, cria o caminho a partir da pasta onde está

    if os.path.isdir(directory):

        return os.getcwd() + '/' + directory

    else:

        return "Directory not found"



