import csv
from dateutil.relativedelta import relativedelta    # imports para calcular las fechas
from datetime import datetime
from datetime import timedelta
import numpy as np
from contrato import contrato


class manejadorContratos:
    __arregloContratos = None
    __dimension = 0
    __i = 0

    def __init__(self):
        self.__arregloContratos = np.empty(self.__dimension, dtype=contrato)

    def agregarContrato(self):
        fechaInicio = input('Ingrese fecha de inicio del contrato: ')
        fechaFin = input('Ingrese fecha de finalización del contrato: ')
        pago = float(input('Ingrese pago mensual del contrato: '))
        unContrato = contrato(fechaInicio, fechaFin, pago)
        self.__dimension += 1
        self.__arregloContratos.resize(self.__dimension)
        self.__arregloContratos[self.__i] = unContrato
        self.__i += 1
        return unContrato

    def mostrar(self):
        for i in self.__arregloContratos:
            print(i)

    def setJugador(self, cont, jug):
        cont.setJugador(jug)

    def setEquipo(self, cont, eq):
        cont.setEquipo(eq)

    def buscarJugPorDNI(self, dni):
        i = 0
        band = False
        while (not band) and (i < self.__dimension):
            jug = self.__arregloContratos[i].getJugador()
            if jug.getDNI() == dni:
                band = True
            else:
                i += 1
        if not band:
            i = -1
        return i

    def getNombreJug(self, indice):
        jug = self.__arregloContratos[indice].getJugador()
        return jug.getNombre()

    def getNombreEquipo(self, indice):
        eq = self.__arregloContratos[indice].getEquipo()
        return eq.getNombre()

    def getFechaFin(self, indice):
        return self.__arregloContratos[indice].getFechaFin()

#    def verificarFecha(self):
#        fechaActual = datetime.now()
#        fechaActual = fechaActual.strftime("%Y-%m-%d")
#        dentroDeUnMes = fechaActual + timedelta(months=1)
#        print(dentroDeUnMes)

    def listarJugadoresContratados(self, nombreEquipo):
        for i in self.__arregloContratos:
            equip = i.getEquipo()
            if nombreEquipo.lower() == equip.getNombre().lower():
                jug = i.getJugador()
                print(jug)      # deberia mostrarlo solo cuando faltan 6 meses para terminar el contrato

    def calcularImporte(self, nombreEquipo):
        total = 0
        for i in self.__arregloContratos:
            equip = i.getEquipo()
            if nombreEquipo.lower() == equip.getNombre().lower():
                total += i.getPago()
        return total

    def guardarContratos(self):
        band = False
        with open('contratos.csv', 'w', newline='', encoding='utf8') as archivo:
            writer = csv.writer(archivo, delimiter=';')
            writer.writerow(['DNI', 'Equipo', 'Fecha de inicio', 'Fecha de finalización', 'Pago mensual'])
            for i in self.__arregloContratos:
                jug = i.getJugador()
                eq = i.getEquipo()
                writer.writerow([jug.getDNI(), eq.getNombre(), i.getFechaInicio(), i.getFechaFin(), i.getPago()])
                if not band:
                    band = True
        archivo.close()
        return band

    def leerArchivo(self):
        archivo = open('contratos.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            print(fila)
