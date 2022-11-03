import argparse
'''1. (1 punto) Crear la clase Alumno con los datos relativos a un alumno (id, nombre, apellidos, email). 

 

Tendrá los siguientes métodos: 

(0,5) Constructor: dónde recibirá los datos del alumno.
(0,5) Deberá tener un método para imprimir los datos.'''

class Alumno:
    def __init__(self,ID,Nombre,Apellidos,Email):
        self.id = ID
        self.nombre = Nombre
        self.apellidos = Apellidos
        self.email = Email
    def __str__(self):
        return 'ID: ' + str(self.id) + ' Nombre: ' + self.nombre + ' Apellidos: ' + self.apellidos + ' email: ' + self.email

'''2. (4,5 puntos) Crear la clase Listado, que recibirá un fichero con los alumnos de asignaturas y grupos. 
La clase tendrá los siguientes métodos:

(0,25) Constructor: recibirá el fichero de alumnos Alumnos.txt (disponible en la sección módulos), deberá definir una lista vacía
para almacenar los nombres de los ficheros de actas generados en el método GenerarActas.
(2,5) GenerarActas: deberá leer el fichero de alumnos y crear tantos ficheros nuevos como asignaturas y grupos existan,
de forma que si en el fichero de alumnos hay 6 alumnos, de los cuales 4 son de la asignatura 2455 grupo A y 2 alumnos de la misma
asignatura pero del grupo B, deberá generar un fichero con esos 4 alumnos llamado "Acta_2455_GRUPO_A.txt" y otro fichero con los 2 del 
grupo B llamado "Acta_2455_GRUPO_B.txt". No olvides guardar el nombre del fichero en la lista de esta clase destinada para ello.  
(1,25) Repetidos: no recibirá nada, deberá leer los datos de todos los ficheros generados en GenerarActas y deberá devolver una lista
alumnos qué existan en más de 1 acta. 
(0,5) InfoAlumno: recibirá el email de un alumno y deberá mostrar por pantalla los datos del alumno impresos a través del método 
adecuado de la clase Alumno.'''
class Listado:
    def __init__(self,path):
        self.path = path
        #el siguiente atributo es solamente en caso de que generar actas este incompleto para que me funcione el resto de metodos
        self.listado = [] 
        self.listaNombreFicheros = ['fichero1.txt','fichero2.txt']
        
    def generarActas(self):
        f = open(self.path,'r', encoding="UTF-8")
        datos = f.readlines()
        asig = []
        grupos = []
        listado = []
        
        for i in datos:
            lista = i.replace('\n','').split(';')
            self.listado.append(lista)
            asig.append(lista[4])
            grupos.append(lista[5])
        asigSinRepes = []
        grupoSinRepes = []
        for item in asig:
            if item not in asigSinRepes:
                asigSinRepes.append(item)
        for item2 in grupos:
            if item2 not in grupoSinRepes:
                grupoSinRepes.append(item2)
        print(asig)
        print(grupos)
    def repetido(self):
        diccionario ={}
        listados = []
        listaMail = []
        
        for i in self.listaNombreFicheros:
            
            f = open(i,'r+', encoding='UTF-8')
            listaA = f.readlines()
            aux = 0
            for j in listaA:
                lista = j.replace('\n','').split()
                listados.append(lista)
            for w in listados:
                listaMail.append(w[3])

            print(diccionario)
            print(listaMail)
            print(listados)
                    
    def infoalumno(self,mail):
        f = open(self.path,'r',encoding='UTF-8')
        datos = f.readlines()
        listados = []
        for x in datos:
            lista = x.replace('\n','').split(';')
            listados.append(lista)
            for j in listados:
                if mail in j:
                    result = j
        f.close()
        a1 = Alumno(result[3],result[0],result[1],result[2])
        print(a1)
'''parser = argparse.ArgumentParser()
parser.add_argument('-f','--file', type =str,required=True,help='fichero sobre el que buscar.',dest='path')
parser.add_argument('-r','--repetido',type=str,required=False,help='algo.',dest='var')
parser.add_argument('-a','--acta',type=str,required=False,help='algo.',dest='var1')
args = parser.parse_args()
ruta = Listado(args.file)
if args.repetido != None:
        print("...repetido...")
        ruta.repetido(args.var)
if args.generarActas != None:
        print("...repetido...")
        ruta.generarActas(args.var1)'''

a0 = Alumno(1,'Pablo','Martin Mayoral','p.martinmayoral@gmail.com')
print(a0)
g0 = Listado('Alumnos.txt')
g0.generarActas()
g0.repetido()
g0.infoalumno('borja109@test.es')