import csv
import numpy as np
from calefactor import Calefactor
from calefactorAGas import CalefactorAGas
from calefactorElectrico import CalefactorElectrico


class manejadorCalefactores:
    __arregloCal = None
    __dimension = 0
    __i = 0

    def __init__(self):
        self.__arregloCal = np.empty(self.__dimension, dtype=Calefactor)

    def leerArchivoGas(self):
        band = False
        archivo = open('calefactor-a-gas.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            if not band:
                band = True
            else:
                self.__dimension += 1
                self.__arregloCal.resize(self.__dimension)
                unCalefactor = CalefactorAGas(fila[0], fila[1], fila[2], fila[3])
                self.__arregloCal[self.__i] = unCalefactor
                self.__i += 1
        archivo.close()

    def leerArchivoElectrico(self):
        band = False
        archivo = open('calefactor-electrico.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            if not band:
                band = True
            else:
                self.__dimension += 1
                self.__arregloCal.resize(self.__dimension)
                unCalefactor = CalefactorElectrico(fila[0], fila[1], fila[2])
                self.__arregloCal[self.__i] = unCalefactor
                self.__i += 1

    def mostrar(self):
        for i in self.__arregloCal:
            print(i)

    def mostrarMarcaYModelo(self, pos):
        marca = self.__arregloCal[pos].getMarca()
        modelo = self.__arregloCal[pos].getModelo()
        return 'Marca: {} Modelo: {}'.format(marca, modelo)

    def mostrarCalefactor(self, pos):
        text = ''
        if isinstance(self.__arregloCal[pos], CalefactorAGas):
            text += '- Calefactor a gas\n'
        elif isinstance(self.__arregloCal[pos], CalefactorElectrico):
            text += '- Calefactor eléctrico\n'
        text += '{}'.format(self.__arregloCal[pos])
        return text

    def calculo(self, pos, cant, costo):
        total = (self.__arregloCal[pos].getConsumo()/100)*cant*costo
        return total

    def calcularCostoGas(self, costo, cant):
        pos = -1
        minimo = 99999999999999
        for i in range(len(self.__arregloCal)):
            if isinstance(self.__arregloCal[i], CalefactorAGas):
                total = self.calculo(i, cant, costo)
                if total < minimo:
                    minimo = total
                    pos = i
        return pos

    def calcularCostoElectrico(self, costo, cant):
        pos = -1
        minimo = 99999999999999
        for i in range(len(self.__arregloCal)):
            if isinstance(self.__arregloCal[i], CalefactorElectrico):
                total = self.calculo(i, cant, costo)
                if total < minimo:
                    minimo = total
                    pos = i
        return pos

    def calcularGeneral(self, costo, cant):
        pos = -1
        minimo = 99999999999999
        for i in range(len(self.__arregloCal)):
            total = self.calculo(i, cant, costo)
            if total < minimo:
                minimo = total
                pos = i
        return pos
