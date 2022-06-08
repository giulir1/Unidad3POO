class contrato:
    __inicio = ''
    __fin = ''
    __pagoMensual = 0.0
    __jugador = None
    __equipo = None

    def __init__(self, inicio, fin, pago):
        self.__inicio = inicio
        self.__fin = fin
        self.__pagoMensual = pago

    def __str__(self):
        return '{} {} {} {} {}'.format(self.__inicio, self.__fin, self.__pagoMensual, self.__jugador, self.__equipo)

    def setJugador(self, jugador):
        self.__jugador = jugador

    def setEquipo(self, equipo):
        self.__equipo = equipo

    def getJugador(self):
        return self.__jugador

    def getEquipo(self):
        return self.__equipo

    def getFechaInicio(self):
        return self.__inicio

    def getFechaFin(self):
        return self.__fin

    def getPago(self):
        return self.__pagoMensual
