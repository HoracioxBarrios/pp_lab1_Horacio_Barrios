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
def mostrar_nombres_posicion_o_ubicacion(
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
            print("Incorrecto: ingrese numero valido")


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
        lista_jugadores : list, indice_elegido : int)-> str:
    '''
    Prepara un texto con el nombre del jugador y sus estadisticas.
    Recibe: (arg 1) la lista de jugadores y (arg 2) el indice (int) 
    que eligio el usuario.
    Devuelve: la cadena de texto.
    '''
    if(lista_jugadores):
        for indice in range(len(lista_jugadores)):
                if(indice == indice_elegido):#cambios
                    dato_nombre_y_posicion = "Nombre: {0}\nPosicion: {1}".format(
                        lista_jugadores[indice]["nombre"],
                        lista_jugadores[indice]["posicion"])
                    
                    lista_estadisticas = []
                    diccionario_estadisticas = lista_jugadores[indice]["estadisticas"]
                    for clave, valor in diccionario_estadisticas.items():
                        dato_estadistica = "{0}: {1}".format(clave, valor)
                        lista_estadisticas.append(dato_estadistica)
        estadisticas = "\n".join(lista_estadisticas)
        nombre_estadisticas = "{0}\n{1}".format(
                dato_nombre_y_posicion, estadisticas)
        return nombre_estadisticas
    else:
        return "Lista vacia"
    
def seleccionar_jugador_segun_indice(lista_jugadores : list[dict])-> None | int:
    '''
    Permite selecionar un jugador por su indice en la lista.
    Recibe una lista de Jugadores.
    Devuelve: -1 en caso de ser lista vacia.
    '''
    if(lista_jugadores):
        while(True):
            mostrar_nombres_posicion_o_ubicacion(
                lista_jugadores, ver_indice_ubi =True)
            mensaje = ">>> Ingrese numero de (indice) del jugador para ver sus estadisticas: "
            indice_elegido = pedir_ingreso_de_numero(r"^[0-9]+$", mensaje)
            existe_indice = comprobar_indice_valido(
                lista_jugadores, indice_elegido)
            if(existe_indice):
                return indice_elegido
            else:
                print("Indice invalido, intente nuevamente...\n ")
                os.system('cls')           
    else:
        print("La lista está vacia")
        return -1



'''
3) Después de mostrar las estadísticas de un jugador seleccionado por el usuario,
permite al usuario guardar las estadísticas de ese jugador en un archivo CSV. El
archivo CSV debe contener los siguientes campos: nombre, posición, temporadas,
puntos totales,promedio de puntos porpartido,rebotestotales,promedioderebotes
por partido, asistencias totales, promedio de asistencias por partido, robos totales,
bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y
porcentajedetirostriples
'''
def guardar_a_csv(path_nombre : str, dato_a_guardar : str):
    with open(path_nombre, "w") as archivo:
        archivo.write(dato_a_guardar)
        nombre_en_lista = re.findall(r"[a-zA-Z_]+\.[csv]{3}", path_nombre)
        nombre_str = "".join(nombre_en_lista)
        print("Se guardó archivo como : {0}".format(nombre_str))

           
def desea_guardar_como_archivo(path_nombre : str, dato_a_guardar : str):
    mensaje = ">>> Desea Guardarlo como archivo? si/no "
    respuesta = si_no_del_usuario(mensaje)
    if(respuesta):
        guardar_a_csv(path_nombre, dato_a_guardar)
        
def si_no_del_usuario(mensaje_a_mostrar : str):
    while(True):
        eleccion_user = input(mensaje_a_mostrar)
        eleccion_user = eleccion_user.lower()
        respuesta_lista = re.findall(r"^[si]{2}$|^[no]{2}$",eleccion_user)
        respuesta_str = "".join(respuesta_lista)
        if(respuesta_str == "si"):
            return True
        elif(respuesta_str == "no"):
            return False
        else:
           print("Elija una Opcion valida...")
           
def separar_campo_y_valor_de_una_lista(lista : list[str])-> str:
    '''
    separa campos de una lista
    Recibe una lista de cadenas str
    Devuelve una cadena ordenada y formateada
    '''
    if(lista):
        lista_campos = []
        lista_valores = []
        for indice in range(len(lista)):
            lista[indice] = lista[indice].strip(" ")
            if(indice % 2 == 0):
                lista_campos.append(lista[indice])
            else:
                lista_valores.append(lista[indice])
        cadena_campos = "".join(lista_campos)
        cadena_valores = "".join(lista_valores)
        datos_estadisticas_preparada_csv = "{0}\n{1}".format(cadena_campos, cadena_valores)
        return datos_estadisticas_preparada_csv
        
    else:
        print("La lista esta vacia") 
    
    
#Nombre Michael Jordan
def sacar_nombre_de_cadena(cadena : str):
    nombre_lista = re.findall(r"Nombre: (.*)", cadena)
    nombre_str = "".join(nombre_lista)
    return nombre_str

def seleccionar_guardar_estadisticas_jugador_elegido(lista_jugadores : list):
    indice_elegido = seleccionar_jugador_segun_indice(lista_jugadores)
    nombre_mas_estadisticas = preparar_texto_estadisticas(lista_jugadores, indice_elegido)
    print_dato(nombre_mas_estadisticas)
    nombre_del_jugador_con_espacio =sacar_nombre_de_cadena(nombre_mas_estadisticas)
    nombre_del_jugador_mas_guion_bajo = nombre_del_jugador_con_espacio.replace(" ", "_")
    
    path_nombre_formateado = "parcial\estadisticas_del_jugador_{0}.csv".format(nombre_del_jugador_mas_guion_bajo)
    
    desea_guardar_como_archivo(path_nombre_formateado,nombre_mas_estadisticas)
    
#--Menú y ejecucion de la app

def opciones_del_menu()-> str:
    '''
    Opciones del menu.
    Recibe: No aplica.
    Devuelve: una cadena str .
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
    mensaje_a_mostrar = "Por favor ingrese una opcion "
    numero_ingresado = pedir_ingreso_de_numero(r"^[0-9]+$", mensaje_a_mostrar)
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
                mostrar_nombres_posicion_o_ubicacion(lista_Jugadores)
            case 2:
                seleccionar_guardar_estadisticas_jugador_elegido(lista_Jugadores)
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