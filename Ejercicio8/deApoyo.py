from personal import Personal


class DeApoyo(Personal):
    __categoria = ''

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad)
        self.__categoria = categoria

    def __str__(self):
        return '{} Categoría: {}'.format(super().__str__(), self.__categoria)

    def getCategoria(self):
        return self.__categoria

    def toJSON(self):
        diccionario = dict(
            __class__=self.__class__.__name__,
            __atributos_=dict(
                cuil=super().getCuil(),
                ape=super().getApellido(),
                nom=super().getNombre(),
                sueldo=super().getSueldoBasico(),
                antiguedad=super().getAntiguedad(),
                categoria=self.__categoria
            )
        )
        return diccionario
