import math
import random
from fuente import generaPalabra

# Calcula el vector estacionario de una cadena de Markov dada su matriz de transición
# La matriz de transición es una lista de listas, donde cada sublista representa las probabilidades
# en una cadena de markov si dejas pasar suficiente tiempo, el sistema tiende a estabilizarse en un "equilibrio" donde las probabilidades de estar en cada estado
# ya no cambian, aunque el sistema siga saltando de un estado a otro. Este equilibrio se representa con el vector estacionario.
# inicializa el vector estacionario
# el codigo simula el paso del tiempo multiplicando el vector estacionario por la matriz de transición repetidamente
# el algoritmo termina cuando el cambio entre iteraciones es menor que 1e-10 o si se alcanzan las 10000 iteraciones
def vectorEstaconario(matriz):
    n = len(matriz)
    pi = [1.0/n] * n
    for _ in range(10000):
        nuevo_pi = [0.0] * n #nuevo_pi va a tener 0s en todas sus posiciones
        for i in range(n):
            for j in range(n):
                nuevo_pi[j] += pi[i] * matriz[i][j]
        diff = sum(abs(nuevo_pi[i] - pi[i]) for i in range(n))
        pi = nuevo_pi
        if(diff < 1e-10):
            break
    s = sum(pi)
    pi = [x/s for x in pi]
    return pi





# Dada una cadena de caracteres que representa un mensaje emitido por una fuente, devuelve una lista con su alfabeto y su matriz de transición.
# "Si estoy en la letra 'a', hay un X% de probabilidad de que la siguiente sea una 'n'"
# recorre la cadena y extrae el alfabeto
# cuenta las transiciones desde a hasta b, acumulando la probabilidad en la matriz
# se normalizan las filas de la matriz para que sumen 1
def generaMat(cadena):
    alfabeto = []
    for i in cadena:
        if(i not in alfabeto):
            alfabeto.append(i)
    n = len(alfabeto)

    mat = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(len(cadena)-1):
        a = cadena[i]
        b = cadena[i+1]
        mat[alfabeto.index(a)][alfabeto.index(b)] += 1

    mat = [[mat[i][j]/(sum(mat[i]) if sum(mat[i]) > 0 else 1) for j in range(n)] for i in range(n)]

    return alfabeto, mat





# Genera una palabra de longitud dada a partir de un alfabeto y sus matriz de transición
# Elige el primer símbolo del mensaje al azar, busca en la matriz la fila correspondiente a la letra actual. Esa fila contiene las probabilidades condicionales específicas para el siguiente paso.
# Si llegamos a un estado "pozo" (un símbolo que apareció al final del texto de entrenamiento pero nunca en el medio, por lo que no tiene transiciones salientes), la suma de su fila sería 0.
# Para evitar que el programa falle, le asigna probabilidades uniformes ([1/n, 1/n...]) para poder saltar a cualquier otro lado y seguir generando texto
# Llama a una función auxiliar (presumiblemente similar a random.choices o la anterior generaMensaje) pasándole las probabilidades dinámicas de esa fila específica.


def generaPalabra2(alfabeto, mat, longitud):
    n = len(alfabeto)
    palabra = ""
    letra = random.choices(alfabeto, k = 1)[0]
    palabra = palabra + letra
    for i in range(longitud - 1):
        prob = mat[alfabeto.index(letra)]
        if(sum(prob) == 0):
            prob = [1/n] * n
        letra = generaPalabra(alfabeto, prob, 1)[0]
        palabra = palabra + letra
    return palabra






# Comprueba si una matriz de transición corresponde a una fuente de memoria nula
# determina si la fuente, aunque esté modelada como Markov, en realidad se comporta como una Fuente de Memoria Nula
# Fuente con Memoria: Las filas son distintas. Saber dónde estás (i) cambia las probabilidades de a dónde vas (j).
# Fuente de Memoria Nula: Todas las filas son idénticas. No importa en qué estado estuvieras antes (si en i o en k), la probabilidad de que salga el símbolo j es siempre la misma. El pasado no influye en el futuro
def esMemoriaNula(matriz, tolerancia):
    fila = matriz[0]
    i = 0
    verifica = True
    while(i < len(matriz) and verifica):
        j = 0
        while(j < len(matriz[i]) and verifica):
            if(abs(matriz[i][j] - fila[j]) > tolerancia):
                verifica = False
            j += 1
        i += 1
    return verifica




def printMat(matriz):
    i = len(matriz)
    j = len(matriz[0])
    for x in range(i):
        for y in range(j):
            print(f"{matriz[y][x]:.4f}", end=" ")
        print()



alf, mat = generaMat("-+-+*//++///*/-////+---////-+/+--+-+/-/+-+/-+*++//")
print(alf)
printMat(mat)