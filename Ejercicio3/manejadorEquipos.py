import csv
import numpy as np
from equipo import equipo


class manejadorEquipos:
    __arreglo = None
    __dimension = 0
    __i = 0

    def __init__(self):
        self.__arreglo = np.empty(self.__dimension, dtype=equipo)

    def leerArchivo(self):
        band = False
        archivo = open('equipos.csv', encoding='utf8')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            if not band:
                band = True
                self.__dimension = int(fila[0])
                self.__arreglo.resize(self.__dimension)
            else:
                self.__arreglo[self.__i] = equipo(fila[0], fila[1])
                self.__i += 1
        archivo.close()

    def mostrar(self):
        for i in self.__arreglo:
            print(i)

    def buscarEquipo(self, nombre):
        i = 0
        band = False
        while (not band) and (i < self.__dimension):
            if self.__arreglo[i].getNombre().lower() == nombre.lower():
                band = True
            else:
                i += 1
        if not band:
            i = -1
        return i

    def agregarContrato(self, indice, cont):
        self.__arreglo[indice].addContrato(cont)

    def retornaEquipo(self, indice):
        return self.__arreglo[indice].getEquipo()
