import os

def identificar_extensoes(dir_name):

    filenames = os.listdir(dir_name)
    extn_names = []
    for file in filenames:
        name, extension = os.path.splitext(file)
        if extension not in extn_names:
            extn_names.append(extension)

    return extn_names