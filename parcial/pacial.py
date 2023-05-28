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
    with open(nombre_path, "r", encoding='utf-8') as archivo:
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

def pedir_ingreso_de_numero(
    patron_re: str, mensaje_a_mostrar: str) -> int | float:
    '''
    Pide al usuario un número.
    Recibe: (arg1) un patrón Regex para validar y (arg2) un mensaje str 
    para mostrar al usuario.
    Devuelve: el número ingresado, convertido a int o float.
    '''
    while True:
        mensaje = "{0}".format(mensaje_a_mostrar)
        numero_ingresado_str = input(mensaje)
        num_ingresado = re.findall(patron_re, numero_ingresado_str)
        if num_ingresado:
            resultado_num_str = "".join(num_ingresado)
            if resultado_num_str.count(".") == 1:
                resultado_num = float(resultado_num_str)
            elif resultado_num_str.count(".") == 0:
                resultado_num = int(resultado_num_str)
            return resultado_num
        else:
            print("Incorrecto: ingrese un número válido")


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
            mensaje = ">>>>> Ingrese numero de (indice) del jugador para ver sus estadisticas: "
            indice_elegido = pedir_ingreso_de_numero(r"^[0-9]+$", mensaje)
            existe_indice = comprobar_indice_valido(lista_jugadores,
                                                    indice_elegido)
            if(existe_indice):
                return indice_elegido
            else:
                print(" Indice invalido, intente nuevamente...\n ")
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
        mensaje = mensaje_estadisticas_para_guardar(
            lista_jugadores, indice_elegido)
        return mensaje
    else:
        mensaje = mensaje_estadisticas_para_mostrar(
            lista_jugadores, indice_elegido)
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
           print(" Elija una Opcion valida...")
          
def desea_guardar_como_archivo_csv(path_nombre : str, dato_a_guardar : str)-> None:
    '''
    Pregunta al usuario si quiere guardar el archivo a csv.
    Recibe (arg 1) el nombre con la ruta donde se va a gudardar(str).
    (arg 2) el dato a guardar(str).
    Devuelve: No aplica.
    '''
    mensaje = ">>>>> Desea Guardarlo como archivo? si/no "
    respuesta = si_no_del_usuario(mensaje)
    if(respuesta):
        guardar_a_csv(path_nombre, dato_a_guardar)
    else:
        print(" Eligió no guardar")
        
    
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
    Permite guardar a archivo las estadisticas del jugador antes
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


#4
def mostrar_nombres_jugadores(lista_jugadores : list[dict])-> None:
    '''
    Muestra los nombres de los jugadores.
    Recibe la lista de jugadores.
    Devuelve - No aplica
    '''
    lista_nombres_ordenados = ordenar_bubble_sort(lista_jugadores, clave="nombre")
    for jugador in lista_nombres_ordenados:
        print_dato(jugador)


def pedir_nombre_y_apellido_jugador()-> str:
    '''
    Pide el nombre y apellido del jugador.
    Recibe - no aplica
    Devuelve - el nombre con apellido validado
    '''
    nombre_apellido = input(
        ">>>>>> Ingrese nombre y apellido del jugador a Buscar ")
    nombre_apellido_cap = str(nombre_apellido).capitalize()
    nombre_validado = sacar_nombre_de_cadena_con_regex(
        r"^[A-Za-z]+\s{1}[A-Za-z]+$", nombre_apellido_cap)
    return nombre_validado.lower().strip()

def buscar_jugador_y_ver_sus_logros(lista_jugadores: list[dict]):
    '''
    Imprime por consola los logros del jugador buscado.
    Recibe la lista de jugadores.
    Devuelve - No aplica ------
    '''
    mostrar_nombres_jugadores(lista_jugadores)
    nombre_ingresado_lower = pedir_nombre_y_apellido_jugador()
    encontrado = False
    for jugador in lista_jugadores:
        if jugador["nombre"].lower().strip() == nombre_ingresado_lower:
            encontrado = True
            print("---- jugador encontrado ----")
            cadena_logros = "Nombre del Jugador: {0}\n{1}".format(
                jugador["nombre"], "\n".join(jugador["logros"]))
            print_dato(cadena_logros)
    if encontrado == False:
        print(" No existe el nombre en la lista")

