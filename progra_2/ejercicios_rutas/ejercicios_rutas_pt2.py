import os
class rute:
    def __init__(self,path):
        self.path = path
    def abrirfichero(self):
        try:
            f = open(self.path)
            return f
        except:
            raise Exception('error al abrir el fichero')
    def cerrarFichero(self,p):
        p.close()
    def imprimeTodo(self):
        self.abrirfichero()
        output_text = self.abrirfichero().read()
        self.cerrarFichero()
        return output_text
    def imprimePalabras(self):
        self.abrirfichero()
        casteado = self.imprimeTodo().split()
        for x in casteado:
            print(x)
        self.cerrarFichero(self.abrirfichero())
    def imprimePalabras2(self):
        self.abrirfichero()
        cadena_min = self.imprimeTodo().lower()
        casteado = cadena_min.split()
        for x in casteado:
            if 'o'  in x or 'a' in x:
                continue
            else:
                print(x)
        self.cerrarFichero(self.abrirfichero())
    def imprimeNum(self):
        self.abrirfichero()
        for x in self.imprimeTodo():
            if x.isdigit() == True:
                print(x)
        self.cerrarFichero(self.abrirfichero())
    def sustituye(self):
        lista_str = ['cero','uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve']
        f = open(self.path, 'r+')
        output_text = f.read()
        print(output_text)
        output_text2 = ""
        for x in output_text:
            if x.isdigit() == True:
                output_text2 += x.replace(x,lista_str[int(x)])
            else:
                output_text2 += x
        print(output_text2)
        self.cerrarFichero(f)
        os.remove(self.path)
        try:
            r = open(self.path,'w+')
            r.write(output_text2)
        except:
            raise Exception ('No se ha podido abrir el fichero o no se ha podido realizar la escritura')
        self.cerrarFichero(r)                    
f0 = rute('fichero.txt')
print(f0.imprimeTodo())
f0.imprimePalabras()
f0.imprimePalabras2()
f0.sustituye()