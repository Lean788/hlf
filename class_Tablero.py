import numpy as np
import variables as var
import random

class Tablero():
    def __init__(self, dimension, barcos=[]):
        self.dimension = dimension
        self.matrix = np.full((dimension,dimension), var.AGUA_SIMB)
        self.barcos = barcos

    def casilla_random(self):
        fila_random = random.randint(0,9)
        columna_random = random.randint(0,9)
        casilla_random = (fila_random, columna_random)
        return casilla_random


    def generar_b_aleatorio(self):
        
        for barcos_prop in var.LISTA_BARCOS:
            contador = 0
            while contador < barcos_prop [1]:
                posicion = self.casilla_random()
                fila = self.casilla_random()[0]
                columna = self.casilla_random()[1]

                orien_norte = self.matrix[fila: fila - barcos_prop[0]:-1, columna]
                orien_sur = self.matrix[fila: fila + barcos_prop[0], columna]
                orien_oeste = self.matrix[fila, columna:columna - barcos_prop[0]:-1]
                orien_este = self.matrix[fila, columna: columna + barcos_prop[0]]

                if var.BARCO_SIMB not in orien_norte and len(orien_norte) == barcos_prop[0]:
                    self.matrix[fila: fila - barcos_prop[0]: -1, columna] = var.BARCO_SIMB
                    contador += 1
                elif var.BARCO_SIMB not in orien_sur and len(orien_sur) == barcos_prop[0]:
                    self.matrix[fila: fila + barcos_prop[0], columna] = var.BARCO_SIMB
                    contador += 1
                elif var.BARCO_SIMB not in orien_oeste and len(orien_oeste) == barcos_prop[0]:
                    self.matrix[fila, columna:columna - barcos_prop[0]:-1] = var.BARCO_SIMB
                    contador += 1
                elif var.BARCO_SIMB not in orien_este and len(orien_este) == barcos_prop[0]:
                    self.matrix[fila, columna: columna + barcos_prop[0]] = var.BARCO_SIMB
                    contador += 1

        
    def mostrar_tablero(self):

        return self.matrix

    def colocar_barco(self, barco):
        fila = barco.posicion[0] - 1
        columna = var.coord_letras.index(barco.posicion[1])

        if barco.axis == 0:
            self.matrix[fila: barco.eslora + fila, columna] = var.BARCO_SIMB
        else:
            self.matrix[fila, columna: barco.eslora + columna] = var.BARCO_SIMB

    def colocar_barcos(self):
        for barco in self.barcos:
            self.colocar_barco(barco)
