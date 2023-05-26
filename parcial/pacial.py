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

def leer_archivo_json(nombre_path : str)-> list[dict]:
    '''
    Lee un archvo json.
    Recibe la ruta con el nombre de archivo .json.
    Devuelve una lista de jugadores.
    '''
    with open(nombre_path, "r") as archivo:
        equipo = json.load(archivo)
    
        return equipo["jugadores"]

#1
def mostrar_nombres_posicion_o_ubicacion(
    lista_de_jugadores: list[dict] , ver_indice_ubi = False)-> None | int:
    '''
    Muestra los nombres, posicion de cada jugador y opcionalmente su indice.
    Recibe:(arg 1) una lista de jugadores y(arg 2) opcional puede 
    elegir ver el indice donde esta cada jugador (ver_indice = True).

    Devuelve: None o -1 en caso de lista vacia
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

#2
def pedir_ingreso_de_numero(patron_re : str, mensaje_a_mostrar : str)-> int:
    '''
    Pide el usuario un numero.
    Recibe: (arg1)Un patron Regex para validar.y (arg 2) un mensaje
    str para mostrar al usuario.
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

def comprobar_indice_valido(
    lista_jugadores : list[dict], indice_elegido: int)-> bool:
    '''
    Comprueba si el indice pasado por parametro es valido.
    Recibe: (arg1)lista_jugadores y (arg2)el numero (int ) que 
    representa al indice a evaluar si esta en la lista.
    Deveulve: boolean
    '''
    len_lista = len(lista_jugadores)
    if(indice_elegido >= 0 and indice_elegido < len_lista):
        return True
    else:
        return False
    
def seleccionar_jugador_segun_indice(lista_jugadores : list[dict])-> int | None:
    '''
    De los jugadores existentes permite al usuario elegir uno 
    segun su indice.
    Recibe una lista de Jugadores.
    Devuelve: el indice del jugador elegido, o 
    -1 en caso de ser lista vacia.
    '''
    if(lista_jugadores):
        while(True):
            mostrar_nombres_posicion_o_ubicacion(lista_jugadores, 
                                                 ver_indice_ubi =True)
            mensaje = ">>> Ingrese numero de (indice) del jugador para ver sus estadisticas: "
            indice_elegido = pedir_ingreso_de_numero(r"^[0-9]+$", mensaje)
            existe_indice = comprobar_indice_valido(lista_jugadores,
                                                    indice_elegido)
            if(existe_indice):
                return indice_elegido
            else:
                print("Indice invalido, intente nuevamente...\n ")
                os.system('cls')           
    else:
        print("La lista está vacia")
        return -1

def mensaje_estadisticas_para_guardar(
    lista_jugadores: list[dict], indice_elegido: int)-> str | int:
    '''
    Arma el mensaje de estadisticas del jugador para guardar a csv.
    Recibe: (arg 1) una lista de jugadores.(arg 2) el 
    indice elegido por el usuario.(Int).
    Devuelve una cadena formateada para csv. o -1 si 
    lista esta vacia
    '''
    if(lista_jugadores):
        lista_titulo = ["Nombre", "Posicion"]
        lista_valores = []
        for indice in range(len(lista_jugadores)):
            if indice == indice_elegido:
                lista_valores.append(str(lista_jugadores[indice]["nombre"]))
                lista_valores.append(str(lista_jugadores[indice]["posicion"]))
                
        diccionario_estadist = lista_jugadores[indice]["estadisticas"]
        for clave, valor in diccionario_estadist.items():
            clave = str(clave).capitalize().replace("_", " ")
            lista_titulo.append(clave)
            lista_valores.append(str(valor))
        
        cadena_titulos = ",".join(lista_titulo)
        cadena_valores = ",".join(lista_valores)
        return "{0}\n{1}".format(cadena_titulos,cadena_valores)
    else:
        print("La lista está vacía")
        return -1


