class Calefactor:
    __marca = ''
    __modelo = ''

    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    def __str__(self):
        return 'Marca: {} Modelo: {}'.format(self.__marca, self.__modelo)

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo
