from personal import Personal


class Docente(Personal):
    __carrera = ''
    __cargo = ''
    __catedra = ''

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra, categoriaIncentivos='', importeExtra=0):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, categoriaIncentivos, importeExtra)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra

    def __str__(self):
        return '{} {} {} {}'.format(super().__str__(), self.__carrera, self.__cargo, self.__catedra)
