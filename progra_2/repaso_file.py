from audioop import reverse
from logging import raiseExceptions
from turtle import pos
from typing import List

'''
datos = {'nombre':'Pablo','edad':21,'aficiones':['aficion1','aficion2']}
for x in datos.values():
    if type(x)==str:
        x.upper()
        #print(x)
    print(type(x),x)

nombre = 'Pablo'
edad = 21
aficiones = ['aficion1','aficion2']

print(type(nombre),nombre,type(edad),edad,type(aficiones),aficiones)
print(nombre.upper())
print(nombre.capitalize())
new_nombre = ''
for x in nombre.lower():
    if x != 'a':
        new_nombre += x
    else:
        new_nombre += '4'
print(new_nombre)

print('El alumno '+ nombre + ' tiene '+str(edad)+' años')

for y in nombre:
    print(y)

if edad < 18:
    print('menor de 18 años')
elif edad >18 and edad < 30:
    print('la edad esta entre los 18 y los 30 años')
else:
    print('edad mayor de 30 años')

diccionario = {}
diccionario['nombres'] = ['pablo','alvaro','luis']
diccionario['edades']= [21,19,17]
diccionario['aficiones']=['aficiones1','aficiones2','aficiones3']

for w in diccionario['edades']:
    if type(w) == int:
            if w < 18:
                print('menor de 18 años')
            elif w >18 and w < 30:
                print('la edad esta entre los 18 y los 30 años')
            else:
                print('edad mayor de 30 años')

def muestraDict(dicc):
    for w in dicc['edades']:
        if type(w) == int:
            if w < 18:
                print('menor de 18 años')
            elif w >18 and w < 30:
                print('la edad esta entre los 18 y los 30 años')
            else:
                print('edad mayor de 30 años')
muestraDict(diccionario)

def getEdad(dic):
    print(dic.get('edades'))
def getNombre(dic):
    print(dic.get('nombres'))
def getAficiones(dic):
    print(dic.get('aficiones'))
getEdad(diccionario)
getNombre(diccionario)
getAficiones(diccionario)'''

'''EJERCICIO 12'''

class crud:
    def __init__(self,Colecciones):
        self.colecciones = Colecciones
        if type(self.colecciones) == list:
            #esto es como si fuera booleano, el valor que tendra es True
            self.esLista = type(self.colecciones) == list       
        else:
            raise Exception('No es una lista')
    def addColeccion(self,elementoAdd,pos = -1):
        if self.esLista:
            self.colecciones.insert(pos,elementoAdd)  
    def deleteColeccion(self,pos):
        if self.esLista:
            self.colecciones.pop(pos)
    def mostrar(self):
        for i in self.colecciones:
            print(i)
    def update(self,new_valor,pos):
        if self.esLista  and  type(pos) == int and pos < len(self.colecciones) :
            self.colecciones[pos] = new_valor
        else:
            raise Exception('el indice no es correcto')
    def buscaPos(self,valor):
        pos = 0
        for j in self.colecciones:
            if j == valor:
                return pos
            pos += 1
        return 'no se encuentra en la lista/tupla'
    def comprueba2(self):
        for w in range(len(self.colecciones)):
            if w < len(self.colecciones) and self.colecciones[w] == self.colecciones[w+1] and self.colecciones[w] ==2:            
                return True
        return False
    def suma(self):
        if 6 not in self.colecciones or 7 not in self.colecciones:
            return sum(self.colecciones)
        indice_6= self.colecciones.index(6)
        indice_7= self.colecciones.index(7)
        del self.colecciones[indice_6:indice_7 + 1]
        return sum(self.colecciones)
    def resta(self):
        if self.esLista:   
            self.colecciones.sort(reverse =True)
            return self.colecciones[0] - self.colecciones[-1]
    def impares(self):
        num_impares = 0
        for x in self.colecciones:
            if x % 2 == 1:
                num_impares += 1
        return num_impares


try:
    c1 = crud([20, 16, 9, 8, 4, 3, 1])
    #print( c1.comprueba2())
    print(c1.suma())
    print(c1.resta())
    print(c1.impares())
    c0 = crud(['rojo','verde'])
    c0.addColeccion('azul')  
    c0.deleteColeccion(0)
    c0.update('amarillo',1)
    print(c0.colecciones)
    c0.mostrar()  
    print(c0.buscaPos('amarillo'))

except:
    print('error2') 
'''
class person:
    def __init__(self,Nombre,Apellido1,Apellido2,Edad,Nacionalidad,Peso):
        self.nombre = Nombre
        self.apellido1 = Apellido1
        self.apellido2 = Apellido2
        self.edad = Edad
        self.nacionalidad = Nacionalidad
        self.peso = Peso
class player(person):
    def __init__(self,Nombre,Apellido1,Apellido2,Edad,Nacionalidad,Peso,Dorsal,Posicion,Num_ficha):
        self.dorsal = Dorsal
        self.posicion = Posicion
        self.num_ficha = Num_ficha
        super().__init__(Nombre,Apellido1,Apellido2,Edad,Nacionalidad,Peso)
    
p0 = player('Pablo','Martin','Mayoral',21,'Española',65.00,7,'central',7894)
print(p0.nombre)
'''