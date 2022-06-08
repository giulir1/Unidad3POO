from contrato import contrato


class jugador:
    __nombre = ''
    __dni = ''
    __ciudadNatal = ''
    __paisOrigen = ''
    __nacimiento = ''
    __contrato = None

    def __init__(self, nombre, dni, ciudad, pais, fechaNac):
        self.__nombre = nombre
        self.__dni = dni
        self.__ciudadNatal = ciudad
        self.__paisOrigen = pais
        self.__nacimiento = fechaNac

    def __str__(self):
        return 'Jugador: {} DNI: {} Ciudad natal: {} País: {} Nacimiento: {}'.format(self.__nombre, self.__dni, self.__ciudadNatal, self.__paisOrigen, self.__nacimiento)

    def setContrato(self, cont):
        self.__contrato = cont

    def getContrato(self):
        return self.__contrato

    def getNombre(self):
        return self.__nombre

    def getDNI(self):
        return self.__dni

    def getJugador(self):
        return self
