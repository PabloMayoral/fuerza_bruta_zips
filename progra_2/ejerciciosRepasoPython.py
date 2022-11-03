from logging import raiseExceptions
import random
import string


# 1. Crea una función en python que reciba una serie de parámetros indeterminados 
# cuente cuantos elementos de tipo int, float y bool hay, si existe algún elemento 
#de otro tipo debe ponerlos en una categoría "resto". 
#Ejemplo:
# Recibe la lista con los siguientes elementos: "1", 4.5, "Hola", (1,2,3,4), 'a', 
#2, 56, true 
# Imprimirá: 
# int -> 2
# float -> 1
# bool -> 1
# otros -> 4

def funcion1(*elementos):
    cuentaInt = 0
    cuentaFloat = 0
    cuentaBool = 0
    resto = 0
    for i in elementos:
        if type(i)==int:
            cuentaInt += 1
        elif type(i)==float:
            cuentaFloat +=1
        elif type(i)== bool:
            cuentaBool +=1
        else:
            resto += 1
    print('Int -> ' + str(cuentaInt) + "\nFloat -> " + str(cuentaFloat)+ "\nBool -> " + str(cuentaBool) + "\nResto -> " + str(resto))
funcion1("1", 4.5, "Hola", (1,2,3,4), 'a', 2, 56, True)

# 2. Crea una función en Python que reciba una cadena de texto y un numero entero, 
# y realice las siguientes acciones:
#    - Imprima los X últimos caracteres. Donde X será el entero recibido. 
#    - Imprima los X primeros caracteres. Donde X será el entero recibido. 
#    - Reemplace las aes y las oes por X. Donde X será el entero recibido.  
#    - Devuelva la cadena resultante invertida. 

def funcion2(texto,num):
    #Primera accion de la funcion
    textoInvertido = texto[::-1]
    reInvertido = textoInvertido[:num]
    ultimosCaracteres = reInvertido[::-1]
    #print(ultimosCaracteres)
    #Segunda accion de la funcion
    #print(texto[:num])
    #Tercera accion de la funcion
    new_texto = ''
    for x in texto.lower():
        if x != 'a' or x != 'o':
            new_texto += x
        else:
            new_texto += str(num)
    print(new_texto)
    #Cuarta accion de la funcion
    print(textoInvertido)
funcion2('Hola',2)
# 3. Crea la clase Documento, que tenga los siguientes atributos:
#   - Documento.
#   - Letra. 
# Deberá tener los siguiguientes métodos: 
#   - Constructor: recibirá sólo el documento sin letra. 
#   - CalcularLetra: cogerá el documento y si es válido, calculará la letra del mismo y la asignará al atributo correspondiente de la clase. 
#   - ValidarDNI: comprobará que sea un DNI válido, es decir que tenga 8 dígitos y no contenga caracteres no numéricos.
#   En caso de no ser válido deberá lanzar una excepción. 
# 
# El cálculo del DNI se realiza siguiendo las siguientes instrucciones:
#    - Se divide el numéro entre 23. 
#    - El resto se sustituye por una letra siguiendo esta tabla:
#    0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22
#    T  R  W  A  G  M  Y  F  P  D  X   B   N   J   Z   S   Q   V   H   L   C   K   E

class Documento:
    def __init__(self,documento):
        self.documento = documento
        self.letra = None
    def calcularLetra(self):
        listaLetras = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
        comprubaDocumento = self.documento.isdigit()
        if comprubaDocumento == True:
            calculaResto = int(self.documento) % 23
            self.documento += listaLetras[calculaResto]
        print(self.documento)
    def validarDni(self):
        try:
            if self.documento.isdigit() and len(self.documento) == 8:
                print('Documento DNI valido')
        except:
            print('Documento DNI no valido')
c = Documento('51127784')
c.calcularLetra()
# 4. Crea una función que sea un juego en el que el usuario tiene que acertar un 
#numero de X cifras, X se recibirá como parámetro de la función, 
# con las siguientes reglas: 
#   - El usuario tiene 9 oportunidades. 
#   - Si acierta un dígito deberá mostrarselo por pantalla con guiones en el resto de dígitos. 
#   - Si acierta el numero completo el programa le felicita por ganar y le preguntasi quiere jugar de nuevo. 
#   - En caso de no acertar, el programa debe continuar hasta que se quede sin oportunidades o acierte.
#   - Cada vez que el usuario introduzca un numero, si no acierta, el programa le indicará que no está ese dígito, 
#   además debe decirle cuantos intentos le quedan. 
#   - Si se queda sin oportunidades, ha perdido y el programa termina su ejecución.
# Se permite el uso de input para recoger el dígito del usuario.

