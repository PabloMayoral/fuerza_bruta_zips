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
    def hay22(self):
        for i in range(len(self.colecciones)):
            if (i < (len(self.colecciones) - 1)) and (self.colecciones[i] == self.colecciones[i + 1]) and self.colecciones[i] == 2: 
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
c1 = crud([20, 16, 9, 8, 4, 3, 1])
print(c1.hay22())
try:
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