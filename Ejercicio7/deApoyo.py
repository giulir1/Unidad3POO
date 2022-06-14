from personal import Personal


class DeApoyo(Personal):
    __categoria = ''

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad)
        self.__categoria = categoria

    def __str__(self):
        return '{} {}'.format(super().__str__(), self.__categoria)