def adivinaNumeros(tamañoNum):
    fallos = 0
    numeroOculto = ''
    w=1
    j=10
    for i in range(0,tamañoNum):
        numeroRandom = random.randint(w,j)
        w *=10
        j*=10
    print(numeroRandom)
    numeroOculto += str(numeroRandom) 
    print(numeroOculto[1])
    barras = []
    for i in range(0,tamañoNum):
            barras.append('_ ')
    print(barras)
    i = 1
    listaNumerosOcultos = []
    for recorreNumOcultos in numeroOculto:
        listaNumerosOcultos.append(recorreNumOcultos)
    my_input = input('Introduce el número que apareció en pantalla: ')
    listaInput=[]
    for recorreInput in my_input:
        listaInput.append(recorreInput)
    
    pos = 0
    for x in listaNumerosOcultos:
        for j in listaInput:
            if x == j:
                barras.pop(pos)
                barras.insert(pos,x)
            else:
                fallos += 1
        pos +=1
    print(barras)
adivinaNumeros(4)

# 5. Crea la clase Vehiculo que tendrá los siguientes atributos:
# - ID: int
# - Tipo: texto
# - Marca: texto
# - Modelo: texto
# - Peso: float
# - Stock: verdadero/false
# Además del constructor que deberá recibir los datos de un vehículo, añade un método para indicar 
# que hay stock y otro para indicar que ya no hay. 
# Crea un método para cambiar el modelo y peso del vehículo. 
# Crea el método que compruebe si el vehículo tiene marca y modelo, en caso de no tener uno de ellos deberá 
# lanzar una excepción.
# Añade el método para mostrar los datos del vehículo.

class vehiculo:
    def __init__(self,ID,Tipo,Marca,Modelo,Peso,Stock):
        self.id = ID
        self.tipo = Tipo
        self.marca = Marca
        self.modelo = Modelo
        self.peso = Peso
        self.stock = Stock
    def compruebaStock(self):
        if self.stock == False:
            print('No hay stock')
        else:
            print('Hay stock')
    def cambiaModeloPeso(self,new_modelo,new_peso):
        self.modelo = new_modelo
        self.peso = new_peso
    def compruebaMarcaModelo(self):
        if self.marca == None  or  self.modelo == None:
            raise Exception('no tiene marca o modelo')
    def __str__(self): #da info del objeto a mi gusto
        datos="datos del vehiculo con ID "+":"
        datos += "\n -- peso: "+str(self.peso)
        datos += "\n -- marca: "+str(self.marca)
        datos += "\n -- tipo: "+str(self.tipo)
        datos += "\n -- modelo: "+str(self.modelo)
        datos += "\n -- stock: "+str(self.stock)
        return datos  
try:
    v1 = vehiculo(1,'Deportivo','Audi','R8',230.05,True)
    v1.compruebaStock()
    v1.cambiaModeloPeso('GTR',300.0)
    v1.compruebaMarcaModelo()
    print(v1)
except:
    print('error')
# 6. Crea la clase Contrasenia que tendrá los siguientes atributos:
# - Tamanio: int
# - Contrasenia: texto
# - Robustez: bool
# Añade un método crearContrasenia que dependiendo del tamaño  
# generere una contraseña alfanumérica y la devuleva.  
# Añade otro método robustez que devuelva verdadero si la contraseña es 
# robusta, para ello debe tener al menos 2 numeros, tres o más letras minúsculas,
# 1 o más letras mayúsculas y al menos 1 guión medio o bajo.
# Añade un método para cambiar el tamaño de la contraseña y otro para mostrarla. 

class contrasenia:
    def __init__(self,Contrasenia,Robustez,Tamanio):
        self.Contrasenia = Contrasenia
        self.robustez = Robustez
        self.tamanio = Tamanio
    def crearContrasenia(self,longitud):
        letters_and_digits = string.ascii_letters + string.digits
        rand_string = ''.join(random.sample(letters_and_digits, longitud))
        print(rand_string)
        
    def compruebaRobustez(self):
        contadorNum= 0
        contadorLowerChar = 0
        contadorUpperChar = 0
        contadorGuion = 0
        for i in self.Contrasenia:
            if i.isdigit() == True:
                contadorNum += 1
            elif i.isupper() == True:
                contadorUpperChar +=1
            elif i.islower() == True:
                contadorLowerChar += 1
            elif i == '_' or i == '-':
                contadorGuion += 1
        if contadorGuion >= 1 and contadorLowerChar >= 3 and contadorNum >= 2 and contadorUpperChar >= 1:
            self.robustez = True
        else:
            self.robustez = False
        return self.robustez
    def cambiaTamanio(self,new_tamanio):
        self.tamanio = new_tamanio
        self.crearContrasenia(self.tamanio)
        return self.Contrasenia
