from calefactor import Calefactor


class CalefactorAGas(Calefactor):
    __matricula = ''
    __calorias = 0

    def __init__(self, marca, modelo, mat, calorias):
        super().__init__(marca, modelo)
        self.__matricula = mat
        self.__calorias = int(calorias)

    def __str__(self):
        return '{} Matrícula: {}. Calorías por metro cúbico: {}'.format(super().__str__(), self.__matricula, self.__calorias)

    def getConsumo(self):
        return self.__calorias
