
from pacial import (menu_principal, 
                     mostrar_nombres_posicion_o_ubicacion, 
                     mostrar_estadisticas_del_jugador_elegido,
                     guardar_estadisticas_del_jugador_elegido,
                     buscar_jugador_y_ver_sus_logros,
                     calcular_y_mostrar_el_promedio_de_puntos_del_dream_team,
                     buscar_jugador_para_ver_logro,
                     calcular_y_mostrar_jugador_mayor_estadistica,
                     mostrar_jugadores_mayores_al_ingresado,
                     calcular_y_mostrar_el_promedio_de_puntos_del_dream_team_sin_el_menos_habil,
                     calcular_jugador_con_mas_logros,
                     mostrar_estadistica_ordenado_por_posicion,
                     ordenar_y_guardar_ranking_de_jugadores,
                     calcular_y_mostrar_posiciones_cantidad,
                     ordenar_por_cantidad,
                     clear_console,
                     leer_archivo_json)
                    

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
                buscar_jugador_para_ver_logro(lista_Jugadores)
            case 7:
                calcular_y_mostrar_jugador_mayor_estadistica(
                    lista_Jugadores, 
                    clave_interior_estadistica = "rebotes_totales")
            case 8:
                calcular_y_mostrar_jugador_mayor_estadistica(
                    lista_Jugadores, 
                    clave_interior_estadistica = "porcentaje_tiros_de_campo")
            case 9:
                calcular_y_mostrar_jugador_mayor_estadistica(
                    lista_Jugadores, 
                    clave_interior_estadistica = "asistencias_totales")
            case 10:
                mostrar_jugadores_mayores_al_ingresado(
                    lista_Jugadores, 
                    clave_interior_estadistica = "promedio_puntos_por_partido")
            case 11:
                mostrar_jugadores_mayores_al_ingresado(
                    lista_Jugadores, 
                    clave_interior_estadistica = "promedio_rebotes_por_partido")
            case 12:
                mostrar_jugadores_mayores_al_ingresado(
                    lista_Jugadores, 
                    clave_interior_estadistica = "promedio_asistencias_por_partido")
            case 13:
                calcular_y_mostrar_jugador_mayor_estadistica(
                    lista_Jugadores, 
                    clave_interior_estadistica = "robos_totales")
            case 14:
                calcular_y_mostrar_jugador_mayor_estadistica(
                    lista_Jugadores, 
                    clave_interior_estadistica = "bloqueos_totales")
            case 15:
                mostrar_jugadores_mayores_al_ingresado(
                    lista_Jugadores, 
                    clave_interior_estadistica = "porcentaje_tiros_libres")
            case 16:
                    calcular_y_mostrar_el_promedio_de_puntos_del_dream_team_sin_el_menos_habil(
                        lista_Jugadores, 
                        clave_interior_estadistica = "promedio_puntos_por_partido")
            case 17:
                calcular_jugador_con_mas_logros(lista_Jugadores, maximo = True)
            case 18:
                mostrar_jugadores_mayores_al_ingresado(
                    lista_Jugadores, 
                    clave_interior_estadistica = "porcentaje_tiros_triples")
            case 19:
                calcular_y_mostrar_jugador_mayor_estadistica(
                    lista_Jugadores, clave_interior_estadistica = "temporadas")
            case 20:
                mostrar_estadistica_ordenado_por_posicion(lista_Jugadores)
            case 21:
                print("No está dispinible esta opcion")
            case 22:
                print("No está dispinible esta opcion")
            case 23:
                ordenar_y_guardar_ranking_de_jugadores(lista_Jugadores)
            case 24:
                calcular_y_mostrar_posiciones_cantidad(lista_Jugadores, clave="posicion")
            case 25:
                ordenar_por_cantidad(lista_Jugadores)
            case 26:
                pass
            case _:
                print("Opcion incorrecta, por favor intente nuevamente.")
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