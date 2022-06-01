from carrera import carrera


class facultad:
    __codigo = 0
    __nombre = ''
    __direccion = ''
    __localidad = ''
    __telefono = ''
    __carreras = []

    def __init__(self, codigo, nombre, direccion, localidad, telefono, carreras):
        self.__codigo = int(codigo)
        self.__nombre = str(nombre)
        self.__direccion = str(direccion)
        self.__localidad = str(localidad)
        self.__telefono = str(telefono)
        self.__carreras = carreras

    def __str__(self):
        return '{} {} {} {} {}'. format(self.__codigo, self.__nombre, self.__direccion, self.__localidad, self.__telefono)

    def mostrarCarreraYDuracion(self):
        for i in self.__carreras:
            print('{}. Duración: {}'.format(i.getNombre(), i.getDuracion()))

    def getNombre(self):
        return self.__nombre

    def getCodigo(self):
        return self.__codigo

    def getLocalidad(self):
        return self.__localidad

    def buscarCarrera(self, nombre):
        i = 0
        band = False
        while (i < len(self.__carreras)) and (not band):
            if self.__carreras[i].getNombre().lower() == nombre.lower():
                band = True
            else:
                i += 1
        if not band:
            i = -1
        return i

    def mostrarDatos(self, indice):
        print('Código Facultad: {} Código Carrera: {}\nCarrera: {}\nLocalidad: {}'.format(self.getCodigo(), self.__carreras[indice].getCodigo(), self.__carreras[indice].getNombre(), self.getLocalidad()))