#5
def calcular_promedio_de_puntos_equipo(lista_jugadores : list[dict])-> float:
    '''
    Calcula el promedio de puntos por partido de todo el equipo 
    del Dream team.
    Recibe la lista de jugadores. List
    Devuelve el promedio (Float)
    '''
    cantidad_de_jugadores = len(lista_jugadores)
    acum_promedio_jugador_puntos_por_partido = 0
    for jugador in lista_jugadores:
        dicc_estadisticas_jugador = jugador["estadisticas"]
        for clave, valor in dicc_estadisticas_jugador.items():
            if(clave == "promedio_puntos_por_partido"):   
                acum_promedio_jugador_puntos_por_partido += valor
    promedio_equipo =acum_promedio_jugador_puntos_por_partido / cantidad_de_jugadores
    
    return promedio_equipo


def ordenar_bubble_sort(lista_original : list[dict], clave = "nombre", orden = "asc")-> list:
    '''
    Ordena segun clave
    Recibe: (arg 1)una lista , (arg2) una clave ej:("nombre"),
    (arg 3) el orden( "asc" o "des").
    Devuelve: una lista de nombres ordenada alfabeticamente. list
    '''
    if(lista_original):
        lista = lista_original[:]
        len_lista = len(lista) - 1
        flag_swap = True
        while flag_swap:
            flag_swap = False
            for indice in range(len_lista):
                if lista[indice][clave] > lista[indice + 1][clave] and orden == "asc":
                    lista[indice], lista[indice + 1] = lista[indice + 1], lista[indice]
                    flag_swap = True
                if lista[indice][clave] < lista[indice + 1][clave] and orden == "des":
                    lista[indice], lista[indice + 1] = lista[indice + 1], lista[indice]
                    flag_swap = True
        lista_nombres = []
        for nombre in lista:
            lista_nombres.append(nombre[clave])
        return lista_nombres

 
def tomar_nombre_mas_estadisticas_mj_a_lista(lista_jugadores_original : list[dict],
    lista_jugadores_ordenada_alfabet : list,  clave_nombre="nombre",
    clave_estadistica= "estadisticas",
    clave_interior_estadistica ="promedio_puntos_por_partido"):
    '''
    De una lista obtiene los nombres de los jugadores con su estadistica,
    ejemplo promedio de puntos por partido armando un nuevo diccionario.
    Recibe: (arg 1)una lista de jugadores, (arg 2) una clave ej "nombre",
    (arg 3) otra clave (para diccionario dentro ej: "estadisticas",(arg 4)
    otra clave (para el dentro del dicc estadisticas ejemplo: 
    "promedio_puntos_por_partido"), (arg 5) orden="asc" (para el ordenamiento)
    Devuelve - una nueva lista_ con el nombre ordenado  su estadistica.
    '''
    
    nueva_lista_nombres = []
    nueva_lista_valores = []
    for jugador_lista_ordenada in lista_jugadores_ordenada_alfabet:
        for jugador_lista_original in lista_jugadores_original:
            if(jugador_lista_ordenada == jugador_lista_original[clave_nombre]):
                nombre = jugador_lista_original[clave_nombre]
                promedio = jugador_lista_original[clave_estadistica][clave_interior_estadistica]
                nueva_lista_nombres.append(nombre)
                nueva_lista_valores.append(promedio)
    clave_dicc_estadisticas_sin_guion = clave_interior_estadistica.replace("_", " ")
    nueva_lista_nombre_ordenado_y_estadistica = []
    for indice in range(len(nueva_lista_nombres)):
        mensaje = "{0} :  {1}  {2}".format(
            nueva_lista_nombres[indice], clave_dicc_estadisticas_sin_guion,
            nueva_lista_valores[indice])
        nueva_lista_nombre_ordenado_y_estadistica.append(mensaje)
    return nueva_lista_nombre_ordenado_y_estadistica


def imprimir_mensaje_nombres_estaditicas(lista_nombres__estadisticas : list):
    '''
    imprime el mensaje que esta en la lista.
    Recibe una lista con conmbre y estadisticas de ese player.
    devuelve- no aplica
    '''
    for nombre_estadisitca in lista_nombres__estadisticas:
        print(nombre_estadisitca)


