from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def Download(nome_arquivo): 

    gauth = GoogleAuth()
    gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
    drive = GoogleDrive(gauth)
    arquivo = "'"+nome_arquivo+"'"
    files = drive.ListFile({'q': "title:" + arquivo}).GetList()
    for item in files:
        print('%s Downloaded' % (item['title']))
        download_mimetype = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        item.GetContentFile(item['title']+"_COPIA", mimetype = download_mimetype)
    

def Metadados_arquivos(nome_pasta):

    gauth = GoogleAuth()
    gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
    drive = GoogleDrive(gauth)
    arquivo = "'"+nome_pasta+"'"
    files = drive.ListFile({'q': "title:" + arquivo}).GetList()

    for file in files:
        parent_id = "'"+file['id']+"'"
        
    children = drive.ListFile({'q':  parent_id +" in parents"}).GetList()
    
    Metadados_Geral = []

    for child in children:
        print(child)
        print("\n\n")
        child_atributo = [child['title'], child['title']]
        Metadados_Geral.append(child_atributo)
    print(Metadados_Geral)

Metadados_arquivos("Arquivos CDA")
#Download("FORMULARIO RESPUESTAS")




       
      

