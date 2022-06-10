from zope.interface import Interface
from zope.interface import implementer


class interfaz(Interface):
    def insertarElemento(self, elemento, posicion):
        pass

    def agregarElemento(self, elemento):
        pass

    def mostrarElemento(self, posicion):
        pass
