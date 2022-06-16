from ObjectEncoder import ObjectEncoder


if __name__ == '__main__':
    jsonF = ObjectEncoder()
    d = jsonF.leerJSONArchivo('personal.json')
    listaPersonal = jsonF.decodificarDiccionario(d)
    opcion = input('1 - Insertar personal en una posición\n2 - Agregar personal al final de la lista\n3 - Mostrar el tipo de personal en una posición\n4 - Mostrar docentes investigadores de una carrera\n5 - Mostrar cantidad de docentes investigadores e investigadores de un área\n6 - Mostrar todo el personal\n7 - Mostrar docentes investigadores de una categoría\n8 - Guardar archivo .JSON\n0 - SALIR\nOpción: ')
    while opcion != '0':
        print('-------------------------------------------------')
        if opcion == '1':
            try:
                unAgente = listaPersonal.crearAgente()
                pos = int(input('Ingrese una posición para insertar en la lista: '))
                listaPersonal.insertarElemento(unAgente, pos)
            except IndexError:
                input('ERROR - La posición ingresada excede la cantidad de elementos de la lista. Intente nuevamente con un número más pequeño.\nPresione enter para volver al menú.')
                del unAgente
            except ValueError:
                input('ERROR - Debe ingresar número válidos.\nPresione enter para volver al menú.')
        elif opcion == '2':
            try:
                unAgente = listaPersonal.crearAgente()
                listaPersonal.agregarElemento(unAgente)
            except ValueError:
                input('ERROR - Debe ingresar número válidos.\nPresione enter para volver al menú.')
        elif opcion == '3':
            try:
                pos = int(input('Mostrar el tipo de agente almacenado en la posición: '))
                print(listaPersonal.mostrarTipo(pos))
            except IndexError:
                input('ERROR - La posición ingresada excede la cantidad de elementos de la lista. Intente nuevamente con un número más pequeño.\nPresione enter para volver al menú.')
            except ValueError:
                input('ERROR - Debe ingresar número válidos.\nPresione enter para volver al menú.')
        elif opcion == '4':
            carrera = input('Ingrese el nombre de la carrera: ')
            ret = listaPersonal.docInvPorCarrera(carrera)
            if ret is not None:
                print(ret)
            else:
                print('No hay docentes investigadores o no se encontró la carrera {}.'.format(carrera))
        elif opcion == '5':
            area = input('Ingrese el área de investigación: ')
            print(listaPersonal.contarPersonalPorArea(area))
        elif opcion == '6':
            print(listaPersonal.mostrarDatos())
        elif opcion == '7':
            cat = input('Ingrese una categoría (I, II, III, IV o V): ')
            if cat.lower() not in ['i', 'ii', 'iii', 'iv', 'v']:
                input('ERROR - Ingrese una opción válida.\nPresione enter para volver al menú.')
            else:
                impExtra = listaPersonal.mostrarPorCategoria(cat)
                if impExtra != 0:
                    print('Total de importes extra: ${:.2f}'.format(impExtra))
                else:
                    print('No hay docentes investigadores de categoría {}'.format(cat.upper()))
        elif opcion == '8':
            d = listaPersonal.toJSON()
            jsonF.guardarJSONArchivo(d, 'personal.json')
            print('ARCHIVO GUARDADO')
        print('-------------------------------------------------')
        opcion = input('1 - Insertar personal en una posición\n2 - Agregar personal al final de la lista\n3 - Mostrar el tipo de personal en una posición\n4 - Mostrar docentes investigadores de una carrera\n5 - Mostrar cantidad de docentes investigadores e investigadores de un área\n6 - Mostrar todo el personal\n7 - Mostrar docentes investigadores de una categoría\n8 - Guardar archivo .JSON\n0 - SALIR\nOpción: ')