def mensaje_estadisticas_para_mostrar(
    lista_jugadores : list[dict], indice_elegido : int)-> str | int:
    '''
    Arma el mensaje de estadisticas del jugador para mostrar al usuario.
    Recibe: (arg 1) una lista de jugadores.(arg 2) el 
    indice elegido por el usuario.(Int).
    Devuelve una cadena formateada para mostrar al usuario. o -1 si 
    lista esta vacia.
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
                        clave = str(clave).capitalize().replace("_"," ")
                        dato_estadistica = "{0}: {1}".format(clave, valor)
                        lista_estadisticas.append(dato_estadistica)
        estadisticas = "\n".join(lista_estadisticas)
        nombre_estadisticas = "{0}\n{1}".format(
                dato_nombre_y_posicion, estadisticas)
        return nombre_estadisticas
    else:
        print("Lista vacia")
        return -1
    


def preparar_texto_estadisticas_mostrar_o_guardar(
        lista_jugadores : list[dict], indice_elegido : int, para_guardar = False)-> str:
    '''
    Prepara un texto con el nombre del jugador y sus estadisticas.
    Recibe: (arg 1) la lista de jugadores y (arg 2) el indice (int) 
    que eligio el usuario.
    Devuelve: la cadena de texto.
    '''
    if(para_guardar):
        mensaje = mensaje_estadisticas_para_guardar(lista_jugadores, indice_elegido)
        return mensaje
    else:
        mensaje = mensaje_estadisticas_para_mostrar(lista_jugadores, indice_elegido)
        return mensaje
#3
def guardar_a_csv(path_nombre : str, dato_a_guardar : str)-> None:
    '''
    Guarda datos str a archivo .csv
    Recibe (arg 1)el nombre con la ruta donde se va a guardar el archivo.
    arg(2) el dato a guardar (str).
    Retorna - (None) o No aplica.
    '''
    with open(path_nombre, "w") as archivo:
        archivo.write(dato_a_guardar)
        mostrar_mensaje_se_guardo_como(path_nombre)

def mostrar_mensaje_se_guardo_como(path_nombre : str)-> None:
    ''' 
    Toma del nombre_path el nombre y lo formatea para armar
    el mensaje 'se guardo el archivo ...' y lo muestra.
    Recibe (arg 1) el nombre_path (str).
    Devuelve: None
    '''
    nombre_en_lista = sacar_nombre_de_cadena_con_regex(
        r"[a-zA-Z_]+\.[csv]{3}", path_nombre)
    nombre_str = "".join(nombre_en_lista)
    print("Se guardó archivo como : {0}".format(nombre_str))

def si_no_del_usuario(mensaje_a_mostrar : str)-> bool:
    '''
    Pregunta al usuario si/no validando la respuesta.
    Recibe el mensaje a preguntar.
    Devuelve: boolean
    '''
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
          
def desea_guardar_como_archivo_csv(path_nombre : str, dato_a_guardar : str)-> None:
    '''
    Pregunta al usuario si quiere guardar el archivo a csv.
    Recibe (arg 1) el nombre con la ruta donde se va a gudardar(str).
    (arg 2) el dato a guardar(str).
    Devuelve: No aplica.
    '''
    mensaje = ">>> Desea Guardarlo como archivo? si/no "
    respuesta = si_no_del_usuario(mensaje)
    if(respuesta):
        guardar_a_csv(path_nombre, dato_a_guardar)
    else:
        print("Eligió no guardar")
        
    
def mostrar_estadisticas_del_jugador_elegido( lista_jugadores : list[dict])-> int:
    '''
    Seleciona y muestra las estadisticas del jugador elegido.
    Recibe: La lista de Jugadores
    Devuelve el indice del jugador elegido.
    '''
    indice_elegido = seleccionar_jugador_segun_indice(lista_jugadores)
    nombre_mas_estadisticas_para_mostrar = preparar_texto_estadisticas_mostrar_o_guardar(
        lista_jugadores, indice_elegido, para_guardar= False)
    print_dato(nombre_mas_estadisticas_para_mostrar)
    return indice_elegido


def sacar_nombre_de_cadena_con_regex(exprecion_re_nombre :str, cadena : str)-> str:
    ''' 
    De una cadena toma el nombre del jugador segun expresion regular.
    Recibe una expresion regular para tomar el nombre (arg 2) y la cadena str.
    Devuelve el nombre del jugador.
    '''
    nombre_lista = re.findall(exprecion_re_nombre, cadena)
    nombre_str = "".join(nombre_lista)
    return nombre_str


def guardar_estadisticas_del_jugador_elegido(
    lista_jugadores : list[dict], indice_elegido : int)-> None:
    '''
    Permite guardar a arhivo las estadisticas del jugador antes,
    elegido.
    Recibe: (arg 1) la lista de jugadores, y (arg 2) el indice
    de la ulbicacion del jugador.
    Devuelve - None
    '''
    nombre_mas_estadisticas_para_mostrar = preparar_texto_estadisticas_mostrar_o_guardar(
        lista_jugadores, indice_elegido, para_guardar= False)
    nombre_del_jugador_con_espacios =sacar_nombre_de_cadena_con_regex(
        r"Nombre: (.*)", nombre_mas_estadisticas_para_mostrar)
    nombre_del_jugador_guion_con_bajo = nombre_del_jugador_con_espacios.replace(" ", "_")
    path_nombre_formateado = "parcial\estadisticas_por_jugador\estadisticas_del_jugador_{0}.csv".format(
        nombre_del_jugador_guion_con_bajo)
    nombre_mas_estadisticas_para_guardar = preparar_texto_estadisticas_mostrar_o_guardar(
        lista_jugadores, indice_elegido, para_guardar= True)
    desea_guardar_como_archivo_csv(
        path_nombre_formateado,nombre_mas_estadisticas_para_guardar)

    




'''
  4) Permitir al usuario buscar un jugador por su nombre y mostrar sus logros, como
    campeonatos de la NBA, participaciones en el All-Star y pertenencia al Salón de la
    FamadelBaloncesto,etc.
'''
  
  
  
  
  
  
#--Menú y ejecucion de la app
def opciones_del_menu()-> str:
    '''
    Opciones del menu.
    Recibe: No aplica.
    Devuelve: una cadena str .
    '''
    opciones = "Bienvenido:\n1- Ver Jugadores y Posicion de todos los jugadores del Dream Team\n2- Seleccionar un jugador para ver sus estadisticas (Opcional: guardar)\n3- Guardar estadisticas del jugador seleccionado\n"
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
    flag_guardar_estadisticas = False
    while(True):
        opciones = menu_principal()
        match(opciones):
            case 1:
                mostrar_nombres_posicion_o_ubicacion(lista_Jugadores)
            case 2:
                indice_elegido = mostrar_estadisticas_del_jugador_elegido(lista_Jugadores)
                flag_guardar_estadisticas = True
            case 3:
                if(flag_guardar_estadisticas):
                    guardar_estadisticas_del_jugador_elegido(lista_Jugadores, indice_elegido)
                else:
                    print("Pase por el punto 2 primero")
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