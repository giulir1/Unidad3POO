from manejadorCalefactores import manejadorCalefactores


if __name__ == '__main__':

    manejador = manejadorCalefactores()
    manejador.leerArchivoGas()
    manejador.leerArchivoElectrico()
    opcion = input('1 - Mostrar calefactor a gas con menor costo de consumo\n2 - Mostrar calefactor eléctrico de menor consumo\n3 - Mostrar calefactor de menor consumo\n0 - SALIR\nOpción: ')
    while opcion != '0':
        print('------------------------------------------------')
        if opcion == '1':
            try:
                costo = int(input('Costo por metro cúbico: '))
                cant = int(input('Cantidad que se estime consumir en metro cúbico: '))
                pos = manejador.calcularCostoGas(costo, cant)
                print('CALEFACTOR A GAS CON MENOR COSTO DE CONSUMO')
                print(manejador.mostrarMarcaYModelo(pos))
            except ValueError:
                input('ERROR - Debe ingresar número válidos.\nPresione enter para volver al menú.')
        elif opcion == '2':
            try:
                costo = int(input('Costo del kilowatt/h: '))
                cant = int(input('Cantidad que se estime consumir por hora: '))
                pos = manejador.calcularCostoElectrico(costo, cant)
                print('CALEFACTOR ELECTRICO CON MENOR COSTO DE CONSUMO')
                print(manejador.mostrarMarcaYModelo(pos))
            except ValueError:
                input('ERROR - Debe ingresar número válidos.\nPresione enter para volver al menú.')
        elif opcion == '3':
            try:
                costo = int(input('Costo por metro cúbico/kilowatt por hora: '))
                cant = int(input('Cantidad que se estime consumir en metro cúbico/ por hora: '))
                pos = manejador.calcularCostoElectrico(costo, cant)
                print('CALEFACTOR DE MENOR CONSUMO')
                print(manejador.mostrarCalefactor(pos))
            except ValueError:
                input('ERROR - Debe ingresar número válidos.\nPresione enter para volver al menú.')
        else:
            print('ERROR - Ingrese una opción válida.')
        print('------------------------------------------------')
        opcion = input('1 - Mostrar calefactor a gas con menor costo de consumo\n2 - Mostrar calefactor eléctrico de menor consumo\n3 - Mostrar calefactor de menor consumo\n0 - SALIR\nOpción: ')

