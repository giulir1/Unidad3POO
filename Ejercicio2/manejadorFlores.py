import csv
import numpy as np
from flor import flor


class manejadorFlores:
    __arreglo = None
    __dimension = 0
    __i = 0

    def __init__(self):
        self.__arreglo = np.empty(self.__dimension, dtype=flor)

    def leerArchivo(self):
        band = False
        archivo = open('flores.csv',encoding='utf8')
        reader = csv.reader(archivo,delimiter=';')
        for fila in reader:
            if not band:
                band = True
            else:
                self.__dimension += 1
                self.__arreglo.resize(self.__dimension)
                unaFlor = flor(fila[0], fila[1], fila[2], fila[3])
                self.__arreglo[self.__i] = unaFlor
                self.__i += 1
        archivo.close()

    def mostrar(self):
        for i in self.__arreglo:
            print(i)

    def buscarFlor(self, nombreFlor):
        i = 0
        band = False
        unaFlor = None
        while (not band) and (i < self.__dimension):
            if nombreFlor.lower() == self.__arreglo[i].getNombre().lower():
                band = True
                unaFlor = self.__arreglo[i]
            else:
                i += 1
        return unaFlor

    def retornaIndice(self, unaFlor):
        i = 0
        band = False
        while (i < self.__dimension) and (not band):
            if self.__arreglo[i] == unaFlor:
                band = True
            else:
                i += 1
        return i

    def venta(self, indice, cantidad):
        for i in range(cantidad):
            self.__arreglo[indice].agregarVenta()

    def ordenarPorVentas(self):
        aux = np.sort(self.__arreglo)[::-1]
        for i in range(5):
            print('{}° - {} {} vendidas'.format(i+1, aux[i].getNombre(), aux[i].getVenta()))
