import csv
from carrera import carrera
from facultad import facultad

# {} []

class manejadorFacultades:
    __listaF = []

    def __init__(self):
        self.__listaF = []

    def leerArchivo(self):
        archivo = open('facultades.csv')
        reader = csv.reader(archivo, delimiter=':')
        fila = next(reader)
        band = True
        while band:    
            unaFacultad = facultad(fila[0], fila[1], fila[2], fila[3], fila[4])
            filaCarrera = next(reader)
            while band and fila[0] == filaCarrera[0]:
                unaCarrera = carrera(filaCarrera[0], filaCarrera[1], filaCarrera[2], filaCarrera[3], filaCarrera[4])
                self.__listaF.append(unaFacultad)
                try:
                    filaCarrera = next(reader)
                except StopIteration:
                    band = False
        archivo.close()

        for i in self.__listaF:
            print(i)