from personal import Personal


class Docente(Personal):
    __carrera = ''
    __cargo = ''
    __catedra = ''
    __porcentajePorCargo = 0

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, areaInvestigacion='', tipoInvestigacion='', carrera='', cargo='', catedra='', porcentajePorCargo=0, categoriaIncentivos='', importeExtra=0):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, areaInvestigacion, tipoInvestigacion)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra
        self.__porcentajePorCargo = porcentajePorCargo

    def __str__(self):
        return '{} Carrera: {}. Cargo: {}. Cátedra: {}'.format(super().__str__(), self.__carrera, self.__cargo, self.__catedra)

    def getCarrera(self):
        return self.__carrera

    def getCargo(self):
        return self.__cargo

    def getCatedra(self):
        return self.__catedra

    def setPorcentaje(self, nuevo):
        self.__porcentajePorCargo = nuevo

    def toJSON(self):
        diccionario = dict(
            __class__=self.__class__.__name__,
            __atributos_=dict(
                cuil=super().getCuil(),
                apellido=super().getApellido(),
                nombre=super().getNombre(),
                sueldoBasico=super().getSueldoBasico(),
                antiguedad=super().getAntiguedad(),
                carrera=self.__carrera,
                cargo=self.__cargo,
                catedra=self.__catedra,
                porcentajePorCargo=self.__porcentajePorCargo
            )
        )
        return diccionario
