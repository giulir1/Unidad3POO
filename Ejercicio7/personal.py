class Personal(object):
    __cuil = ''
    __apellido = ''
    __nombre = ''
    __sueldoBasico = 0.0
    __antiguedad = 0

    def __init__(self,cuil, apellido, nombre, sueldoBasico, antiguedad, carrera='', cargo='', catedra='', categoria='', areaInvestigacion='', tipoInvestigacion='', categoriaIncentivos='', importeExtra=''):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldoBasico = sueldoBasico
        self.__antiguedad = antiguedad

    def __str__(self):
        return '{} {} {} {} {}'.format(self.__cuil, self.__apellido, self.__nombre, self.__sueldoBasico, self.__antiguedad)
