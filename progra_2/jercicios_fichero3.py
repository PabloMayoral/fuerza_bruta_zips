class contacto:
    def __init__(self,Nombre,Apellidos,Telefono):
        self.id = None
        self.nombre = Nombre
        self.apellidos = Apellidos
        self.telf = Telefono
    def generarID(self):
        lonNombre = len(self.nombre)
        lonApellidos = len(self.apellidos.replace(' ',''))
        apellidoSplit = self.apellidos.split(' ')
        sumaLen = lonNombre+lonApellidos
        self.id = str(sumaLen)+self.nombre[0]+apellidoSplit[0][0]+apellidoSplit[1][0]
        return self.id
    def __str__(self) :
        return 'ID: '+self.id + ' Nombre: ' + self.nombre + ' Apellidos: ' +self.apellidos + ' Telefono: ' + str(self.telf)

class Agenda:
    pass
c0 = contacto('Pablo','Martin Mayoral',154841512)
c0.generarID()
print(c0)