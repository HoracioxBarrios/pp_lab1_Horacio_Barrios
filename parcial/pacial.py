import json
import os
import re

def clear_console() -> None:
    """
    Espera que el usuario ingrese enter 
    para reimprimir en consola las opciones.
    """
    _ = input('Presione una tecla para continuar...')
    os.system('cls')

def leer_archivo_json(nombre_path : str)-> list:
    '''
    Lee un archvo json.
    Recibe la ruta con el nombre de archivo .json.
    Devuelve una lista de jugadores
    '''
    with open(nombre_path, "r") as archivo:
        equipo = json.load(archivo)
    
        return equipo["jugadores"]

'''
1) Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
 Nombre Jugador- Posición. Ejemplo:
 Michael Jordan- Escolta
'''
def mostrar_nombres_posicion_o_tambien_ubicacion(
    lista_de_jugadores: list , ver_indice_ubi = False)-> None | int:
    '''
    Muestra los nombres, posicion de cada jugador y opcionalmente su indice.
    Recibe: una lista de jugadores y opcional puede elegir ver el indice 
    donde esta cada jugador (ver_indice = True).

    Devuelve: -1 en caso de lista vacia
    '''
    if(lista_de_jugadores):
        if(ver_indice_ubi):
            for indice in range(len(lista_de_jugadores)):
                dato_jugador = "Ubicacion {0}: {1}- {2}".format(
                    indice, lista_de_jugadores[indice]["nombre"], 
                    lista_de_jugadores[indice]["posicion"])
                print_dato(dato_jugador)
        else:
            for indice in range(len(lista_de_jugadores)):
                dato_jugador = "{0}- {1}".format(
                    lista_de_jugadores[indice]["nombre"],
                    lista_de_jugadores[indice]["posicion"])
                print_dato(dato_jugador)
    else:
        print("La lista está vacia")
        return -1



'''
2) Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas
 completas, incluyendo temporadas jugadas, puntos totales, promedio de puntos por
 partido, rebotes totales, promedio de rebotes por partido, asistencias totales,
 promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de
 tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.
'''
def pedir_ingreso_de_numero(patron_re : str, mensaje_a_mostrar : str)-> int:
    '''
    Pide el usuario un numero.
    Recibe: (arg1)Un patron Regex para validar.y (arg 2) un mensaje str para mostrar.
    Devuelve: el numero ingresado, casteado a int.
    '''
    while(True):
        mensaje = "{0}".format(mensaje_a_mostrar)
        numero_ingresado_str = input(mensaje)
        num_imgresado = re.findall(patron_re, numero_ingresado_str)
        if(num_imgresado):
            resultado_num_str = "".join(num_imgresado)
            resultado_num_int = int(resultado_num_str)
            return resultado_num_int
        else:
            print("Numero Incorrecto: ")


def comprobar_indice_valido(lista_jugadores : list, indice_elegido)-> bool:
    '''
    Comprueba si el indice pasado por parametro es menor a los 
    elementos de la lista de jugadores.
    Recibe: (arg1)lista_jugadores y (arg2)el numero que representa
    al indice a evaluar si esta en la lista.
    Deveulve: boolean
    '''
    len_lista = len(lista_jugadores)
    if(indice_elegido >= 0 and indice_elegido < len_lista):
        return True
    else:
        return False

def preparar_texto_estadisticas(
        lista_jugadores : list, indice_elegido : int)-> str | int:
    '''
    prepara un texto con el nombre del jugador y sus estadisticas.
    Recibe: (arg 1) la lista de jugadores y (arg 2) el indice (int) 
    que eligio el usuario.
    Devuelve: la cadena de texto. o sino -1
    '''
    if(lista_jugadores):
        for indice in range(len(lista_jugadores)):
                if(indice == indice_elegido):
                    dato_nombre_y_posicion = "Nombre {0}- Posicion: {1}".format(
                        lista_jugadores[indice]["nombre"],
                        lista_jugadores[indice]["posicion"])
                    
                    lista_estadisticas = []
                    diccionario_estadisticas = lista_jugadores[indice]["estadisticas"]
                    for clave, valor in diccionario_estadisticas.items():
                        dato_estadistica = "{0}: {1}".format(clave, valor)
                        lista_estadisticas.append(dato_estadistica)
        estadisticas = "\n".join(lista_estadisticas)
        nombre_estadisticas = "{0}\n{1}\n".format(
                dato_nombre_y_posicion, estadisticas)
        return nombre_estadisticas
    else:
        print("Lista vacia")
        return -1

def seleccionar_jugador_segun_indice(lista_jugadores : list[dict])-> None | int:
    '''
    Permite selecionar un jugador por su indice en la lista.
    Recibe una lista de Jugadores.
    Devuelve: -1 en caso de ser lista vacia.
    '''
    if(lista_jugadores):
        mostrar_nombres_posicion_o_tambien_ubicacion(
            lista_jugadores, ver_indice_ubi =True)
        patron_de_validacion = r"^[0-9]+$"
        mensaje = "Ingrese numero de ubicacion (indice) del jugador para ver sus estadisticas: "
        while(True):
            indice_elegido = pedir_ingreso_de_numero(patron_de_validacion, mensaje)
            existe_indice = comprobar_indice_valido(lista_jugadores, indice_elegido)
            if(existe_indice):
                nombre_estadisticas = preparar_texto_estadisticas(lista_jugadores, indice_elegido)
                print(nombre_estadisticas)
                break
            else:
                print("Indice invalido, intente nuevamente... ")           
    else:
        print("La lista está vacia")
        return -1


#--Menú y ejecucion de la app


def opciones_del_menu()-> str:
    '''
    Opciones del menu.
    Recibe: No aplica.
    Devuelve: una cadena str.
    '''
    opciones = "Bienvenido:\n1- Ver Jugadores y Posicion de todos los jugadores del Dream Team\n2- Seleccionar un jugador y ver sus estadisticas\n"
    return opciones

def print_dato(dato : str)->None:
    '''
    imprime una cadena de texto.
    Recibe una cadena.
    Devuelve: No aplica.
    '''
    print("{0}".format(dato))
    

def menu_principal()-> int:
    '''
    imprime el menu y toma una opcion del usuario
    recibe -no aplica
    devuelve la opcion elegida, en caso de False devuelve -1
    '''
    opciones_para_el_usuario = opciones_del_menu()
    print_dato(opciones_para_el_usuario)
    patron_de_validacion = r"^[0-9]+$"
    mensaje_a_mostrar = "Por favor ingrese una opcion "
    numero_ingresado = pedir_ingreso_de_numero(patron_de_validacion, mensaje_a_mostrar)
    return numero_ingresado
   
   
def aplicacion(lista_Jugadores : list[dict])-> None:
    '''
    opciones para el usuario
    Recibe la lista de Jugadores
    Devuelve: no aplica.
    '''
    while(True):
        opciones = menu_principal()
        match(opciones):
            case 1:
                mostrar_nombres_posicion_o_tambien_ubicacion(lista_Jugadores)
            case 2:
                seleccionar_jugador_segun_indice(lista_Jugadores)
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                break
            case _:
                print("Opcion incorrecta")
        clear_console()
 
        

def main()-> None:
    '''
    Ejecuta la aplicacion
    Recibe: -
    Devuelve: -No aplica
    '''
    lista_jugadores = leer_archivo_json("parcial\dt.json")
    aplicacion(lista_jugadores)
    

main()#Inicio del programa