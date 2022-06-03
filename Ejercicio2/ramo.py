class ramo:
    __tamano = ''
    __flores = []

    def __init__(self,):
        self.__flores = []

    def __str__(self):
        return '{} {}'.format(self.__tamano, self.__flores)

    def addFlor(self, flor):
        self.__flores.append(flor)

    def setTamano(self, cant):
        if cant <= 5:
            self.__tamano = 'Chico'
        elif (5 < cant) and (cant <= 10):
            self.__tamano = 'Mediano'
        elif 10 < cant:
            self.__tamano = 'Grande'

    def mostrarNombreFlores(self):
        for i in self.__flores:
            print(i.getNombre())

    def getTamano(self):
        return self.__tamano
