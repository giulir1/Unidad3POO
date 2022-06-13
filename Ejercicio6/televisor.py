import json
from pathlib import Path
from aparato import aparato


class televisor(aparato):
    __pantalla = ''
    __pulgadas = 0
    __definicion = ''
    __internet = False

    def __init__(self, marca, modelo, color, pais, precioBase, pantalla, pulgadas, definicion, internet):
        super().__init__(marca, modelo, color, pais, precioBase)
        self.__pantalla = str(pantalla)
        self.__pulgadas = str(pulgadas)
        self.__definicion = str(definicion)
        self.__internet = str(internet)

    def __str__(self):
        return '{} {} {} {} {}'.format(super().__str__(), self.__pantalla, self.__pulgadas, self.__definicion, self.__internet)

    def toJSON(self):               # devuelve un diccionario que representa al objeto
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca=super().getMarca(),
                modelo=super().getModelo(),
                color=super().getColor(),
                pais=super().getPais(),
                precioBase=super().getPrecio(),
                pantalla=self.__pantalla,
                pulgadas=self.__pulgadas,
                definicion=self.__definicion,
                internet=self.__internet
            )
        )
        return d

    def getDefinicion(self):
        return self.__definicion

    def getInternet(self):
        return self.__internet