def calcular_y_mostrar_el_promedio_de_puntos_del_dream_team(
    lista_jugadores : list[dict]):
    '''
    calcula y muestra el promedio de puntos del dream team y luego el promedio
    individual de cada uno.
    Recibe la lista de jugadores.
    Devuelve- no aplica.
    '''
    mensaje_promedio_de_equipo = calcular_promedio_de_puntos_equipo(lista_jugadores)    
    print_dato("El promedio de puntos por partido de todo el equipo es {0} ".format(
        round(mensaje_promedio_de_equipo, 2)))
    lista_ordenada_alfabeticamente =  ordenar_bubble_sort(
        lista_jugadores, clave="nombre", orden= "asc")
    
    lista_nombres_ordenado_y_estadisticas = tomar_nombre_mas_estadisticas_mj_a_lista(
        lista_jugadores,lista_ordenada_alfabeticamente ,clave_nombre="nombre",
        clave_estadistica= "estadisticas", 
        clave_interior_estadistica ="promedio_puntos_por_partido")
    
    imprimir_mensaje_nombres_estaditicas(lista_nombres_ordenado_y_estadisticas)
    
    
    
# 6
def buscar_jugador_y_ver_logro(
    lista_jugadores, clave_nombre="nombre", clave_logros="logros",
    valor_logro="Miembro del Salon de la Fama del Baloncesto", 
    mensaje_a_mostrar_en_print="Pertenece"):
    '''
    Permite al usuario ingresar el nombre de un jugador y mostrar su logro.
    ejemplo : si pertenece al salon de la fama.
    Recibe (arg ) la lista de jugadores, (arg 2) la clave_logros ejemplo ="logros",
    (arg 3) valor_logro ejemplo ="Miembro del Salon de la Fama del Baloncesto",
    (arg 4)mensaje_a_mostrar_en_print ejemplo ="Pertenece"
    '''
    mostrar_nombres_jugadores(lista_jugadores)
    nombre_ingresado_lower = pedir_nombre_y_apellido_jugador()
    encontrado = False
    flag_ok_condicion = False
    for jugador in lista_jugadores:
        if jugador[clave_nombre].lower().strip() == nombre_ingresado_lower:
            encontrado = True
            print("---- jugador encontrado ----")
            for logro in jugador[clave_logros]:
                if logro == valor_logro:
                    flag_ok_condicion = True
                elif logro != valor_logro:
                    flag_ok_condicion = False 
            break     
    if encontrado:
        if flag_ok_condicion:
            print("{0}: {1}".format(mensaje_a_mostrar_en_print, valor_logro))
        else:
            print("No {0} como: {1}".format(mensaje_a_mostrar_en_print, valor_logro))


#7

def calcular_max_min_estadisticas(
    lista_jugadores: list[dict], clave_estadistica = "estadisticas",
    clave_interior_estadistica = "rebotes_totales", maximo = True)-> int:
    '''
    Calcula el maximo o minimo de las estadisticas segun clave.
    Recibe: (arg 1)La lista de jugadores, (arg 2) la clave "estadisticas,
    (arg 3) la clave interior del diccionario estadisticas ej: "rebotes_totales",
    (arg 4) si maximo o minimo (maximo = True) por defecto.
    '''
    if(lista_jugadores):
        flag_primera_iteracion = True
        for indice in range(len(lista_jugadores)):
            diccionario_estadisticas = lista_jugadores[indice][clave_estadistica]
            valor_estadistica = diccionario_estadisticas[clave_interior_estadistica]
            
            if(flag_primera_iteracion or 
            (valor_estadistica > max_min_estadistica and maximo == True) or 
            (valor_estadistica < max_min_estadistica and maximo == False)): 
                max_min_estadistica = valor_estadistica
                max_min_indice = indice
                flag_primera_iteracion = False    
        return max_min_indice
    else:
        print("La lista está vacia")
        return -1

