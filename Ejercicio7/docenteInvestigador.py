from docente import Docente
from investigador import Investigador


class DocenteInvestigador(Docente, Investigador):
    __categoriaIncentivos = ''
    __importeExtra = 0.0

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, areaInvestigacion, tipoInvestigacion, carrera, cargo, catedra, categoriaIncentivos, importeExtra):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, areaInvestigacion, tipoInvestigacion, carrera, cargo, catedra)
        self.__categoriaIncentivos = categoriaIncentivos
        self.__importeExtra = float(importeExtra)

    def __str__(self):
        return '{} Categoría incentivos: {} Importe extra: {}'.format(super().__str__(), self.__categoriaIncentivos, self.__importeExtra)

    def getCategoria(self):
        return self.__categoriaIncentivos

    def getImporteExtra(self):
        return self.__importeExtra

    # SOBRECARGA DE OPERADORES
    def __lt__(self, other):
        return self.getNombre() < other.getNombre()

    def toJSON(self):
        diccionario = dict(
            __class__=self.__class__.__name__,
            __atributos_=dict(
                cuil=super().getCuil(),
                ape=super().getApellido(),
                nom=super().getNombre(),
                sueldo=super().getSueldoBasico(),
                antiguedad=super().getAntiguedad(),
                areaInvestigacion=super().getArea(),
                tipoInvestigacion=super().getTipo(),
                carrera=super().getCarrera(),
                cargo=super().getCargo(),
                catedra=super().getCatedra(),
                categoriaIncentivos=self.__categoriaIncentivos,
                importeExtra=self.__importeExtra
            )
        )
        return diccionario
