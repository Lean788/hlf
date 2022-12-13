import os
from time import sleep
import variables as var
from class_Jugador import *
from functions import validar_entrada, posicion_aleatoria, intro, instrucc

intro()

instrucc()

input("Presiona enter para continuar\n\n")


while var.jugador1.vidas > 0 and var.Skynet.vidas > 0:
    if not var.es_Skynet:
        var.jugador1.muestra_tablero()
        print("\n")
        # var.Skynet.muestra_tablero()   
        # print("\n")
        
        while var.game_started:
            print("=========================================")
            print("\n")
            print("SALIR = 0")
            posicion = input("Introduzca la coordenada donde quiera disparar, indicando número y letra, seguidos y sin espacio (Por ejemplo: 3a, 5d, etc.): ")
            print("\n")
            print("=========================================")
            print("\n")

            posicion_validada = validar_entrada(var.jugador1,posicion)

            if posicion_validada != None:
                break
            else: 
                print("Entrada no válida, vuelva a intentarlo \n")
                print("\n")
        
        if posicion_validada == 0:
            var.salir = True
            break

        resultado = var.jugador1.disparar(posicion_validada,var.Skynet)

        if resultado:
            var.es_Skynet = False
            
            if var.Skynet.vidas != 0:
                print("¡HAS ACERTADO! Vuelve a disparar nuevamente \n\n")

        else: 
            print("No has acertado, es el turno de Skynet: ")
            print("\n")
            var.es_Skynet = True
            sleep(1)
        
    else: 
        print("=========================================")
        print("\n")
        print("Turno de Skynet ")
        print("\n")
        print("=========================================")
        print("\n")

        sleep(1)

        apuntar = False

        while not apuntar:
            posicion_validada = posicion_aleatoria()

            if not posicion_validada in var.Skynet.disparos:
                apuntar = True

        print("Skynet está apuntando a: ", posicion_validada,"\n")

        resultado = var.Skynet.disparar(posicion_validada, var.jugador1)

        sleep(2.75)

        if not resultado: 
            print("Skynet no ha acertado, es tu turno: ")
            print("\n")
            print("=========================================")
            print("\n")
            sleep(1)
            var.es_Skynet = False

        else:
            print("Skynet ha acertado, le toca tirar de nuevamente\n")

            var.es_Skynet = True

            sleep (1)
    
if var.es_Skynet and not var.salir:
    print("=========================================")
    print("\n")
    print("Skynet ha ganado... Eres un paquete, vuelve a intentarlo!")
    print("\n")
    print("=========================================")
    print("\n")
elif not var.es_Skynet and not var.salir:
    print("=========================================")
    print("\n")
    print("¡HAS GANADO! Sarah Connor estaría orgullosa de ti")
    print("\n")
    print("=========================================")
    print("\n")
elif var.salir:

    print("Fin del juego")