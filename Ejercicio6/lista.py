from zope.interface import implementer
from aparato import aparato
from heladera import heladera
from interfaz import interfaz
from lavarropas import lavarropas
from Nodo import Nodo
from televisor import televisor


@implementer(interfaz)
class Manejador:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None

#   ------  METODOS PARA LISTA ITERABLE  -------

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
        return dato
#   -------------------------------------------

    def getTope(self):
        return self.__tope

#   ------  METODOS DE LA INTERFAZ  ------

    def insertarElemento(self, elemento, posicion):         # inserta un nodo en la posición indicada por el índice (empieza en 0)
        if isinstance(elemento, aparato):                   # punto 1
            nodo = Nodo(elemento)
            aux = self.__comienzo
            i = 1
            if posicion > self.__tope:
                raise IndexError
            else:
                if posicion == 0:
                    nodo.setSiguiente(self.__comienzo)
                    self.__comienzo = nodo
                    # self.__actual = nodo
                else:
                    while (aux.getSiguiente() is not None) and (i < posicion):
                        i += 1
                        aux = aux.getSiguiente()
                    if i == posicion:
                        nodo.setSiguiente(aux.getSiguiente())
                        aux.setSiguiente(nodo)
                        # self.__actual = nodo
                    else:
                        del nodo
                        raise IndexError

    def agregarElemento(self, elemento):    # agrega un nodo a la lista
        if isinstance(elemento, aparato):   # punto 2
            nodo = Nodo(elemento)
            aux = self.__comienzo
            if self.__comienzo is None:
                nodo.setSiguiente(self.__comienzo)      # hace que el nodo apunte al siguiente (en el primer caso apunta a None)
                self.__comienzo = nodo                  # setea el comienzo de la lista en el nodo actual (la lista se guarda "de abajo hacia arriba")
                self.__actual = nodo                    # setea el actual como el nodo recien agregado
                self.__tope += 1                        # aumenta en 1 el tope de la lista)
            else:
                while aux.getSiguiente() is not None:   # si es el último nodo apunta a None y no realiza la asignación
                    aux = aux.getSiguiente()            # si no es el último nodo realiza la asignación
                nodo.setSiguiente(aux.getSiguiente())   # el nodo apunta al siguiente
                aux.setSiguiente(nodo)                  # el nodo anterior apunta al recien agregado
                self.__tope += 1

    def mostrarElemento(self, posicion):            # muestra el elemento indicado por el índice (empieza en 0)
        aux = self.__comienzo
        i = 0
        text = ''
        if posicion > self.__tope:
            raise IndexError
        else:
            while (aux.getSiguiente() is not None) and (i < posicion):
                i += 1
                aux = aux.getSiguiente()
            if i == posicion:
                text = '{}'.format(aux.getDato())
        return text
#   --------------------------------------

    def mostrarTipo(self, posicion):            # muestra el tipo de aparato indicado por el índice (empieza en 0)
        aux = self.__comienzo                   # punto 3
        i = 0
        text = ''
        if posicion > self.__tope:
            raise IndexError
        else:
            while (aux.getSiguiente() is not None) and (i < posicion):
                i += 1
                aux = aux.getSiguiente()
            if i == posicion:
                dato = aux.getDato()
                text = '{}'.format(type(dato))
        return text

    def agregaralprincipio(self, elemento):     # PRUEBA - No es necesario
        nodo = Nodo(elemento)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def mostrarTodo(self):  # muestra todos los datos de los elementos de la lista
        text = ''
        i = 0
        aux = self.__comienzo
        while aux is not None:  # recorre la lista
            text += '{} - {}\n'.format(i, aux.getDato())
            i += 1
            aux = aux.getSiguiente()
        return text

#   ------  METODOS JSON  ------

    def listaJSON(self):
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
            aparatos=self.listaJSON()
        )
        return d