def armar_diccionario_jugador_max_min_estadisticas(
    lista_jugadores : list[dict], max_min_indice : int,clave_estadistica = "estadisticas",
    clave_interior_estadistica = "rebotes_totales")-> dict | int:
    '''
    Arma un diccionario con el nombre y la estadistica maxima o minima 
    obtenida. ejemplo: Nombre : Michael Jordan, Rebotes totales : 3520.
    Recibe (arg 1 ) la lista de jugadores, (arg 2) el indice maximo o
    minimo obtenido anteriormente. 
    (arg 3) la clave "estadisticas", (arg 4) la clave de la estadistica
    especifica del diccionario (Ejemplo : "rebotes_totales").
    '''
    if max_min_indice is None:
        print("Error al conseguir el jugador con la maxima o minima estadistica")
        return -1
    jugador_max_min_obtenido = lista_jugadores[max_min_indice]
    
    nuevo_dicc_nombre_estadistica_max_min = {}
    nuevo_dicc_nombre_estadistica_max_min["nombre"] = jugador_max_min_obtenido["nombre"]
    nuevo_dicc_nombre_estadistica_max_min[clave_interior_estadistica] = \
        jugador_max_min_obtenido[clave_estadistica][clave_interior_estadistica]
    
    return nuevo_dicc_nombre_estadistica_max_min


def preparar_datos_nombre_estadistica_de_diccionario_a_texto(
    diccionario_nombre_estadistica : dict)-> str:
    '''
    De un diccionario estadisticas arma una cadena str para imprimir.
    Recibe el diccionario  con los datos por ejemplo:  
    Nombre : Michael Jordan, Rebotes totales : 3520
    
    Devuelve una cadena formateada para imprimir por consola.
    '''
    pares_clave_valor = []
    for clave, valor in diccionario_nombre_estadistica.items():
        texto_par = "{0}: {1}".format(clave, valor)
        pares_clave_valor.append(texto_par.capitalize().replace("_", " "))

    cadena = "\n".join(pares_clave_valor)
    return cadena

def calcular_y_mostrar_jugador_mayor_estadistica(
    lista_jugadores : list[dict], clave_estadistica = "estadisticas", 
    clave_interior_estadistica = "rebotes_totales"):
    '''
   Calcula y muestra el nombre con su maxima estadistica, segun clave.
   Recibe (arg 1)la lsita de jugadores, (arg 2) la clave estadisticas,
   (arg 3) la clave de la estadistica ejemplo ("rebotes_totales").
   Devuelve: No aplica
    '''
    max_min_indice = calcular_max_min_estadisticas(
    lista_jugadores, clave_estadistica,clave_interior_estadistica, maximo= True)
    
    jugador_estadistica_dicc = armar_diccionario_jugador_max_min_estadisticas(
    lista_jugadores, max_min_indice ,clave_estadistica,
    clave_interior_estadistica)
    
    cadena = preparar_datos_nombre_estadistica_de_diccionario_a_texto(
        jugador_estadistica_dicc)
    print_dato(cadena)

#8

#9

# 10 

def jugadores_mayores_al_ingresado(
    lista_jugadores: list[dict], clave_estadistica, 
    clave_interior_estadistica)-> list[dict]:
    '''
    Permite ingresar un valor y busca los que superan ese valor.
    Recibe: (arg 1) la lista de jugadores, (arg 2) clave dicc estadisticas.
    (ej: clave_dicc_ext ="estadisticas")
    (arg 3) la clave dentro del dicc estadisticas (ej "promedio_puntos_por_partido")) 
    '''
    nueva_lista_Jugadores = []
    mensaje_a_mostrar = "Ingrese un valor numérico: "
    numero_ingresado = pedir_ingreso_de_numero(r"^[0-9]+|\.[0-9]+$", mensaje_a_mostrar)
    encontrado = False
    
    for jugador in lista_jugadores:
        if jugador[clave_estadistica][clave_interior_estadistica] > numero_ingresado:
            nueva_lista_Jugadores.append(jugador)
            encontrado = True
    if encontrado == False:
        print("Nadie cumple con la condicion")
    else:
        return nueva_lista_Jugadores
    
