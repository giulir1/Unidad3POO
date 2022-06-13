from ObjectEncoder import ObjectEncoder


if __name__ == '__main__':
    jsonF = ObjectEncoder()
    dic = jsonF.leerJSONArchivo('aparatoselectronicos.json')    # leer el archivo y cargar los datos en la lista
    listaAparatos = jsonF.decodificarDiccionario(dic)
    opcion = input('1 - Insertar un aparato en una posición determinada\n2 - Agregar un aparato al final de la lista\n3 - Mostrar tipo de objeto en una posición determinada\n4 - Mostrar aparatos marca "Philips"\n5 - Mostrar lavarropas con carga superior\n6 - Mostrar aparatos\n7 - Guardar archivo .JSON\n0 - SALIR\nOpción: ')
    while opcion != '0':
        print('---------------------------------------------------------------------------')
        if opcion == '1':       # inserta un aparato en una posicion dada
            try:
                unAparato = listaAparatos.crearAparato()
                pos = int(input('Ingrese la posición en la que desea guardar el aparato creado: '))
                while pos >= listaAparatos.getTope():
                    print('ERROR - La posición ingresada excede el tamaño de la lista. Intente nuevamente con un número más pequeño.')
                    pos = int(input('Ingrese la posición en la que desea guardar el aparato creado: '))
                listaAparatos.insertarElemento(unAparato, pos)
            except ValueError:
                input('ERROR - No se guardó el aparato, debe ingresar números válidos.\nPresione enter para volver al menú.')
        elif opcion == '2':     # agrega un aparato al final de la lista
            try:
                unAparato = listaAparatos.crearAparato()
                listaAparatos.agregarElemento(unAparato)
            except ValueError:
                input('ERROR - No se guardó el aparato, debe ingresar números válidos.\nPresione enter para volver al menú.')
        elif opcion == '3':     # muestra el tipo de dato almacenado en una posición dada
            try:
                posicion = int(input('Ingrese una posición: '))
                while posicion > listaAparatos.getTope():
                    print('ERROR - La posición ingresada excede el tamaño de la lista. Intente nuevamente con un número más pequeño.')
                    posicion = int(input('Ingrese una posición: '))
                print('El aparato almacenado en la posicion {} es de tipo: {}'.format(posicion, listaAparatos.mostrarTipo(posicion)))
            except ValueError:
                input('ERROR - Debe ingresar números válidos. Presione enter para volver al menú.')
        elif opcion == '4':
            print(listaAparatos.contarCantPhilips())
        elif opcion == '5':     # muestra la marca de lavarropas con carga superior
            print('Marcas de Lavarropas con carga superior:\n{}'.format(listaAparatos.mostrarMarcaLavarropas()))
        elif opcion == '6':
            print('- Marca, país e importe de venta de todos los aparatos en venta -')
            print(listaAparatos.mostrarDatos())
        elif opcion == '7':
            dic = listaAparatos.toJSON()
            jsonF.guardarJSONArchivo(dic, 'aparatoselectronicos.json')
            print('Archivo guardado con éxito.')
        else:
            input('ERROR - Ingrese una opción válida. Presione enter para volver al menú.')
        print('---------------------------------------------------------------------------')
        opcion = input('1 - Insertar un aparato en una posición determinada\n2 - Agregar un aparato al final de la lista\n3 - Mostrar tipo de objeto en una posición determinada\n4 - Mostrar aparatos marca "Philips"\n5 - Mostrar lavarropas con carga superior\n6 - Mostrar aparatos\n7 - Guardar archivo .JSON\n0 - SALIR\nOpción: ')
