from manejadorContratos import manejadorContratos
from manejadorEquipos import manejadorEquipos
from manejadorJugadores import manejadorJugadores


if __name__ == '__main__':
    controlE = manejadorEquipos()       # CREACION DE MANEJADORES
    controlJ = manejadorJugadores()
    controlC = manejadorContratos()
    controlE.leerArchivo()              # LECTURA DE ARCHIVOS
    controlJ.leerArchivo()
    opcion = input('1 - Crear contrato\n2 - Consultar jugadores contratados\n3 - Consultar contratos\n4 - Calcular importe de contratos\n5 - Guardar contratos\n0 - SALIR\nOpción: ')
    while opcion != '0':
        print('---------------------------------------------------------------------------')
        if opcion == '1':
            nombreJug = input('Ingrese el nombre y apellido de un jugador: ')
            indiceJug = controlJ.buscarJugadorPorNombre(nombreJug)      # busca jugador en manejador de jugadores
            if indiceJug != -1:
                if not controlJ.verificarContrato(indiceJug):
                    nombreEquip = input('Ingrese el nombre completo del equipo: ')
                    indiceEquip = controlE.buscarEquipo(nombreEquip)    # busca equipo en manejador de equipos
                    if indiceEquip != -1:
                        try:
                            cont = controlC.agregarContrato()               # agrega el contrato al manejador de contratos y lo devuelve
                            controlJ.agregarContrato(indiceJug, cont)       # agrega el contrato al jugador
                            controlE.agregarContrato(indiceEquip, cont)     # agrega el contrato al equipo
                            jug = controlJ.retornaJugador(indiceJug)        # devuelve el jugador
                            controlC.setJugador(cont, jug)                  # agrega la referencia al jugador al contrato
                            eq = controlE.retornaEquipo(indiceEquip)        # devuelve el equipo
                            controlC.setEquipo(cont, eq)                    # agrega la referencia al equipo al contrato
                        except ValueError:
                            input('ERROR - Debe ingresar un número válido. Presione enter para volver al menú.')
                    else:
                        input('No se encontró el equipo.\nNOTA: Recuerde respetar las tildes.\nPresione enter para volver al menú.')
                else:
                    input('El jugador ya tiene un contrato. Presione enter para volver al menú.')
            else:
                input('No se encontró el jugador.\nNOTA: Recuerde respetar las tildes.\nPresione enter para volver al menú.')
        elif opcion == '2':
            dni = input('Ingrese el DNI del jugador (sin puntos): ')
            indice = controlC.buscarJugPorDNI(dni)      # busca el jugador en el manejador de contratos
            if indice != -1:
                print('Jugador: {}\nContratado por: {}\nFecha de finalización del contrato: {}'.format(controlC.getNombreJug(indice), controlC.getNombreEquipo(indice), controlC.getFechaFin(indice)))
            else:
                print('El jugador con DNI: {} no está contratado por ningún equipo o no se encontró.'.format(dni))
        elif opcion == '3':
            equip = input('Ingrese el nombre completo del equipo (recuerde colocar las tildes necesarias): ')
            indice = controlE.buscarEquipo(equip)
            if indice != -1:
                controlC.listarJugadoresContratados(equip)      # hay que mostrar solo los contratos a los que le faltan 6 meses
            else:
                input('No se encontró el equipo.\nNOTA: Recuerde respetar las tildes.\nPresione enter para volver al menú.')
        elif opcion == '4':
            nombreEquipo = input('Ingrese el nombre completo del equipo (recuerde colocar las tildes necesarias): ')
            indice = controlE.buscarEquipo(nombreEquipo)
            if indice != -1:
                print('Importe total de sueldos del equipo {}: ${}'.format(nombreEquipo, controlC.calcularImporte(nombreEquipo)))
            else:
                input('No se encontró el equipo.\nNOTA: Recuerde respetar las tildes.\nPresione enter para volver al menú.')
        elif opcion == '5':
            if controlC.guardarContratos():                           # crea el archivo de contratos y guarda las instancias ahi
                print('Contratos guardados.\n')
            else:
                print('ERROR - No se guardaron los contratos.\n')
        else:
            input('ERROR - Ingrese una opción válida. Presione enter para volver al menú.')
        print('---------------------------------------------------------------------------')
        opcion = input('1 - Crear contrato\n2 - Consultar jugadores contratados\n3 - Consultar contratos\n4 - Calcular importe de contratos\n5 - Guardar contratos\n0 - SALIR\nOpción: ')
