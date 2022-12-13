import random
import numpy as np
import variables as var
from pyfiglet import Figlet
import os
from time import sleep


def posicion_aleatoria():
    fila = random.randint(1,10)
    columna = var.LISTA_EJE_X[random.randint(0,9)]

    return (fila, columna)

def validar_entrada(jugador, posicion):
    entrada = None
    try:
        if len(posicion) == 3:
            if int(posicion[:2]) == 10 and posicion[2].upper() in var.LISTA_EJE_X:
                entrada = (int(posicion[:2]),posicion[2].upper())
        elif len(posicion) == 2:
            if int(posicion[0]) > 0 and int(posicion[0]) < 10 and posicion[1].upper() in var.LISTA_EJE_X:
                entrada = (int(posicion[0]), posicion[1].upper())
        elif posicion == "0":
            entrada = 0
        if entrada in jugador.disparos:
            print("Ya has disparado en esta coordenada")
            entrada = None
        
        return entrada
    except: return None

def conteo_vidas():
    conteo_vida = []
    for vidas in var.LISTA_BARCOS:
        conteo_vida.append(vidas[0]*vidas[1])
    return sum(conteo_vida)

def intro():
    f = Figlet(font='slant')
    word = 'Hunde la Flota !'
    curr_word = ''
    for char in word:
        os.system('reset') #assuming the platform is linux, clears the screen
        curr_word += char;
        print(f.renderText(curr_word))
        sleep(0.15)

def instrucc():
    print("Bienvenido al juego de Hunde la Flota!\n\nEl juego tradicional de estrategia y algo de suerte, que involucra a dos participantes, el usuario (jugador 1) y la CPU: Skynet.\n")

    sleep(0.5)

    print("Los jugadores manejan un tablero de oceano y un tablero de tiro; cada uno divididos en casillas.\nCada tablero representa una zona diferente del mar abierto: la propia y la contraria. \nEn el primer tablero, el jugador coloca sus barcos y registra los disparos del oponente; en el otro,\n se registran los tiros propios contra el otro jugador, diferenciando los impactos y los que dan al agua.\n Al tiempo, se deduce la posicion de los barcos del contrincante.\n")

    sleep(0.5)

    print("Los espacios vacios ' ' hacen referncia al agua")

    sleep(0.5)

    print("El símbolo 'O' hacen referncia a una eslora de uno de tus barcos")

    sleep(0.5)

    print("El símbolo '-' hace referencia a un disparo fallido")

    sleep(0.5)

    print("El símbolo 'X' hace referencia a un barco tocado")

    sleep(0.5)

    print("¡COMENCEMOS!\n")