p1 = contrasenia('',True,8)
p1.crearContrasenia(8)
print(p1.compruebaRobustez())
print(p1.cambiaTamanio(12))

# 7. Crea la clase CuentaUsuario que tendrá los siguientes atributos:
# - ID: int con el identificador del usuario
# - Email: texto con el email del usuario
# - Password: texto
# Añade un método crearCuenta, que dado un objeto de tipo Usuario, deberá llamar al
# método crearContrasenia de la clase Contrasenia para crearle una cuenta y mostrar el 
# siguiente texto:
# "Estimado usuario, sus credenciales de acceso son:
# Email -> xxxxxx@xxxx.es
# Password -> XXXXXXXXXXX"
class usuario:
    def __init__(self,ID,Mail):
        self.id_usuario = ID
        self.mail = Mail 
        
class cuentaUsuario:
    def creaCuenta(self,objUsuario):
        password = ''
        for i in objUsuario.mail:
            password += i
            if i == '@':
                break
        password += str(objUsuario.id_usuario)
        print('Estimado usuario, sus credenciales de acceso son:')
        print('Email: '+ objUsuario.mail)
        print('password: '+ password)
user = usuario(8,'mail@gmail.com')
p1 = cuentaUsuario()
p1.creaCuenta(user)

# 8. Crear la clase Poción con los siguientes atributos: 
#POCION_ID: int
#POCION_NOMBRE: texto
#PUNTOS: int
#LLENA: boolean
#Deberá tener los siguientes métodos:
# Constructor: recibirá todos los datos por parámetro, excepto el POCION_ID que 
#deberá generarlo aleatoriamente entre 1 y 100. 
# Vaciar: no recibirá nada y cambiará a false el atributo LLENA. 
# Método apropiado para imprimir los datos de la poción. 
#




class pocion:
    def __init__(self,Nombre_pocion,Llena,Puntos):
        self.id_pocion = random.randint(0,101)
        self.nombre_pocion = Nombre_pocion
        self.llena = Llena
        self.puntos_pocion = Puntos
    def vaciar(self):
        self.llena = False
    def __str__(self): #da info del objeto a mi gusto
        datos="Los datos de la poción son"+":"
        datos += "\n -- ID: "+str(self.id_pocion)
        datos += "\n -- Nombre: "+str(self.nombre_pocion)
        datos += "\n -- Llena: "+str(self.llena)
        datos += "\n -- Puntos: "+str(self.puntos_pocion)
        return datos 
poti = pocion('night vision',True,10)
poti.vaciar()
print(poti)
#Crear la clase Galo con los siguientes atributos:
#CLAVE: texto
#NOMBRE: texto
#FUERZA: int
#SALTO: float
#CASCO: boolean
#POCIONES: lista de objetos Pocion (vacía de inicio).
#Deberá tener los siguientes métodos: 
# Constructor de la clase: recibirá todos los datos menos la clave, que se deberá 
#rellenar llamando al método GenerarClave de la clase Galo. 
# GenerarClave: NO recibirá nada y devolverá la clave del Galo siguiendo el 
#siguiente patrón: 2 ultimas iniciales del nombre + FUERZA + la primera inicial del 
#nombre + una letra (siendo esta X si la fuerza es par, Y si es impar y Z si es 
#mayor que 10). 
# CogerPocion: recibirá un objeto de tipo poción y lo añadirá a la lista de 
#pociones, siempre que no exista una poción con el mismo nombre de poción. 
# BeberPocion: recibirá el nombre de la poción, comprobará si está en la lista de 
#pociones, si existe, deberá multiplicar la fuerza que ya tiene el galo con el 
#numero de puntos que tenga la poción, además deberá vaciar esa poción que está en 
#la lista. Si no tiene esa poción informará por pantalla. 
# Método para mostrar los datos del Galo.
#
class galo:
    def __init__(self,Nombre,Fuerza,Salto,Casco,Pociones):
        self.clave = ''
        self.nombre = Nombre
        self.fuerza = Fuerza
        self.salto = Salto
        self.casco = Casco
        self.pociones = Pociones
    def generarClave(self):
        if self.fuerza % 2 == 0:
            letra = 'X'
        elif self.fuerza % 2 == 1:
            letra = 'Y'
        elif self.fuerza > 10:
            letra = 'Z'
        self.clave = self.nombre[:-2] + str(self.fuerza)+self.nombre[:1] + letra
    def cogerPocion(self,objeto):
        for j in self.pociones:
            if objeto.nombre_pocion != self.nombre:
                self.pociones.append(objeto)
    def beberPocion(self,nombrePocion):
        for j in self.pociones:
            if nombrePocion == j.nombre_pocion:
                self.fuerza *= j.puntos_pocion
                j.vaciar()
    def __str__(self): #da info del objeto a mi gusto
        datos="Los datos de la poción son"+":"
        datos += "\n -- ID: "+str(self.clave)
        datos += "\n -- Nombre: "+str(self.nombre)
        datos += "\n -- fuerza: "+str(self.fuerza)
        datos += "\n -- salto: "+str(self.salto)
        datos += "\n -- casco: "+str(self.casco)
        datos += "\n -- pociones: "+str(self.pociones)
        return datos 
