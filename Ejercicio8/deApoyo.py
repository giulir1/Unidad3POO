from personal import Personal


class DeApoyo(Personal):
    __categoria = ''
    __porcentajePorCategoria = 0

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, categoria, porcentajePorCategoria):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad)
        self.__categoria = categoria
        self.__porcentajePorCategoria = porcentajePorCategoria

    def __str__(self):
        return '{} Categoría: {}'.format(super().__str__(), self.__categoria)

    def getCategoria(self):
        return self.__categoria

    def setPorcentaje(self, nuevo):
        self.__porcentajePorCategoria = nuevo

    def toJSON(self):
        diccionario = dict(
            __class__=self.__class__.__name__,
            __atributos_=dict(
                cuil=super().getCuil(),
                apellido=super().getApellido(),
                nombre=super().getNombre(),
                sueldoBasico=super().getSueldoBasico(),
                antiguedad=super().getAntiguedad(),
                categoria=self.__categoria,
                porcentajePorCategoria=self.__porcentajePorCategoria
            )
        )
        return diccionario
