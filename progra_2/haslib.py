import hashlib

#h.update(b'Mensaje')
#print(h.hexdigest())

def funcion(cadena1,cadena2):
    h = hashlib.new(cadena1,cadena2.encode('UTF-8'))
    return h.hexdigest()
lista = ['Sha1','md5','Sha256']
for i in lista:
    print(funcion(i,'cadena caracteres')) 

