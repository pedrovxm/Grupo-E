import os

def contar_arquivos(dir_name):

    filenames = os.listdir(dir_name)

    return len(filenames)