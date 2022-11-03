'''if __name__ == "__main__":
    f = open('create.txt','x+')
    f.write('hello!')
    f.close()'''
'''if __name__ == "__main__":
    f = open('create.txt','a')
    f.write('hello!')
    f.close()'''
if __name__ == "__main__":
    f = open('prueba.txt','w+')
    f.write('paco sanz!')
    try:
        print(f.readlines())
    except:
        print('Error')
    f.close()
    #readlines() para textos cortos, readline() para textos grandes.