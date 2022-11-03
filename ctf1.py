from zipfile import ZipFile
num = 2000
with ZipFile(""+str(num) +'.zip', 'r') as obj_zip:
    FileNames = obj_zip.namelist()
    for nombreFicheros in FileNames:
        if nombreFicheros.endswith('.zip'):
            obj_zip.extract(nombreFicheros, 'temp_txt')
    num -=1
for vueltas in range(0,2000):
    with ZipFile("temp_txt/"+str(num) +'.zip', 'r') as obj_zip:
        FileNames = obj_zip.namelist()
        for nombreFicheros in FileNames:
            if nombreFicheros.endswith('.zip') or nombreFicheros.endswith('.txt'):
                obj_zip.extract(nombreFicheros, 'temp_txt')
                
    num -=1