from os.path import exists as file_exists
class rutas:
    #poner en el metodo de crear un os.iffileexist
    def __init__(self,path):
        self.path = path
    def createFile(self):
        if file_exists(self.path) == False:
            f = open(self.path,'x+')
            f.close()
        else:
            print('El fichero ya existe')
    def modificarFichero(self,texto):
        f = open(self.path,'w+')
        f.write(texto)
        f.close()
    def visualizarFichero(self):
        f = open(self.path,'r')
        print(f.readlines())
        f.seek(0)
        f.close()
    def buscaPalabra(self,palabra):
        contador = 0
        f = open(self.path,'r+')
        listado = f.readlines()
        
        for x in listado:
            separacion = x.split()
            for i in separacion:
                if i == palabra:
                    contador += 1
        print(contador)
        f.close()
r0 = rutas('ejercicios_rutas.txt')
r0.createFile()
r0.modificarFichero('llamado texto prueba\nllamado ejercicios_rutas.txt')
r0.visualizarFichero()
r0.buscaPalabra('llamado')