from os.path import exists as file_exists
import argparse
# examen parcial 2021


#1. (1 punto) Crear la clase Film con los datos relativos a una película (título, año, valoración). 
#Tendrá los siguientes métodos: 
#Constructor: dónde recibirá los datos de título, año y valoración.Deberá tener un método para imprimir los datos.
class film:
    def __init__(self,Titulo,Anio,Valoracion):
        self.titulo = Titulo
        self.anio = Anio
        self.valoracion = Valoracion
    def __str__(self) :
        return 'Titulo: '+ self.titulo + 'Año: ' + str(self.anio) + 'valoracion: ' + str(self.valoracion)

#2. (4 puntos) Crear la clase Ranking, que recibirá un fichero con las mejores películas de la historia. 
#La clase tendrá los siguientes métodos:

#Constructor: recibirá el fichero de películas TopFilms.txt (en la sección módulos)

class ranking:
    def __init__(self,path):
        self.path = path

#OrdenarPor: recibirá el tipo de orden (por año o por valoración) y deberá leer el fichero de películas 
# y crear un nuevo fichero 
# llamado TopFilmsBy[TIPO].txt con el listado de películas (una por línea) ordenado por el tipo recibido
#  de menor a mayor. 
    def ordenadoPor(self,tipo):
        #try:
        f  = open(self.path,'r')
        nombreFichero = 'topFilms'+str(tipo)+'.txt'
        if file_exists == False:
            r = open(nombreFichero,'x')
        w = open(nombreFichero,'r+')
        #except:
            #raise Exception('error')
        datos = f.readlines()
        #print(datos)
        f.close()
        val = []
        year = []
        listado =[]
        
        for i in datos:
            lista = i.replace('\n','').split('###')
            listado.append(lista)
            if tipo == 'Anio':
                year.append(lista[1])
            if tipo == 'valoracion':
                val.append(lista[2])
            val.sort()
            year.sort()
        #print(listado)
        aux = 0
        listaOrdenada = []
        
        for x in listado:
            if tipo == 'Anio':
                for r in year:
                    print(x[1] +'|' +r)
                    if x[1] == r:
                        print('engtra')
                        print(x[1] +'|' +r)
                        listaOrdenada.append(x)
                        aux += 1
                    print(aux)
                print(listaOrdenada)
            if tipo == 'valoracion':
                    if x[2] == val[aux]:
                        listaOrdenada.append(x)
                    aux += 1
        '''print(x[1])
        print(year[1])
        print(aux)'''
#Top: recibirá un numero y el tipo de orden que le indicará si debe leer del fichero ordenado por año o el ordenado por valoración, 
# y mostrará por pantalla las n primeras películas del fichero. 

    def top(self,n):
        try:
            archivo = open(self.path)
            listado = archivo.readlines()
            print(listado[:n])
            archivo.close()
        except:
            print('error')
    

#FindFilm: recibirá el título de una película y devolverá un objeto de tipo Film con sus datos, si no existe deberá lanzar un error. 

#3. (1 punto) Añadir al script los argumentos de entrada necesarios para poder al menos ejecutar las opciones de ordenar por tipo y 
# mostrar el top.
'''parser = argparse.ArgumentParser()
parser.add_argument('-f','--file', type =str,required=True,help='fichero sobre el que buscar.',dest='path')
parser.add_argument('-o','--orden',type=str,required=False,help='orden del top.',dest='tipo')
parser.add_argument('-t','--top',type=int,required=False,help='top.',dest='top')'''
#args = parser.parse_args()



pelis = film('intelestelar',2014,8.9)
#print(pelis)
#r1 = ranking(args.path)
r0 = ranking('topFilms.txt')
r0.ordenadoPor('Anio')
#r1.ordenadoPor(args.tipo)