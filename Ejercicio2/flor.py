class flor:
    __num = ''
    __nombre = ''
    __color = ''
    __descripcion = ''
    __ventas = 0

    def __init__(self, num, nombre, color, desc):
        self.__num = num
        self.__nombre = nombre
        self.__color = color
        self.__descripcion = desc

    def __str__(self):
        return '{} {} {} {}'.format(self.__num, self.__nombre, self.__color, self.__descripcion)

    def getNombre(self):
        return self.__nombre

    def getVenta(self):
        return self.__ventas

    def agregarVenta(self):
        self.__ventas += 1

    # SOBRECARGA

    def __gt__(self, other):
        return self.__ventas > other.getVenta()
