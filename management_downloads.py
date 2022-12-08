import os
from datetime import datetime
import shutil
from pathlib import Path


home = str(Path.home()).replace('C:', '').replace('\\', '/')
dir = home + '/Downloads/'
date = datetime.now().strftime('%d%m%Y-%H%M')
keyExclude = []

def move_files_default(file):
    if os.path.isfile(dir + file): 
        ext = os.path.splitext(dir + file)
        for typeExt in typefiles.keys():
            if ext[1].lower() in typefiles[typeExt]:                
                dirTarget = f'{dir}{typeExt}-{date}/'
                if os.path.isdir(dirTarget):
                    shutil.move(dir + file, dirTarget + file)
                else:
                    os.makedirs(dirTarget)
                    shutil.move(dir + file, dirTarget + file)


def move_files(exce, file):
    if os.path.isfile(dir + file):
        for keyExp in exce.keys():
            for w in exce[keyExp].split():
                if w in file.lower():
                    dirTarget = f'{dir}{keyExp}-{date}/'
                    if os.path.isdir(dirTarget):
                        shutil.move(dir + file, dirTarget + file)
                    else:
                        os.makedirs(dirTarget)
                        shutil.move(dir + file, dirTarget + file)          


typefiles = {'images':['.bmp', '.tiff', '.jpeg', '.gif', '.png', '.eps', '.svg', '.jpg'], 'pdf':['.pdf'], 'compactados':['.rar', '.zip', '.7z'], 'docs-word':['.docx', '.doc'], 'excel': ['.xlsx'], 'powerpoint': ['.pptx'], 'executaveis': ['.exe'], 'texto': ['.txt'], 'codigos/html': ['.html'], 'codigos/java': ['.java'], 'codigos/php': ['.php'], 'codigos/css': ['.css'], 'codigos/python': ['.py'], 'codigos/sql': ['.sql', '.mwb'], 'codigos/json': ['.json'], 'musicas': ['.mp3', '.wav', '.aac'], 'iso': ['.iso']}
exceptions = {}


while str(input('Você pode digitar uma palavra que um lote de arquivos contenha e esses arquivos serão adicionados a uma pasta separada.\nObs: independente da extensão.\nDeseja adicionar? \033[7;37;40m s/n \033[m ')) == 's':
    word = str(input('Digite a palavra: '))
    keyDic = str(input('Digite o nome da pasta desejado: '))
    exceptions[keyDic] = word
    print(exceptions)


for files in os.listdir(dir):
    if os.path.isfile(dir + files) and not 'management_downloads.py' in files:
        if len(exceptions) > 0:
            move_files(exceptions, files)

        move_files_default(files)