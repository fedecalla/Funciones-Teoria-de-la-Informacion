import math
import random
from fuente import generaPalabra

# Calcula el vector estacionario de una cadena de Markov dada su matriz de transición
# La matriz de transición es una lista de listas, donde cada sublista representa las probabilidades
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