from ObjectEncoder import ObjectEncoder


if __name__ == '__main__':
    jsonF = ObjectEncoder()
    d = jsonF.leerJSONArchivo('personal.json')
    listaPersonal = jsonF.decodificarDiccionario(d)
    print(listaPersonal.mostrarTodo())

    # BIEN LEIDO - BIEN JERARQUIA DE CLASES - PUNTOS?