g0=galo('Asterix',78,39.07,True,[])
g0.generarClave()
g0.cogerPocion(pocion)
g0.beberPocion('night vision')

print(g0)

#Crear la clase Romano con los siguientes atributos:
#ROMANO_ID: int
#NOMBRE: texto
#FUERZA: int
#SALTO: float
#CASCO: boolean
#ARMA: texto
#Deberá tener los siguientes métodos: 
# Constructor de la clase: recibirá todos los datos. 
# FuerzaTotal: NO recibirá nada y devolverá la fuerza total del romano, que será la
#fuerza + un numero que dependerá del si no tiene arma (+0), si tiene una espada 
#(+1), un hacha (+2) o una lanza (+3). 
# Método adecuado para mostrar los datos del soldado.
#
class romano:
    def __init__(self,ID,Nombre,Fuerza,Salto,Casco,Arma):
        self.id = ID
        self.nombre = Nombre
        self.fuerza = Fuerza
        self.salto = Salto
        self.casco = Casco
        self.arma = Arma
    def fuerzaTotal(self):
        if self.arma == 'sin arma':
            self.fuerza += 0
        elif self.arma == 'espada':
            self.fuerza += 1
        elif self.arma == 'hacha':
            self.fuerza +=2
        elif self.arma == 'lanza':
            self.fuerza += 3
        return self.fuerza
    def __str__(self): #da info del objeto a mi gusto
        datos="Los datos de la poción son"+":"
        datos += "\n -- ID: "+str(self.id)
        datos += "\n -- Nombre: "+str(self.nombre)
        datos += "\n -- fuerza: "+str(self.fuerza)
        datos += "\n -- salto: "+str(self.salto)
        datos += "\n -- casco: "+str(self.casco)
        datos += "\n -- arma: "+str(self.arma)
        return datos 
r0 = romano(89,'Roman',58,48.4,True,'lanza')
print(r0.fuerzaTotal())
r1 = romano(14,'Julio',85,36.78,False,'hacha')
print(r0)
#Crear la clase Campaña con los siguientes atributos: 
#FECHA_ASALTO: texto
#GALO: un objeto de tipo galo.
#ESCUADRON: una lista de objetos de tipo ROMANO (al menos 3).
#Deberá tener los siguientes métodos: 
# Constructor que recibirá todos los datos por parámetro.
# FuerzaEscuadron: no recibirá nada y devolverá la fuerza total de todo el 
#escuadrón (la suma de las fuerzas totales de cada romano). 
# MedirFuerzas: no recibirá nada y devolverá true o false si el Galo necesita o no 
#tomarse una poción para ganar el asalto, deberá tomarse una poción si su fuerza 
#actual multiplicada por 2 no es mayor que la fuerza total del escuadrón de romanos.
# Asalto: no recibirá nada, y mostrará el resultado del combate entre el galo y 
#cada uno de los romanos, de 1 en 1. Primero deberá determinar si debe o no tomarse 
#una poción en base al método MedirFuerzas y deberá comprobar si la fuerza 
#resultante del Galo es mayor que la del Romano, tras cada combate debe restar a la 
#fuerza del Galo la fuerza del Romano de cara al siguiente combate. El Galo ganará 
#siempre y cuando venza a todos los romanos.

class campania:
    def __init__(self,Fecha_asalto,Galo,Escuadron):
        self.fecha_asalto = Fecha_asalto
        self.galo = Galo
        self.escuadron = Escuadron
    def fuerzaEscuadron(self):
        fuerzaEscuadron = 0
        for i in self.escuadron:
            fuerzaEscuadron += i.fuerza
        return fuerzaEscuadron
    def medirFuerzas(self):
        if self.galo.fuerza*2 < self.fuerzaEscuadron():
            return True
        else:
            return False
    def asalto(self):
        if self.medirFuerzas() == False:
            self.galo.beberPocion('night vision')
        for w in self.escuadron:
            self.galo.fuerza -= w.fuerza
            if self.galo.fuerza < 0:
                break
            print('el galo perdió')
c0 = campania('18/06/2022',g0,[r0,r1]) 
print(c0.fuerzaEscuadron())
print(c0.medirFuerzas())
c0.asalto()