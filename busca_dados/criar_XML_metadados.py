import xml.etree.ElementTree as xml
import pandas as pd

def generate_xml(arquivo):

    df = pd.read_excel(arquivo)
    root = xml.Element('Files')
    i = 0
    for row in df.iterrows():
        i += 1
        file = xml.SubElement(root, "ID_Arquivo", name=str(i))

        identificador = xml.SubElement(file, "Identifidores")
        xml.SubElement(identificador, 'Nome_Original', name='Nome_Original_Drive').text = str(row[1].iloc[1])
        xml.SubElement(identificador, 'Descricao', name='Descricao').text = str(row[1].iloc[2])
        xml.SubElement(identificador, 'Ultima_modificacao', name='Ultima_data_de_modificacao').text = str(row[1].iloc[3])
        xml.SubElement(identificador, 'Link', name='Link_Arquivo_Drive').text = str(row[1].iloc[13])
        #tag do novo nome do arquivo
        #xml.SubElement(identificador, 'Novo_nome', name='Novo_Nome').text =

        info_pesq = xml.SubElement(file, 'Informacoes_Pesquisa')
        xml.SubElement(info_pesq, 'Eixo', name="Eixo").text = eixo[str(row[1].iloc[6])]
        xml.SubElement(info_pesq, 'Finalidade', name='Finalidade').text = str(row[1].iloc[11])
        xml.SubElement(info_pesq, 'Local', name='Local da coleta').text = str(row[1].iloc[4])
        xml.SubElement(info_pesq, 'Fonte', name='Fonte').text = str(row[1].iloc[8])

        info_tec = xml.SubElement(file, "Informacoes_Tecnicas")
        xml.SubElement(info_tec, "Extracao", name="Tecnica_de_Extracao").text = str(row[1].iloc[10])
        xml.SubElement(info_tec, "Dado", name="Dado_Estruturado").text = str(row[1].iloc[9])
        #tag para inserir a extensao do arquivo
        #xml.SubElement(info_tec, "Extensao", name="Extensao_do_Arquivo").text =

    tree = xml.ElementTree(root)

    with open("metadados.xml", "wb") as file:
        tree.write(file)

file = "FORMULARIO RESPUESTAS.xlsx"
generate_xml(file)