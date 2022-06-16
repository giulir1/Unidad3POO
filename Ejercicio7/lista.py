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
        if isinstance(unPersonal, Personal):                # solo inserta instancias de la clase personal
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
        if isinstance(unPersonal, Personal):            # solo agrega instancias de la clase personal
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

    def mostrarTipo(self, posicion):    # muestra el tipo de dato en una posicion
        i = 0
        aux = self.__comienzo
        while (aux.getSiguiente() is not None) and (i < posicion):
            i += 1
            aux = aux.getSiguiente()
        if i == posicion:
            dato = aux.getDato()
            tipo = self.getTipo(dato)
        else:
            raise IndexError
        return tipo

    def crearAgente(self):              # crea un una instancia de personal
        print('--- DATOS DEL NUEVO AGENTE ---')
        cuil = input('- CUIL: ')
        apellido = input('- Apellido: ')
        nombre = input('- Nombre: ')
        sueldoBasico = float(input('- Sueldo básico: $'))
        antiguedad = int(input('- Antiguedad: '))
        tipoAgente = int(input('- Tipo de agente\n1 - Docente\n2 - Personal de apoyo\n3 - Investigador\n4 - Docente investigador\nOpción: '))
        if tipoAgente == 1:                             # DOCENTE
            print('-- DOCENTE --')
            carrera = input('- Carrera en la que dicta clases: ')
            cargo = input('- Cargo: ')
            catedra = input('- Catedra: ')
            unAgente = Docente(cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra)
        elif tipoAgente == 2:                           # PERSONAL DE APOYO
            print('-- DE APOYO --')
            categoria = int(input('- Categoría (número entero): '))
            unAgente = DeApoyo(cuil, apellido, nombre, sueldoBasico, antiguedad, categoria)
        elif tipoAgente == 3:                           # INVESTIGADOR
            print('-- INVESTIGADOR --')
            areaInvestigacion = input('- Área de investigación: ')
            tipoInvestigacion = input('- Tipo de investigación: ')
            unAgente = Investigador(cuil, apellido, nombre, sueldoBasico, antiguedad, areaInvestigacion, tipoInvestigacion)
        elif tipoAgente == 4:                           # DOCENTE INVESTIGADOR
            print('-- DOCENTE INVESTIGADOR --')
            carrera = input('- Carrera en la que dicta clases: ')
            cargo = input('- Cargo: ')
            catedra = input('- Catedra: ')
            areaInvestigacion = input('- Área de investigación: ')
            tipoInvestigacion = input('- Tipo de investigación: ')
            categoriaIncentivos = input('- Categoría en el programa de incentivos (I, II, III, IV o V): ')
            while categoriaIncentivos.lower() not in ['i', 'ii', 'iii', 'iv', 'v']:
                print('ERROR - Ingrese un número válido.')
                categoriaIncentivos = input('- Categoría en el programa de incentivos (I, II, III, IV o V): ')
            importeExtra = float(input('- Importe extra por investigación: $'))
            unAgente = DocenteInvestigador(cuil, apellido, nombre, sueldoBasico, antiguedad, areaInvestigacion, tipoInvestigacion, carrera, cargo, catedra, categoriaIncentivos, importeExtra)
        else:
            raise ValueError
        print('PERSONAL CREADO')
        return unAgente

    def ordenarLista(self, lista):
        orden = lista
        orden.sort()
        return orden

    def listaATexto(self, lista):
        text = ''
        for i in lista:
            text += '{}\n'.format(i)
        return text

    def docInvPorCarrera(self, carrera):
        aux = self.__comienzo
        lista = []
        band = False
        while aux is not None:
            dato = aux.getDato()
            if isinstance(dato, DocenteInvestigador):
                if carrera.lower() == dato.getCarrera().lower():
                    lista.append(dato)
                    band = True
            aux = aux.getSiguiente()
        lista = self.ordenarLista(lista)
        retorno = self.listaATexto(lista)
        if not band:
            retorno = None
        return retorno

    def contarPersonalPorArea(self, area):
        aux = self.__comienzo
        inv = 0
        docInv = 0
        while aux is not None:
            dato = aux.getDato()
            if isinstance(dato, Investigador):
                if isinstance(dato, DocenteInvestigador):
                    if area.lower() == dato.getArea().lower():
                        docInv += 1
                else:
                    if area.lower() == dato.getArea().lower():
                        inv += 1
            aux = aux.getSiguiente()
        text = 'Agentes en el área de investigación "{}"\nInvestigadores: {}\nDocentes investigadores: {}'.format(area, inv, docInv)
        return text

    def calculoSueldo(self, agente):    # (aumento*base)/100
        base = agente.getSueldoBasico()
        aumento = 0
        antiguedad = agente.getAntiguedad()
        aumento += (antiguedad * base)/100  # aumento de antiguedad para todos
        if isinstance(agente, Docente):     # aumento de DOCENTE
            cargo = agente.getCargo()
            if cargo.lower() == 'simple':
                aumento += (10 * base)/100      # aumenta el 10%
            elif cargo.lower() == 'semiexclusivo':
                aumento += (20 * base)/100      # aumenta el 20%
            elif cargo.lower() == 'exclusivo':
                aumento += (50 * base)/100      # aumenta el 50%
            if isinstance(agente, DocenteInvestigador):     # aumento de DOCENTE INVESTIGADOR
                aumento += agente.getImporteExtra()     # aumenta el importe extra de docente investigador
        elif isinstance(agente, DeApoyo):
            categoria = agente.getCategoria()
            if categoria <= 10:
                aumento += (10 * base) / 100    # aumenta el 10%
            elif (categoria > 10) and (categoria <= 20):
                aumento += (20 * base)/100      # aumenta el 20%
            elif (categoria > 20) and (categoria <= 30):
                aumento += (30 * base)/100      # aumenta el 30%
        sueldo = base + aumento     # calcula el sueldo final
        return sueldo

    def getTipo(self, agente):
        tipo = ''
        if isinstance(agente, Docente):
            if isinstance(agente, DocenteInvestigador):
                tipo = 'Docente investigador'
            else:
                tipo = 'Docente'
        elif isinstance(agente, DeApoyo):
            tipo = 'Personal de apoyo'
        elif isinstance(agente, Investigador):
            if isinstance(agente, DocenteInvestigador):
                tipo = 'Docente investigador'
            else:
                tipo = 'Investigador'
        return tipo

    def mostrarDatos(self):
        text = ''
        aux = self.__comienzo
        while aux is not None:
            dato = aux.getDato()
            nomb = dato.getNombre()
            ape = dato.getApellido()
            tipo = self.getTipo(dato)
            sueldo = self.calculoSueldo(dato)
            text += 'Nombre y Apellido: {} {}. Tipo de agente: {}. Sueldo: ${:.2f}\n'.format(nomb, ape, tipo, sueldo)
            aux = aux.getSiguiente()
        return text

    def mostrarPorCategoria(self, cat):
        total = 0.0
        text = ''
        band = False
        aux = self.__comienzo
        while aux is not None:
            dato = aux.getDato()
            if isinstance(dato, DocenteInvestigador):
                if cat.lower() == dato.getCategoria().lower():
                    band = True
                    text += 'Nombre y Apellido: {} {}. Importe extra: ${:.2f}\n'.format(dato.getNombre(), dato.getApellido(), dato.getImporteExtra())
                    total += dato.getImporteExtra()
            aux = aux.getSiguiente()
        if band:
            print('-- DOCENTES INVESTIGADORES DE CATEGORIA: {} --'.format(cat.upper()))
            print(text)
        return total
