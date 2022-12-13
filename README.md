# Hundir la Flota - 1º proyecto entregable - [The Bridge]
## _Descripción_

Juego de hundir la flota, desarrollado en Python, aplicando conocimientos en Numpy.

## Tech

For this project I have required the following technologies:

- [Numpy](https://numpy.org/doc/stable/)
- [Python](https://devguide.python.org/)
- [Git](https://git-scm.com/doc)

## Main
En este archivo se ejecuta el programa del juego. Contiene la lógica principal del juego.
## Functions
Recoge las funciones que se implementan en el juego, archivo desde el cual se puede hacer uso de las mismas desde los distintos archivos que lo requieran. Consta de algunas funciones creadas, tales como:

* `posicion_aleatoria()`: crea una posición en un tablero de 10 x 10 de número-letra. Nos devuelve una tupla (fila, columna).
* `validar_entrada()`: se le pasa como parámetros un jugador y una posición. este método comprueba la validez del disparo, no debe de haber disparado en esa misma posición y discrimina entradas que no sean válidas por error de sintáxis o fuera de rango. Utiliza métodos para no tener en cuenta mayúsculas y minúsculas.
* Hay otras funciones como `conteo_vidas()` que no se implementan en esta versión del juego, y encapsulaciones de la introducción, con las explicaciones del juego e instrucciones, en `intro()` e `instrucc()`

## Clase Jugador
Se plantean dos tableros, uno para los barcos propios y otro para mostrar los disparos y posiciones enemigas. Presenta una propiedad de vidas que representa el número de disparos que hay que hacer para hundir todos los barcos (es decir, el total de esloras), y una lista de disparos, que almacena los disparos que ha realizado el jugador.

### Métodos:
* `muestra_tablero()`: Imprime los dos tableros propiedad del jugador, intentando que sea lo más representativo posible.
* `disparar()`: Se pasa como parámetros la posición a donde se dispara y el objetivo, es decir, a qué jugador se dispara. Comprueba si se ha acertado y en ese caso resta la variable vida del jugador afectado
* `interpretar_posicion()`: Se pasa como parámetro la posición que escoge el jugador en su turno, y se interpreta para que pueda ser representado en la matriz.

## Clase Tablero
Se crea una estructura de tablero, el recibirá como parámetros la dimensión del mismo, así como también recibirá el objeto barcos (lista) que serán ubicados en el tablero de manera aleatoria, a través de los métodos `random.randit()` entre otras implementaciones.

### Métodos:
* `casilla_random()`: crea una posición dentro del tablero de forma aleatoria, devolviendo una tupla (fila_random, columna_random)
* `genera_b_aleatorio()`: Genera y colocar todos los barcos de forma aleatoria. En esta parte sobre todo se implementan conocimientos de slicing. 
* `mostrar_tablero()`: Imprime la matriz del juego.
* `colocar_barco()`: Sirve para colocar un barco en una posición dada. (no se implementa en esta versión)
* `colocar_barcos()`: Se encargaría de colocar los barcos de la función anterior, de igual manera, no se llegan a implementar en esta versión.

## Variables

Aquí mostramos los valores que permanecerán constantes durante la ejecución del juego. 

##### game_started = True 
Nos indica que el juego está en progreso

##### BARCO_SIMB= "O"
Representa una eslora de un barco

##### AGUA_SIMB = " "
Representa el mar (agua)

##### TOCADO_SIMB = "X"
Representa una eslora tocada (golpeada)

##### FALLAR_SIMB = "-"
Representa un disparo fallido (disparo al agua)

##### LISTA_BARCOS = [(4, 1), (3, 2), (2, 3), (1, 4)] 
Por cada tupla, el primer valor corresponde a las esloras, y el segundo al número de barcos.

##### coord_letras = "ABCDEFGHIJ"
Nos servirá como referencia para leer la posición donde se desea disparar, utilizado en la función `colocar_barco(barco)`

##### LISTA_EJE_X = ['A','B','C','D','E','F','G','H','I','J']
El eje de abscisas, comúnmente representado con "x" y que corresponde al eje horizontal, es decir, las filas.

##### LISTA_EJE_Y = [1,2,3,4,5,6,7,8,9,10]
El eje de ordenadas, comúnmente representado con "y" y que corresponde al eje vertical, es decir, las columnas.

##### es_Skynet = False
Nos sirve para identificar cuando es el turno de la CPU.

##### salir = False
Salir del juego, por defecto False, pero si el usuario lo solicita, pasará a True.

##### jugador1 = Jugador()
Jugador usuario.

##### Skynet = Jugador()
Jugador CPU.

##### vidas = conteo_vidas()
variable que no se implementa en esta versión del juego, pero que corresponde a una función creada para que las vidas se adapten al número de barcos (y por ende, de esloras) que tengan, en caso de modificarse en el juego. 



## Observations
For this practice I have followed the instructions and steps learned during the lessons at the academy and the instructions and advice provided by the tutor and teachers assistances.



[The Bridge]:<https://www.thebridge.tech/>

