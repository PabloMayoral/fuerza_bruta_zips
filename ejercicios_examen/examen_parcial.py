# examen parcial 2021


#1. (1 punto) Crear la clase Film con los datos relativos a una película (título, año, valoración). 
#Tendrá los siguientes métodos: 
#Constructor: dónde recibirá los datos de título, año y valoración.Deberá tener un método para imprimir los datos.

#2. (4 puntos) Crear la clase Ranking, que recibirá un fichero con las mejores películas de la historia. 
#La clase tendrá los siguientes métodos:

#Constructor: recibirá el fichero de películas TopFilms.txt (en la sección módulos)

#OrdenarPor: recibirá el tipo de orden (por año o por valoración) y deberá leer el fichero de películas y crear un nuevo fichero 
# llamado TopFilmsBy[TIPO].txt con el listado de películas (una por línea) ordenado por el tipo recibido de menor a mayor. 

#Top: recibirá un numero y el tipo de orden que le indicará si debe leer del fichero ordenado por año o el ordenado por valoración, 
# y mostrará por pantalla las n primeras películas del fichero. 

#FindFilm: recibirá el título de una película y devolverá un objeto de tipo Film con sus datos, si no existe deberá lanzar un error. 

#3. (1 punto) Añadir al script los argumentos de entrada necesarios para poder al menos ejecutar las opciones de ordenar por tipo y 
# mostrar el top.

 
import argparse

class classFilm:
    def __init__ (self, titulo, año, valoracion):
        self.titulo = titulo
        self.año = año
        self.valoracion = valoracion
    def __str__ (self):
        return "Titulo -> "+self.titulo + "Año -> "+str(self.año)+"Valoracion -> "+str(self.valoracion)

class classRanking():
    def __init__ (self, fichero):
        self.fichero = fichero
        
    def funOrdenarPor (self, orden):
        if orden == "Año":
            try:
                fichero_peliculas = open (self.fichero, "r", encoding="UTF-8")
                contenido_fichero_lista = fichero_peliculas.readlines()
                lista_peliculas=[]
                
                for elemento in contenido_fichero_lista:
                    linea_fichero_split=elemento.split("##")
                    a=linea_fichero_split[2].replace("/n","")
                    peli = [linea_fichero_split[0], linea_fichero_split[1], a]
                    lista_peliculas.append(peli)
                    
     
                fichero_orden_año = open("TopFilmsByAño.txt", "w", encoding="UTF-8")
                lista_peliculas_ordenada=sorted(lista_peliculas, key = lambda x:(x[1]))
                for linea in lista_peliculas_ordenada:
                    fichero_orden_año.write(str(linea[0])+"##"+str(linea[1]+"##"+str(linea[2])+"\n"))
            except:
                raise Exception ("Error al leer en el fichero")
        
        elif orden == "Valoracion":
            try:
                fichero_peliculas = open (self.fichero, "r", encoding="UTF-8")
                contenido_fichero_lista = fichero_peliculas.readlines()
                lista_peliculas=[]
                for elemento in contenido_fichero_lista:
                    linea_fichero_split=elemento.split("##")
                    a=linea_fichero_split[2].replace("\n","")
                    peli = [linea_fichero_split[0], linea_fichero_split[1], a]
                    lista_peliculas.append(peli)
                fichero_orden_año = open("TopFilmsByValoracion.txt", "w", encoding="UTF-8")
                lista_peliculas_ordenada=sorted(lista_peliculas, key = lambda x:(x[2]))
                for linea in lista_peliculas_ordenada:
                    fichero_orden_año.write(str(linea[0])+"##"+str(linea[1]+"##"+str(linea[2]))+"\n")
                   
            except:
                raise Exception ("Error al leer en el fichero")
    
        else:
            print("Orden no valida")

    def funTop (self, numero, orden):
        if orden == "Año":
            fichero = open("TopFilmsByAño.txt", "r")
            c=fichero.readlines()[0:numero]
            for x in c:
                print(x)
        elif orden == "Valoracion":
            fichero = open("TopFilmsByValoracion.txt", "r")
            c=fichero.readlines()[0:numero]
            for x in c:
                print(x)
        else:
            print("Orden no valida")

    def funFindFilm (self, titulo):
        fichero = open("TopFilms.txt", "r")
        fichero_lista=fichero.readlines()
        for elemento in fichero_lista:
            fichero_split = elemento.split("##")
        posicion_linea=0
        oclassFilm=classFilm(fichero_split[0], fichero_split[1], fichero_split[2])
        
        if titulo == fichero_split[0]:
                print(oclassFilm)
      
'''
o1=classRanking("TopFilms.txt")
o1.funOrdenarPor("Año")
o1.funOrdenarPor("Valoracion")
o1.funTop(4,"Año")
print("\nThen\n")
o1.funTop(3, "Valoracion")
print("\nFindFilm\n")
o1.funFindFilm("Pulp Fiction")'''

