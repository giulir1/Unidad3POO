from manejadorFacultades import manejadorFacultades


if __name__ == '__main__':
    control = manejadorFacultades()
    control.leerArchivo()
    opcion = input('1 - Mostrar carreras por código de facultad\n2 - Buscar carrera\n0 - SALIR\nOpción: ')
    print('-----------------------------------------------------------------------------')
    while opcion != '0':
        if opcion == '1':
            cod = input('Ingrese código de facultad: ')
            control.mostrarFacultadyCarreras(cod)
        elif opcion == '2':
            nombreCarr = input('Ingrese el nombre de una carrera: ')
            control.mostrarDatosCarrera(nombreCarr)
        else:
            input('ERROR - Ingrese una opción válida. Presione enter para volver al menú.')
        print('-----------------------------------------------------------------------------')
        opcion = input('1 - Mostrar carreras por código de facultad\n2 - Buscar carrera\n0 - SALIR\nOpción: ')
        print('-----------------------------------------------------------------------------')
