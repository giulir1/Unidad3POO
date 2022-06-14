from personal import Personal


class Investigador(Personal):
    __areaInvestigacion = ''
    __tipoInvestigacion = ''

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, areaInvestigacion, tipoInvestigacion, categoriaIncentivos='', importeExtra=0):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad)
        self.__areaInvestigacion = areaInvestigacion
        self.__tipoInvestigacion = tipoInvestigacion

    def __str__(self):
        return '{} {} {}'.format(super().__str__(), self.__areaInvestigacion, self.__tipoInvestigacion)
