#ORGANIZADOR DE ARQUIVOS

import os
from tkinter.filedialog import askdirectory

way = askdirectory(title="select a folder")
arquive_list = os.listdir(way)
locais = {
    "imagens": [".png", ".jpg"],
    "planilhas": [".xlsx"],
    "pdfs": [".pdf"],
    "words": [".docx"],
}

for arquive in arquive_list:
    nome, extensao = os.path.splitext(f"{way}/{arquive}")
    for folder in locais:
        if extensao in locais[folder]:
            if not os.path.exists(f"{way}/{folder}"):
                os.mkdir(f"{way}/{folder}")
            os.rename(f"{way}/{arquive}", f"{way}/{folder}/{arquive}")
