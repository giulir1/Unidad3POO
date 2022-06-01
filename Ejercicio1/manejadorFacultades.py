import csv
from carrera import carrera
from facultad import facultad


class manejadorFacultades:
    __listaF = []

    def __init__(self):
        self.__listaF = []

    def leerArchivo(self):
        archivo = open('facultades.csv', encoding='utf8')
        reader = csv.reader(archivo, delimiter=';')
        fila = next(reader)
        band = True
        while band:
            listaCarreras = []
            filaCarrera = next(reader)
            while band and fila[0] == filaCarrera[0]:
                unaCarrera = carrera(filaCarrera[0], filaCarrera[1], filaCarrera[2], filaCarrera[3], filaCarrera[4], filaCarrera[5])
                listaCarreras.append(unaCarrera)
                try:
                    filaCarrera = next(reader)
                except StopIteration:
                    band = False
            unaFacultad = facultad(fila[0], fila[1], fila[2], fila[3], fila[4], listaCarreras)
            self.__listaF.append(unaFacultad)
            fila = filaCarrera
        archivo.close()

    def mostrar(self):
        for i in self.__listaF:
            print(i)
            i.mostrarCarreras()

    def mostrarFacultadyCarreras(self, cod):
        band = False
        i = 0
        while (i < len(self.__listaF)) and (not band):
            if cod == str(self.__listaF[i].getCodigo()):
                band = True
                print('{}'.format(self.__listaF[i].getNombre()))
                print('-CARRERAS')
                self.__listaF[i].mostrarCarreraYDuracion()
            else:
                i += 1
        if not band:
            print('No se encontró la facultad con el código {}.'.format(cod))

    def mostrarDatosCarrera(self, nombre):
        band = False
        i = 0
        while (i < len(self.__listaF)) and (not band):
            indice = self.__listaF[i].buscarCarrera(nombre)
            if indice != -1:
                band = True
                self.__listaF[i].mostrarDatos(indice)
            else:
                i += 1
        if not band:
            print('No se encontró la carrera {}. NOTA: recuerde colocar los acentos debidos.'.format(nombre))
