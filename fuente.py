import math
import random
import itertools

#INFORMACION DE UNA FUENTE
def informacionFuente(probabilidades):
    inf = [math.log2(1/p) for p in probabilidades]
    return inf

def informacionBaseN(probabilidades, base):
    inf = [(-math.log(p, base)) for p in probabilidades]
    return inf

#ENTROPIA DE UNA FUENTE
def entropiaFuente(probabilidades, informaciones):
    ent = 0
    for i in range(0, len(probabilidades)):
       ent = ent + probabilidades[i] * informaciones[i] 
    return ent

#ENTROPIA BINARIA
def entropiaBinaria(w):
    prob = [w, 1-w]
    return entropiaFuente(prob, informacionBaseN(prob, 2))


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

#GENERA PALABRA DE LONGITUD L A PARTIR DE UN ALFABETO Y SUS PROBABILIDADES
def generaPalabra(alfabeto, prob, longitud):
    palabra = random.choices(alfabeto, weights = prob, k = longitud)
    return palabra
    

#GENERA EXTENSION DE ORDEN N DE UNA FUENTE
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


#ENTROPIA DE UNA FUENTE DE MARKOV
def entropiaFuenteMarkov(matriz, vectorEstacionario):
    n = len(matriz)
    ent = 0.0
    for i in range(n):
        sum1 = 0
        for j in range(n):
            sum1 = sum1 + matriz[i][j] * math.log(1/matriz[i][j], 2)
        ent += sum1 * vectorEstacionario[i]
    return ent


def getr(palabras):
    alfabeto = []
    for palabra in palabras:
        for letra in palabra:
            if letra not in alfabeto:
                alfabeto.append(letra)
    return len(alfabeto)



