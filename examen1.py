import math
import random
import itertools

#GENERA ALFABETO Y PROBABILIDADES A PARTIR DE UNA CADENA
def generaAlfabeto(cadena):
    alfabeto = []
    probabilidades = []
    for i in range(0, len(cadena)):
        if(cadena[i] in alfabeto):
            probabilidades[alfabeto.index(cadena[i])] = probabilidades[alfabeto.index(cadena[i])] + 1/len(cadena)
        else:
            alfabeto.append(cadena[i])
            probabilidades.append(1/len(cadena))    
    return alfabeto, probabilidades


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

def entropiaFuente(probabilidades, informaciones):
    ent = 0
    for i in range(0, len(probabilidades)):
       ent = ent + probabilidades[i] * informaciones[i] 
    return ent

def printMat(matriz):
    i = len(matriz)
    j = len(matriz[0])
    for x in range(i):
        for y in range(j):
            print(f"{matriz[y][x]:.4f}", end=" ")
        print()

#INFORMACION DE UNA FUENTE
def informacionFuente(probabilidades):
    inf = [math.log2(1/p) for p in probabilidades]
    return inf

#EXTENSION DE ORDEN N
def extension(alfabeto, probabilidades, orden):
    cartesianos = list(itertools.product(alfabeto, repeat = orden)) #Generamos una lista de productos cartesianos
    probab = []
    ext = []    
    for prod in cartesianos: #Para cada producto cartesiano:
        prob = 1
        caracter = ""
        for simbolo in prod: #Para cada elemento del producto cartesiano:
            caracter = caracter + str(simbolo) # Se genera la cadena de caracteres
            prob = prob * probabilidades[alfabeto.index(simbolo)] # Se calcula la probabilidad
        probab.append(prob) # Se aniade a la lista de probabilidades
        ext.append(caracter) # Se aniade a la lista de cadenas
    return ext,probab


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


def entropiaFuenteMarkov(matriz, vectorEstacionario):
    n = len(matriz)
    ent = 0.0
    for i in range(n):
        sum1 = 0
        for j in range(n):
            if(matriz[i][j] != 0):
                sum1 = sum1 + matriz[i][j] * math.log2(1/matriz[i][j])
        ent += sum1 * vectorEstacionario[i]
    return ent



mensaje1 = "+-/+/-//-/*-/**-*---////-+--*+*/-----/--+/++--*/-+"

alfabeto1, probabilidades1 = generaAlfabeto(mensaje1)
alfabeto1, matriz1 = generaMat(mensaje1)
memoriaNula1 = esMemoriaNula(matriz1, 0.01)
informacion1 = informacionFuente(probabilidades1)
entropia1 = entropiaFuente(probabilidades1, informacion1)
extension1, probextension1 = extension(alfabeto1, probabilidades1, 2)
entropiaExtension = entropiaFuente(probextension1, informacionFuente(probextension1))

print("\n \n \n------------ PRIMERA PALABRA ------------")
print("ALFABETO: ", alfabeto1)
print("PROBABILIDADES: ", probabilidades1)
print("MATRIZ: ")
printMat(matriz1)
print("ES DE MEMORIA NULA? ", memoriaNula1)
print("ENTROPIA: ", entropia1)
print("EXTENSION ORDEN 2: ", extension1)
print("PROBABILIDADES EXTENSION ORDEN 2: ", probextension1)
print("ENTROPIA EXTENSION ORDEN 2: ", entropiaExtension)






print("\n \n \n ------------ SEGUNDA PALABRA ------------")

mensaje2 = "-+-+*//++///*/-////+---////-+/+--+-+/-/+-+/-+*++//"
alfabeto2, probabilidades2 = generaAlfabeto(mensaje2)
alfabeto2, matriz2 = generaMat(mensaje2)
memoriaNula2 = esMemoriaNula(matriz2, 0.01)
vectorEstacionario2 = vectorEstaconario(matriz2)
entropia2 = entropiaFuenteMarkov(matriz2, vectorEstacionario2)

print("ALFABETO: ", alfabeto2)
print("PROBABILIDADES: ", probabilidades2)
print("MATRIZ DE TRANSICION: ")
printMat(matriz2)
print("ES DE MEMORIA NULA? ", memoriaNula2)
print("VECTOR ESTACIONARIO: ", vectorEstacionario2)
print("ENTROPIA: ", entropia2)

