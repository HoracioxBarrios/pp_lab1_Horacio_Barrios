import json

def leer_archivo_json(nombre_path : str)-> list:
    '''
    Lee un archvo json.
    Recibe la ruta con el nombre de archivo .json.
    Devuelve una lista de jugadores
    '''
    with open(nombre_path, "r") as archivo:
        equipo = json.load(archivo)
    
        return equipo["jugadores"]
    
    
lista_jugadores = leer_archivo_json("parcial\dt.json")

'''
1) Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
 Nombre Jugador- Posición. Ejemplo:
 Michael Jordan- Escolta
'''
def mostrar_nombres_posicion_o_tambien_ubicacion(
    lista_de_jugadores: list , ver_indice_ubi = False):
    '''
    Muestra los nombres, posicion de cada jugador y opcionalmente su indice.
    Recibe: una lista de jugadores y opcional elegir ver el indice 
    donde esta cada jugador (ver_indice = True).

    Devuelve: -1 en caso de error
    '''
    if(lista_de_jugadores):
        if(ver_indice_ubi):
            for indice in range(len(lista_de_jugadores)):
                dato_jugador = "Ubicacion {0}: {1}- {2}".format(
                    indice, lista_de_jugadores[indice]["nombre"], 
                    lista_de_jugadores[indice]["posicion"])
                print(dato_jugador)
        else:
            for indice in range(len(lista_de_jugadores)):
                dato_jugador = "{0}- {1}".format(
                    lista_de_jugadores[indice]["nombre"],
                    lista_de_jugadores[indice]["posicion"])
                print(dato_jugador)
    else:
        print("La lista está vacia")
        return -1

mostrar_nombres_posicion_o_tambien_ubicacion(lista_jugadores)


