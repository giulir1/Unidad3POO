import csv
from jugador import jugador


class manejadorJugadores:
    __listaJugadores = []

    def __init__(self):
        self.__listaJugadores = []

    def agregarJugador(self, unJugador):
        if isinstance(unJugador, jugador):
            self.__listaJugadores.append(unJugador)

    def leerArchivo(self):
        band = False
        archivo = open('jugadores.csv', encoding='utf8')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            if not band:
                band = True
            else:
                unJugador = jugador(fila[0], fila[1], fila[2], fila[3], fila[4])
                self.agregarJugador(unJugador)
        archivo.close()

    def mostrar(self):
        for i in self.__listaJugadores:
            print(i)

    def buscarJugadorPorNombre(self, nombre):
        i = 0
        band = False
        while (not band) and (i < len(self.__listaJugadores)):
            if nombre.lower() == self.__listaJugadores[i].getNombre().lower():
                band = True
            else:
                i += 1
        if not band:
            i = -1
        return i

    def buscarJugadorPorDNI(self, dni):
        i = 0
        band = False
        while (not band) and (i < len(self.__listaJugadores)):
            if dni == self.__listaJugadores[i].getDNI():
                band = True
            else:
                i += 1
        if not band:
            i = -1
        return i

    def verificarContrato(self, indice):
        band = False
        if self.__listaJugadores[indice].getContrato() is not None:
            band = True
        return band

    def agregarContrato(self, indice, cont):
        self.__listaJugadores[indice].setContrato(cont)

    def retornaJugador(self, indice):
        return self.__listaJugadores[indice].getJugador()
