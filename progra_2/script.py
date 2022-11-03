import argparse



parser = argparse.ArgumentParser()
parser.add_argument('-f','--file', type =str,required=True,help='fichero sobre el que buscar.',dest='file')
parser.add_argument('-w','--word',type=str,required=True,help='palabra a buscar.',dest='word')
args = parser.parse_args()
archivo = open(args.file,'r')
archivo.read()
'''print(args)
print(args.file)
print(args.word)'''