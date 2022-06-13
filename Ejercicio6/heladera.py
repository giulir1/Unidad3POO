import json
from pathlib import Path
from aparato import aparato


class heladera(aparato):
    __capacidad = 0
    __freezer = False
    __ciclica = False

    def __init__(self, marca, modelo, color, pais, precioBase, capacidad, freezer, ciclica):
        super().__init__(marca, modelo, color, pais, precioBase)
        self.__capacidad = str(capacidad)
        self.__freezer = str(freezer)
        self.__ciclica = str(ciclica)

    def __str__(self):
        return '{} {} {} {}'.format(super().__str__(), self.__capacidad, self.__freezer, self.__ciclica)

    def toJSON(self):                   # devuelve un diccionario que representa al objeto
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca=super().getMarca(),
                modelo=super().getModelo(),
                color=super().getColor(),
                pais=super().getPais(),
                precioBase=super().getPrecio(),
                capacidad=self.__capacidad,
                freezer=self.__freezer,
                ciclica=self.__ciclica
            )
        )
        return d

    def getFreezer(self):
        return self.__freezer

    def getCiclica(self):
        return self.__ciclica
