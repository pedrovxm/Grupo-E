import xml.etree.ElementTree as xml
import pandas as pd
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def Download(nome_arquivo): 

    gauth = GoogleAuth()
    gauth.LocalWebserverAuth() #client_secrets.json need to be in the same directory as the script
    drive = GoogleDrive(gauth)
    arquivo = "'"+nome_arquivo+"'"
    files = drive.ListFile({'q': "title:" + arquivo}).GetList()
    for item in files:
        print('%s Downloaded' % (item['title']))
        download_mimetype = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        item.GetContentFile(item['title']+"_COPIA.xlsx", mimetype = download_mimetype)

def Metadados_arquivos(nome_pasta):

    gauth = GoogleAuth()
    gauth.LocalWebserverAuth() #client_secrets.json need to be in the same directory as the script
    drive = GoogleDrive(gauth)
    arquivo = "'"+nome_pasta+"'"
    files = drive.ListFile({'q': "title:" + arquivo}).GetList()

    for file in files:
        parent_id = "'"+file['id']+"'"
        
    children = drive.ListFile({'q':  parent_id +" in parents"}).GetList()
    
    root = xml.Element('Files')

    for child in children:
        print('sadf\n')
        root = xml.Element('Files')
        file = xml.SubElement(root, "URL", name= child['downloadUrl'] )
        xml.SubElement(file, 'name', name= 'name').text = child['title']
        xml.SubElement(file, 'type', name= 'name').text = child['mimeType']
        xml.SubElement(file, 'modified', name= 'name').text = child['createdDate']
        xml.SubElement(file, 'creator', name= 'name').text = child['ownerNames'][0][0]      
    tree = xml.ElementTree(root)
    with open("metadados_drive.xml", "wb") as file:
        tree.write(file)
        
        
        
        
    #     print(child)
    #     print("\n\n")
    #     child_atributo = [child['title'], child['title']]
    #     Metadados_Geral.append(child_atributo)
    # print(Metadados_Geral)

Metadados_arquivos("Arquivos CDA")
#Download("FORMULARIO RESPUESTAS")




       
      

