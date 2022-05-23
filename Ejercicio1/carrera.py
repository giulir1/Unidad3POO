class carrera:
    __codigoFacultad = 0
    __codigoCarrera = 0
    __nombre = ''
    __duracion = ''
    __tipo = ''

    def __init_(self, codigoF, codigoC, nombre, duracion, tipo):
        self.__codigoFacultad = int(codigoF)
        self.__codigoCarrera = int(codigoC)
        self.__nombre = str(nombre)
        self.__duracion = str(duracion)
        self.__tipo = str(tipo)

    def __str__(self):
        return '{} {} {} {} {}'.format(self.__codigoFacultad, self.__codigoCarrera, self.__nombre, self.__duracion, self.__tipo)