def mostrar_estadisticas_jugadores(
    lista_jugadores : list[dict], clave_interior_estadistica: str):
    '''
    Muestra las estadisticas de los jugadores.
    Recibe (arg 1) la lista de jugadores. y (arg 2) la clave del dicc 
    ej("estadisticas").
    Retorna - no aplica
    '''
    clave_interior_estadistica_guion = \
        clave_interior_estadistica.replace("_"," ").capitalize()
    for jugador in lista_jugadores:
        nombre = jugador["nombre"]
        valor_estadistica = jugador["estadisticas"][clave_interior_estadistica]
        print("{0}: {1}: {2}".format(
            nombre, clave_interior_estadistica_guion, valor_estadistica))
        
        
def mostrar_jugadores_mayores_al_ingresado(
    lista_jugadores : list[dict], clave_estadistica = "estadisticas", 
    clave_interior_estadistica = "promedio_puntos_por_partido"):
    '''
    Permite ingresar un valor y busca los que superan ese valor,
    ademas de mostrarlos por consola.
    Recibe: (arg 1) una lista de jugadores,(arg 2) clave de estadistica "estadisticas" ,
    (arg 3) clave del dicc estadisticas. ejemplo: "promedio_puntos_por_partido".
    Devuelve - no aplica
    '''
    lista_jugadores_obtenida = jugadores_mayores_al_ingresado(
        lista_jugadores, clave_estadistica, clave_interior_estadistica)
    if(lista_jugadores_obtenida):
        mostrar_estadisticas_jugadores(lista_jugadores_obtenida, 
                                       clave_interior_estadistica)
    else:
        return False
    
    
#11
#12
#13
#14
#15
#16


def quitar_el_emenos_habil_segun_clave_estadistica(
    lista_jugadores : list[dict], clave_estadisticas = "estadisticas",
    clave_interior_estadistica = "promedio_puntos_por_partido")-> list[dict]:
    '''
    De la lista quita el menos habil segun estadistica.
    Recibe: (arg 1) la lista de jugadores, (arg 2) la clave "estadistica",
    (arg 3) la clave de la estadistica a evaluar. ejemplo :
    "promedio_puntos_por_partido".
    Devuelve una nueva lista de jugadores sin el mas habil.
    '''
    indice_jugador_menos_habil = calcular_max_min_estadisticas(
        lista_jugadores, clave_estadisticas, clave_interior_estadistica, maximo= False)
    nueva_lista_jugadores = []
    for indice in range(len(lista_jugadores)):
        if(indice != indice_jugador_menos_habil):
            nueva_lista_jugadores.append(lista_jugadores[indice])
    return nueva_lista_jugadores


def calcular_y_mostrar_el_promedio_de_puntos_del_dream_team_sin_el_menos_habil(
    lista_jugadores : list[dict], clave_estadisticas = "estadisticas", 
    clave_interior_estadistica = "promedio_puntos_por_partido"):
    '''
    Calcula y muestra el promedio de puntos del dream team sin incluir al 
    menos habil segun estadistica.
    Recibe (arg 1) la lista de jugadores, (arg 2): clave :"estadisticas", 
    (arg 3) la clave de la estadistica a evaluar. ej: "promedio_puntos_por_partido".
    Devuelve - no aplica
    '''
    nueva_lista_sin_el_menos_habil = quitar_el_emenos_habil_segun_clave_estadistica(
        lista_jugadores, clave_estadisticas, clave_interior_estadistica)
    calcular_y_mostrar_el_promedio_de_puntos_del_dream_team(nueva_lista_sin_el_menos_habil)
    
 
 
 
 
  
