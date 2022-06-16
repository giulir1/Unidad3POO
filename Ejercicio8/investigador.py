from personal import Personal


class Investigador(Personal):
    __areaInvestigacion = ''
    __tipoInvestigacion = ''

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, areaInvestigacion, tipoInvestigacion, categoriaIncentivos='', importeExtra=0):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad)
        self.__areaInvestigacion = areaInvestigacion
        self.__tipoInvestigacion = tipoInvestigacion

    def __str__(self):
        return '{} Área de investigacion: {}. Tipo de investigación: {}'.format(super().__str__(), self.__areaInvestigacion, self.__tipoInvestigacion)

    def getArea(self):
        return self.__areaInvestigacion

    def getTipo(self):
        return self.__tipoInvestigacion

    def toJSON(self):
        diccionario = dict(
            __class__=self.__class__.__name__,
            __atributos_=dict(
                cuil=super().getCuil(),
                ape=super().getApellido(),
                nom=super().getNombre(),
                sueldo=super().getSueldoBasico(),
                antiguedad=super().getAntiguedad(),
                areaInvestigacion=self.__areaInvestigacion,
                tipoInvestigacion=self.__tipoInvestigacion
            )
        )
        return diccionario
