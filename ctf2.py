import zipfile
from tqdm import tqdm

wordlist = 'passwords-UFV-CTF.txt'
zip_location = '2000.zip'

zip_file = zipfile.ZipFile(zip_location)
nPass = len(list(open(wordlist,'r')))
print('Numero de password totales a verificar: ' ,nPass)

with open(wordlist,'r') as wordlist:
    for word in tqdm(wordlist,total=nPass,unit='word'):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print('Password encontrada: ',word.decode().strip())
            exit()
