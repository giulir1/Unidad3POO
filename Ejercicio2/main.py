from manejadorFlores import manejadorFlores
from manejadorRamos import manejadorRamos
if __name__ == '__main__':
    controlF = manejadorFlores()
    controlF.leerArchivo()
    controlR = manejadorRamos()
    controlF.mostrar()
    opcion = input('1 - Registrar ramo vendido\n2 - Mostrar flores más vendidas\n3 - Mostrar flores por tamaño de ramo\n0 - SALIR\nOpción: ')
    print('------------------------------------------------')
    while opcion != '0':
        if opcion == '1':
            print('REGISTRO DE VENTA\nNOTA: Los ramos pueden tener hasta 15 flores.')
            terminarRamo = False                                # bandera para terminar de crear el ramo
            cont = 0                                            # contador de flores para no exceder el tamaño
            indiceRamo = controlR.crearRamo()                   # crea ramo vacío
            while (cont < 15) and (not terminarRamo):           # maximo de flores = 15
                flor = input('Ingrese el nombre de la flor a agregar al ramo: ')
                unaFlor = controlF.buscarFlor(flor)             # devuelve una instancia de la clase flor
                if unaFlor is not None:                         # si no la encuentra devuelve None
                    try:
                        cantidad = int(input('Ingrese la cantidad de flores "{}" a agregar en el ramo: '.format(flor.upper())))
                        if cantidad > 15:                       # la cantidad de flores debe ser menor a 15
                            input('ERROR - El número máximo de flores en un ramo es 15. Presione enter para intentar nuevamente\n')
                        else:
                            cont += cantidad
                            if cont > 15:                       # la cantidad de flores debe ser menor a 15
                                input('ERROR - El número máximo de flores en un ramo es 15. Presione enter para intentar nuevamente.\n')
                                cont -= cantidad                # resta las flores excedentes
                            else:
                                controlR.agregarFlor(unaFlor, cantidad, indiceRamo)  # agrega la cantidad indicada de la flor ingresada
                                op = input('1 para terminar con el ramo / enter para continuar: ')
                                indiceFlor = controlF.retornaIndice(unaFlor)
                                controlF.venta(indiceFlor, cantidad)                 # actualiza cantidad vendida de la flor
                                if op == '1':
                                    terminarRamo = True
                    except ValueError:
                        input('ERROR - Debe ingresar un número válido, la flor no se añadió al ramo. Presione enter para volver a intentar.')
                else:
                    input('ERROR - No se encontró la flor {}. Presione enter para volver a intentar.'.format(flor))
            controlR.cambiarTamano(cont, indiceRamo)            # setea el tamaño del ramo según la cantidad de flores
            print('\nRAMO VENDIDO. TAMAÑO: {}'.format(controlR.retornaTamano(indiceRamo)))
        elif opcion == '2':
            masVendidas = controlF.ordenarPorVentas()           # ordena y muestra flores por cantidad vendidas
        elif opcion == '3':
            opcion2 = input('Ingrese un tamaño de ramo para mostrar las flores:\n1 - CHICO\n2 - MEDIANO\n3 - GRANDE\nOpción: ')
            if opcion2 not in (['1', '2', '3']):
                input('ERROR - Ingrese una opción válida. Presione enter para volver al menú.')
            else:
                controlR.mostrarRamosPorTamano(opcion2)
        else:
            input('ERROR - Ingrese una opción válida. Presione enter para volver al menú.')
        print('------------------------------------------------')
        opcion = input('1 - Registrar ramo vendido\n2 - Mostrar flores más vendidas\n3 - Mostrar flores por tamaño de ramo\n0 - SALIR\nOpción: ')
        print('------------------------------------------------')
