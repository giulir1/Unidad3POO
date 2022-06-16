from personal import Personal


class Docente(Personal):
    __carrera = ''
    __cargo = ''
    __catedra = ''

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, areaInvestigacion='', tipoInvestigacion='', carrera='', cargo='', catedra='', categoriaIncentivos='', importeExtra=0):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, areaInvestigacion, tipoInvestigacion)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra

    def __str__(self):
        return '{} Carrera: {}. Cargo: {}. Cátedra: {}'.format(super().__str__(), self.__carrera, self.__cargo, self.__catedra)

    def getCarrera(self):
        return self.__carrera

    def getCargo(self):
        return self.__cargo

    def getCatedra(self):
        return self.__catedra

    def toJSON(self):
        diccionario = dict(
            __class__=self.__class__.__name__,
            __atributos_=dict(
                cuil=super().getCuil(),
                ape=super().getApellido(),
                nom=super().getNombre(),
                sueldo=super().getSueldoBasico(),
                antiguedad=super().getAntiguedad(),
                carrera=self.__carrera,
                cargo=self.__cargo,
                catedra=self.__catedra
            )
        )
        return diccionario
