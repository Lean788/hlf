from class_Tablero import *
import variables as var
import numpy as np

class Jugador():
    
    def __init__(self):
        self.tablero_barcos = Tablero(10)
        self.tablero_barcos.generar_b_aleatorio()
        self.tablero_disparos = Tablero(10)
        self.vidas = 20
        self.disparos = []

    def muestra_tablero(self):
        eje_x = np.array(var.LISTA_EJE_X)
        print("  ",eje_x, "           ",eje_x,"\n")
        for i in range(len(var.LISTA_EJE_Y)):
            if i!= 9:
                eje_y = str(var.LISTA_EJE_Y[i]) + " "
            else:
                eje_y = str(var.LISTA_EJE_Y[i])

            print(eje_y, self.tablero_barcos.matrix[i],
            "        ", eje_y, self.tablero_disparos.matrix[i])
    
    def disparar(self, posicion, objetivo):

        self.disparos.append(posicion)

        posicion_interpretada = self.interpretar_posicion(posicion)

        if objetivo.tablero_barcos.matrix[posicion_interpretada[0], posicion_interpretada[1]] == var.BARCO_SIMB:
            self.tablero_disparos.matrix[posicion_interpretada[0], posicion_interpretada[1]] = var.TOCADO_SIMB
            objetivo.tablero_barcos.matrix[posicion_interpretada[0], posicion_interpretada[1]] = var.TOCADO_SIMB
            objetivo.vidas -= 1
            return True
        else:
            self.tablero_disparos.matrix[posicion_interpretada[0], posicion_interpretada[1]] = var.FALLAR_SIMB
            objetivo.tablero_barcos.matrix[posicion_interpretada[0], posicion_interpretada[1]] = var.FALLAR_SIMB
            return False

    def interpretar_posicion(self, posicion):
        fila = posicion[0] - 1
        columna = var.LISTA_EJE_X.index((posicion[1]))

        return (fila, columna)