#   -----------------------------

    def crearAparato(self):         # crea objetos para agregar a la lista en punto 1 y punto 2
        unAparato = None
        tipo = input('Seleccione el tipo de aparato\n1 - Televisor\n2 - Heladera\n3 - Lavarropas\nAparato: ')
        while tipo not in ['1', '2', '3']:
            print('Ingrese un número válido.')
            tipo = input('Seleccione el tipo de aparato\n1 - Televisor\n2 - Heladera\n3 - Lavarropas\nAparato: ')
        marca = input('Marca: ')                    # marca del aparato
        mod = input('Modelo: ')                     # modelo del aparato
        color = input('Color: ')                    # color del aparato
        pais = input('País de fabricación: ')       # pais de fabricacion del aparato
        precio = float(input('Precio base: $'))     # precio base del aparato
        if tipo == '1':  # TELEVISOR
            # pantalla del televisor
            pant = input('Tipo de pantalla:\n  1 - CRT\n  2 - VGA\n  3 - SVGA\n  4 - Plasma\n  5 - LCD\n  6 - LED\n  7 - TouchScreen\n  8 - MultiTouch\n Opción: ')
            if pant == '1':
                pant = 'CRT'
            elif pant == '2':
                pant = 'VGA'
            elif pant == '3':
                pant = 'SVGA'
            elif pant == '4':
                pant = 'Plasma'
            elif pant == '5':
                pant = 'LCD'
            elif pant == '6':
                pant = 'LED'
            elif pant == '7':
                pant = 'TouchScreen'
            elif pant == '8':
                pant = 'MultiTouch'
            else:
                raise ValueError
            # pulgadas del televisor
            pulg = int(input('Pulgadas: '))
            # definicion del televisor
            definicion = input('Definición de pantalla:\n  1 - SD\n  2 - HD\n  3 - FULL HD\n Opción: ')
            if definicion == '1':
                definicion = 'SD'
            elif definicion == '2':
                definicion = 'HD'
            elif definicion == '3':
                definicion = 'FULL HD'
            else:
                raise ValueError
            # conexion a internet del televisor
            internet = input('Conexión a Internet:\n  1 - SI\n  2 - NO\n Conexión: ')
            unAparato = televisor(marca, mod, color, pais, precio, pant, pulg, definicion, internet)
        elif tipo == '2':
            # capacidad de la heladera
            capacidad = int(input('Capacidad de la heladera (en litros): '))
            # freezer de la heladera
            freezer = input('Cuenta con freezer: \n  1 - SI\n  2 - NO\n Opción:')
            if freezer == '1':
                freezer = True
            elif freezer == '2':
                freezer = False
            else:
                raise ValueError
            # ciclica de la heladera
            ciclica = input('Es cíclica:\n  1 - SI\n  2 - NO\n Opción: ')
            if ciclica == '1':
                ciclica = True
            elif ciclica == '2':
                ciclica = False
            else:
                raise ValueError
            unAparato = heladera(marca, mod, color, pais, precio, capacidad, freezer, ciclica)
        elif tipo == '3':
            # capacidad de lavado del lavarropas
            cap = float(input('Capacidad de lavado (en kilos): '))
            # velocidad de centrifugado del lavarropas
            vel = int(input('Velocidad de centrifugado (en RPM): '))
            # cantidad de programas
            cantProg = int(input('Cantidad de programas de lavado: '))
            # tipo de carga del lavarropas
            tipoC = input('Tipo de carga:\n  1 - Frontal\n  2 - Superior\n Opción: ')
            if tipoC == '1':
                tipoC = 'Frontal'
            elif tipoC == '2':
                tipoC = 'Superior'
            else:
                raise ValueError
            unAparato = lavarropas(marca, mod, color, pais, precio, cap, vel, cantProg, tipoC)
        return unAparato

    def contarCantPhilips(self):        # devuelve la cantidad de aparatos de marca philips
        contTel = 0                     # punto 4
        contHel = 0
        contLav = 0
        aux = self.__comienzo
        while aux is not None:
            dato = aux.getDato()
            if dato.getMarca().lower() == 'philips':
                if isinstance(dato, televisor):
                    print('encontro tv')
                    contTel += 1
                elif isinstance(dato, heladera):
                    contHel += 1
                elif isinstance(dato, lavarropas):
                    contLav += 1
            aux = aux.getSiguiente()
        text = 'Aparatos marca "Philips"\n- Televisores: {}\n- Heladeras: {}\n- Lavarropas: {}'.format(contTel, contHel, contLav)
        return text

    def mostrarMarcaLavarropas(self):       # devuelve marcas de lavarropas con carga superior
        text = ''                           # punto 5
        aux = self.__comienzo
        while aux is not None:
            dato = aux.getDato()
            if isinstance(dato, lavarropas):
                if dato.getCarga().lower() == 'superior':
                    text += '- {}\n'.format(dato.getMarca())
            aux = aux.getSiguiente()
        return text

    def calcularImporte(self, elemento):
        aumento = 0
        base = float(elemento.getPrecio())
        if isinstance(elemento, televisor):     # calcula si es televisor
            definicion = elemento.getDefinicion().lower()
            if definicion == 'sd':
                aumento += base/100         # 1% del precio base
            elif definicion == 'hd':
                aumento += (2*base)/100     # 2% del precio base
            elif definicion == 'full hd':
                aumento += (3*base)/100     # 3% del precio base
            if elemento.getInternet == 'True':
                aumento += (10*base)/100    # 10% del precio base
        elif isinstance(elemento, heladera):    # calcula si es heladera
            freezer = elemento.getFreezer()
            if freezer:
                aumento += (5*base)/100     # 5% del precio base
            else:
                aumento += base/100         # 1% del precio base
            if elemento.getCiclica() == 'True':
                aumento += (10*base)/100    # 10% del precio base
        elif isinstance(elemento, lavarropas):  # calcula si es lavarropas
            capacidad = elemento.getCapacidad()
            if capacidad <= 5:
                aumento += base/100         # 1% del precio base
            elif capacidad > 5:
                aumento += (3*base)/100     # 3% del precio base
        importe = base + aumento  # aplica el  aumento
        return importe

    def mostrarDatos(self):
        aux = self.__comienzo
        text = ''
        while aux is not None:
            dato = aux.getDato()
            marca = dato.getMarca()
            pais = dato.getPais()
            importe = float(self.calcularImporte(dato))
            text += 'Marca: {:<10} País: {:<16} Importe: ${:.2f}\n'.format(marca, pais, importe)
            aux = aux.getSiguiente()
        return text