#--Menú y ejecucion de la app
def opciones_del_menu()-> str:
    '''
    Opciones del menu.
    Recibe: No aplica.
    Devuelve: una cadena str .
    '''
    opciones = "Bienvenido:\n" \
           "1- Ver Jugadores y Posición de todos los jugadores del Dream Team\n" \
           "2- Seleccionar un jugador para ver sus estadísticas (Opcional: guardar)\n" \
           "3- Guardar estadísticas del jugador seleccionado anteriormente.\n" \
           "4- Buscar un jugador por su nombre para ver sus logros\n" \
           "5- Ver el promedio de puntos por partido de todo el equipo del Dream team\n"\
           "6- Ver si el jugador ingresado pertenece al salon de la fama\n" \
           "7- Ver el jugador con la mayor cantidad de rebotes totales\n" \
           "8- Ver el jugador con el mayor porcentaje de tiros de campo\n" \
           "9- Ver el jugador con el mayor cantidad de asistencias totales\n"\
           "10- Ver los jugadores que tienen el promedio de más puntos por partido que el valor ingresado.\n"\
           "11- Ver los jugadores que tienen el promedio de mas rebotes por partido que el valor ingresado.\n"\
           "12- Ver los jugadores que tienen el promedio asistencias por partido mayor que el valor ingresado.\n"\
           "13- Ver el jugador con la mayor cantidad de robos totales\n"\
           "14- Ver el jugador con la mayor cantidad de bloqueos totales\n"\
           "15- Ver los jugadores que tienen el porcentaje de tiros libres superior al valor ingresado.\n"\
           "16- Ver el promedio de puntos por partido del equipo excluyendo al jugador con la menor puntos\n"\
               
               
    ''        
    return opciones

def print_dato(dato : str)->None:
    '''
    Imprime una cadena de texto.
    Recibe una cadena.
    Devuelve: No aplica.
    '''
    print("{0}".format(dato))
    

def menu_principal()-> int:
    '''
    Imprime el menu y toma una opcion del usuario
    recibe -no aplica
    devuelve la opcion elegida, en caso de False devuelve -1
    '''
    opciones_para_el_usuario = opciones_del_menu()
    print_dato(opciones_para_el_usuario)
    mensaje_a_mostrar = "Por favor ingrese una opcion: "
    numero_ingresado = pedir_ingreso_de_numero(r"^[0-9]+$", mensaje_a_mostrar)
    return numero_ingresado
   
   
def aplicacion(lista_Jugadores : list[dict])-> None:
    '''
    Opciones para el usuario
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
                indice_elegido = mostrar_estadisticas_del_jugador_elegido(
                    lista_Jugadores)
                flag_guardar_estadisticas = True
            case 3:
                if(flag_guardar_estadisticas):
                    guardar_estadisticas_del_jugador_elegido(
                        lista_Jugadores, indice_elegido)
                else:
                    print("Pase por el punto 2 primero")
            case 4:
                buscar_jugador_y_ver_sus_logros(
                    lista_Jugadores)
            case 5:
                calcular_y_mostrar_el_promedio_de_puntos_del_dream_team(
                    lista_Jugadores)
            case 6:
                buscar_jugador_y_ver_logro(lista_Jugadores)
            case 7:
                calcular_y_mostrar_jugador_mayor_estadistica(
                    lista_Jugadores, clave_interior_estadistica = "rebotes_totales")
            case 8:
                calcular_y_mostrar_jugador_mayor_estadistica(
                    lista_Jugadores, clave_interior_estadistica = "porcentaje_tiros_de_campo")
            case 9:
                calcular_y_mostrar_jugador_mayor_estadistica(
                    lista_Jugadores, clave_interior_estadistica = "asistencias_totales")
            case 10:
                mostrar_jugadores_mayores_al_ingresado(
                    lista_Jugadores, clave_interior_estadistica="promedio_puntos_por_partido")
            case 11:
                mostrar_jugadores_mayores_al_ingresado(
                    lista_Jugadores, clave_interior_estadistica="promedio_rebotes_por_partido")
            case 12:
                mostrar_jugadores_mayores_al_ingresado(
                    lista_Jugadores, clave_interior_estadistica="promedio_asistencias_por_partido")
            case 13:
                calcular_y_mostrar_jugador_mayor_estadistica(
                    lista_Jugadores, clave_interior_estadistica = "robos_totales")
            case 14:
                calcular_y_mostrar_jugador_mayor_estadistica(
                    lista_Jugadores, clave_interior_estadistica = "bloqueos_totales")
            case 15:
                mostrar_jugadores_mayores_al_ingresado(
                    lista_Jugadores, clave_interior_estadistica="porcentaje_tiros_libres")
            case 16:
                    calcular_y_mostrar_el_promedio_de_puntos_del_dream_team_sin_el_menos_habil(
                        lista_Jugadores, clave_interior_estadistica="promedio_puntos_por_partido")
            case 17:
                pass
            case 18:
                pass
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