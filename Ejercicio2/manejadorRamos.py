from ramo import ramo


class manejadorRamos:
    __ramos = []
    __i = -1

    def __init__(self):
        self.__ramos = []

    def __str__(self):
        return '{}'.format(self.__ramos)

    def crearRamo(self):                # crea un ramo vacio
        unRamo = ramo()
        self.__ramos.append(unRamo)
        self.__i += 1
        return self.__i                 # devuelve el indice para usarlo más adelante

    def agregarFlor(self, flor, cant, indice):
        for i in range(cant):
            self.__ramos[indice].addFlor(flor)

    def cambiarTamano(self, cant, indice):
        self.__ramos[indice].setTamano(cant)

    def retornaTamano(self, indice):
        return self.__ramos[indice].getTamano()

    def mostrarRamosPorTamano(self, tamano):
        if tamano == '1':
            tamano = 'chico'
        elif tamano == '2':
            tamano = 'mediano'
        elif tamano == '3':
            tamano = 'grande'
        for i in self.__ramos:
            if i.getTamano().lower() == tamano:
                i.mostrarNombreFlores()
