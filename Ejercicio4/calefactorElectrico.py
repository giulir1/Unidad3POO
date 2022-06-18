from calefactor import Calefactor


class CalefactorElectrico(Calefactor):
    __potencia = 0

    def __init__(self, marca, modelo, potencia):
        super().__init__(marca, modelo)
        self.__potencia = int(potencia)

    def __str__(self):
        return '{} Potencia: {} watts'.format(super().__str__(), self.__potencia)

    def getConsumo(self):
        return self.__potencia
