class equipo:
    __nombre = ''
    __ciudad = ''
    __contratos = None

    def __init__(self, nombre, ciudad):
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__contratos = []

    def __str__(self):
        return '{} {} {}'.format(self.__nombre, self.__ciudad, self.__contratos)

    def addContrato(self, cont):
        self.__contratos.append(cont)

    def getNombre(self):
        return self.__nombre

    def getEquipo(self):
        return self

    def getContrato(self, indice):
        return self.__contratos[indice]
