from zope.interface import Interface


class Interfaz(Interface):
    def insertarElemento(self, elemento, posicion):
        pass

    def agregarElemento(self, elemento):
        pass

    def mostrarElemento(self, posicion):
        pass
