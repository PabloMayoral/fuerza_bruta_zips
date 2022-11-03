'''listado = ['hola como estas','esto es una prueba']
contador = 0
for x in listado:
    separacion = x.split()
    for i in separacion:
        if i == 'es':
            contador += 1
print(contador)'''




'''lista_prueba = '1 prueba 12'
for x in lista_prueba:
    
    if x.isdigit() == True:
        print('entra en el if')
        for w in x:
            print(w)
#print(lista_prueba[4])
casteado = lista_prueba.split()

for x in casteado:
        if 'o'  in x or 'a' in x:
            print(x)'''


'''cadena_min = cadena.lower()
casteado = cadena_min.split() 
for x in casteado:
    if 'o' in x or 'a' in x:
        continue
    else:
        print(x)'''
'''contador = 0'''













'''cadena = 'estO es una prueba 123214'
lista_str = ['cero','uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve']
#lista_int = [0,1,2,3,4,5,6,7,8,9]
for x in cadena:
    if x.isdigit() == True:
        cadena = cadena.replace(x,lista_str[int(x)])
print(cadena)'''

'''listado = [1,1,1,4,4,7,7,8,5,4,7,7]

listado.sort()
print(listado)'''


listado =  [['intelestelar', '2014', '6.5'], ['star wars', '2006', '8.9']]

for x in listado:
    if '6.5' in x:
        print(x)   




