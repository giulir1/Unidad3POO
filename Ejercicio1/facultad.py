class facultad:
    __codigo = 0
    __nombre = ''
    __direccion = ''
    __localidad = ''
    __telefono = ''
    __carreras = []

    def __init__(self, codigo, nombre, direccion, localidad, telefono, unaCarrera):
        self.__codigo = int(codigo)
        self.__nombre = str(nombre)
        self.__direccion = str(direccion)
        self.__localidad = str(localidad)
        self.__telefono = str(telefono)
        self.__carreras.append(unaCarrera)

    def __str__(self):
        return '{} {} {} {} {}'. format(self.__codigo, self.__nombre, self.__direccion, self.__localidad, self.__telefono)