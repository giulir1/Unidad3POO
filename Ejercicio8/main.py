from ObjectEncoder import ObjectEncoder
from IDirector import IDirector
from ITesorero import ITesorero
from lista import Manejador


if __name__ == '__main__':
    jsonF = ObjectEncoder()
    d = jsonF.leerJSONArchivo('personal.json')
    listaPersonal = jsonF.decodificarDiccionario(d)
    opcion = input('Ingresar:\n1 - SI\n2 - NO\nOpcion: ')
    while opcion != '2':
        print('--------------------------------------------')
        usuario = input('Usuario: ')
        contrasena = input('Contraseña: ')
        if (usuario.lower() == 'utesorero') and (contrasena == 'ag@74ck'):
            listaPersonal.tesorero(ITesorero(Manejador))
        elif (usuario.lower() == 'udirector') and (contrasena == 'ufC77#!1'):
            listaPersonal.director(IDirector(Manejador))


