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
        self.__sueldoBasico = float(sueldoBasico)
        self.__antiguedad = int(antiguedad)

    def __str__(self):
        return 'CUIL: {} Apellido y nombre: {}, {}. Sueldo Básico: ${} Antiguedad: {}'.format(self.__cuil, self.__apellido, self.__nombre, self.__sueldoBasico, self.__antiguedad)

    def getCuil(self):
        return self.__cuil

    def setBasico(self, nuevo):
        self.__sueldoBasico = nuevo

    def getApellido(self):
        return self.__apellido

    def getNombre(self):
        return self.__nombre

    def getSueldoBasico(self):
        return self.__sueldoBasico

    def getAntiguedad(self):
        return self.__antiguedad

    # SOBRECARGA DE OPERADORES
    def __lt__(self, other):
        return self.__apellido < other.getApellido()
