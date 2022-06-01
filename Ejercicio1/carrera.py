class carrera:
    __codigoFacultad = 0
    __codigoCarrera = 0
    __nombre = ''
    __titulo = ''
    __duracion = ''
    __tipo = ''

    def __init__(self, codigoF, codigoC, nombre, titulo, duracion, tipo):
        self.__codigoFacultad = str(codigoF)
        self.__codigoCarrera = str(codigoC)
        self.__nombre = str(nombre)
        self.__titulo = str(titulo)
        self.__duracion = str(duracion)
        self.__tipo = str(tipo)

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.__codigoFacultad, self.__codigoCarrera, self.__nombre, self.__titulo, self.__duracion, self.__tipo)

    def getCodigo(self):
        return self.__codigoCarrera

    def getNombre(self):
        return self.__nombre

    def getDuracion(self):
        return self.__duracion
