import json
from pathlib import Path
from aparato import aparato


class lavarropas(aparato):
    __capacidad = 0.0
    __velocidad = 0
    __cantidadProgramas = 0
    __tipoCarga = ''

    def __init__(self, marca, modelo, color, pais, precioBase, capacidad, velocidad, cantidadProgramas, tipoCarga):
        super().__init__(marca, modelo, color, pais, precioBase)
        self.__capacidad = float(capacidad)
        self.__velocidad = str(velocidad)
        self.__cantidadProgramas = int(cantidadProgramas)
        self.__tipoCarga = str(tipoCarga)

    def __str__(self):
        return '{} {} {} {} {}'.format(super().__str__(), self.__capacidad, self.__velocidad, self.__cantidadProgramas, self.__tipoCarga)

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
                velocidad=self.__velocidad,
                cantidadProgramas=self.__cantidadProgramas,
                tipoCarga=self.__tipoCarga
            )
        )
        return d

    def getCarga(self):
        return self.__tipoCarga

    def getCapacidad(self):
        return self.__capacidad
