lista_a_ordenar = [{'nombre': 'Michael Jordan', 'puntos_totales': 32292},
                   {'nombre': 'Magic Johnson', 'puntos_totales': 17707}, 
                   {'nombre': 'Larry Bird', 'puntos_totales': 21791}, 
                   {'nombre': 'Charles Barkley', 'puntos_totales': 23757},
                   {'nombre': 'Scottie Pippen', 'puntos_totales': 18940}, 
                   {'nombre': 'David Robinson', 'puntos_totales': 20790}, 
                   {'nombre': 'Patrick Ewing', 'puntos_totales': 24815}, 
                   {'nombre': 'Karl Malone', 'puntos_totales': 36928}, 
                   {'nombre': 'John Stockton', 'puntos_totales': 19711}, 
                   {'nombre': 'Clyde Drexler', 'puntos_totales': 22195},
                   {'nombre': 'Chris Mullin', 'puntos_totales': 17911}, 
                   {'nombre': 'Christian Laettner', 'puntos_totales': 4956}]

def ordenar_lista_dicc_bubble_sort(
    lista_original : list[dict], clave = "puntos_totales", orden = "asc")-> list | int:
    '''
    Ordena los elementos de una lista de jugadores segun clave.
    Recibe: (arg 1) una lista de jugadores, (arg2) una clave ej:("nombre"),
    (arg 3) el orden( "asc" o "desc").
    Devuelve: una lista de nombres ordenada alfabeticamente. list[dict]
    o -1 si la lista esta vacia.
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
                if lista[indice][clave] < lista[indice + 1][clave] and orden == "desc":
                    lista[indice], lista[indice + 1] = lista[indice + 1], lista[indice]
                    flag_swap = True
        len_lista -= 1
        return lista
    else:
        print("La lista está vacia")
        return -1


lista_ordenada = ordenar_lista_dicc_bubble_sort(lista_a_ordenar, clave="puntos_totales",orden="desc")
# for item in lista_ordenada:
#     print(item)
    


# {'nombre': 'Christian Laettner', 'puntos_totales': 4956}
# {'nombre': 'Magic Johnson', 'puntos_totales': 17707}
# {'nombre': 'Chris Mullin', 'puntos_totales': 17911}
# {'nombre': 'Scottie Pippen', 'puntos_totales': 18940}
# {'nombre': 'John Stockton', 'puntos_totales': 19711}
# {'nombre': 'David Robinson', 'puntos_totales': 20790}
# {'nombre': 'Larry Bird', 'puntos_totales': 21791}
# {'nombre': 'Clyde Drexler', 'puntos_totales': 22195}
# {'nombre': 'Charles Barkley', 'puntos_totales': 23757}
# {'nombre': 'Patrick Ewing', 'puntos_totales': 24815}
# {'nombre': 'Michael Jordan', 'puntos_totales': 32292}
# {'nombre': 'Karl Malone', 'puntos_totales': 36928}


contador = 1
for item in lista_ordenada:
    print(f"Ranking #{contador}: {item['nombre']} - Puntos totales: {item['puntos_totales']}")
    contador += 1
