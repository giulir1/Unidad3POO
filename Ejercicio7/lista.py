from zope.interface import implementer
from deApoyo import DeApoyo
from docente import Docente
from docenteInvestigador import DocenteInvestigador
from interfaz import Interfaz
from investigador import Investigador
from nodo import Nodo
from personal import Personal


@implementer(Interfaz)
class Manejador:
    __comienzo = None

    def __init__(self):
        self.__comienzo = None

#   ------  METODOS DE LA INTERFAZ  ------

    def insertarElemento(self, unPersonal, posicion):       # inserta un nodo en la posicion dada
        if isinstance(unPersonal, Personal):
            nodo = Nodo(unPersonal)
            aux = self.__comienzo
            i = 1
            if posicion == 0:
                nodo.setSiguiente(self.__comienzo)
                self.__comienzo = nodo
            else:
                while (aux.getSiguiente() is not None) and (i < posicion):
                    i += 1
                    aux = aux.getSiguiente()
                if i == posicion:
                    nodo.setSiguiente(aux.getSiguiente())
                    aux.setSiguiente(nodo)
                else:
                    del nodo
                    raise IndexError

    def agregarElemento(self, unPersonal):  # agrega un nodo a la lista
        if isinstance(unPersonal, Personal):
            nodo = Nodo(unPersonal)
            aux = self.__comienzo
            if self.__comienzo is None:
                nodo.setSiguiente(self.__comienzo)      # hace que el nodo apunte al siguiente (en el primer caso apunta a None)
                self.__comienzo = nodo                  # setea el comienzo de la lista en el nodo actual
            else:
                while aux.getSiguiente() is not None:   # si es el último nodo apunta a None y no realiza la asignación
                    aux = aux.getSiguiente()            # si no es el último nodo realiza la asignación
                nodo.setSiguiente(aux.getSiguiente())   # el nodo apunta al siguiente
                aux.setSiguiente(nodo)                  # el nodo anterior apunta al recien agregado

    def mostrarElemento(self, posicion):            # muestra el elemento indicado por el índice (empieza en 0)
        aux = self.__comienzo
        i = 0
        while (aux.getSiguiente() is not None) and (i < posicion):
            i += 1
            aux = aux.getSiguiente()
        if i == posicion:
            text = '{}'.format(aux.getDato())
        else:
            raise IndexError
        return text
#   --------------------------------------

#   ------  METODOS JSON  ------
    def nodosJSON(self):
        listaDict = []
        aux = self.__comienzo
        while aux is not None:
            dato = aux.getDato()
            listaDict.append(dato.toJSON())
            aux = aux.getSiguiente()
        return listaDict

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            aparatos=self.nodosJSON()
        )
        return d
#   ----------------------------

    def mostrarTodo(self):      # muestra todos los nodos de la lista
        text = ''
        aux = self.__comienzo
        while aux is not None:
            dato = aux.getDato()
            text += '{}\n'.format(dato)
            aux = aux.getSiguiente()
        return text
