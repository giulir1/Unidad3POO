from docente import Docente
from investigador import Investigador


class DocenteInvestigador(Docente, Investigador):
    __categoriaIncentivos = ''
    __importeExtra = ''

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, areaInvestigacion, tipoInvestigacion, carrera, cargo, catedra, categoriaIncentivos, importeExtra):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, areaInvestigacion, tipoInvestigacion, carrera, cargo, catedra)
        self.__categoriaIncentivos = categoriaIncentivos
        self.__importeExtra = importeExtra

    def __str__(self):
        return '{} {} {}'.format(super().__str__(), self.__categoriaIncentivos, self.__importeExtra)
