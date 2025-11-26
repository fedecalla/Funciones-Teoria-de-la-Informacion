import math
import random
import itertools

#INFORMACION DE UNA FUENTE
# informacion = -log2(pi)
# La informacion mide la "sorpresa" que genera la aparicion de un simbolo i con probabilidad pi
def informacionFuente(probabilidades):
    inf = [math.log2(1/p) for p in probabilidades]
    return inf



# informacion = -logn(pi)
# misma definicion que la anterior pero varia la base (unidad de medida de la informacion)
def informacionBaseN(probabilidades, base):
    inf = [(-math.log(p, base)) for p in probabilidades]
    return inf




#ENTROPIA DE UNA FUENTE
# implementa la formula: H(S) = sumatoria desde i=1 hasta n de pi * I(i) donde pi es la probabilidad del simbolo i e I(i) es la informacion del simbolo i
# La entropia indica la cantidad mínima de bits promedio necesarios para representar los símbolos de esa fuente sin perder información
def entropiaFuente(probabilidades, informaciones):
    ent = 0
    for i in range(0, len(probabilidades)):
       ent = ent + probabilidades[i] * informaciones[i] 
    return ent






#ENTROPIA BINARIA
# Entropia de una fuente binaria con probabilidad w de 1 y (1-w) de 0
def entropiaBinaria(w):
    prob = [w, 1-w]
    return entropiaFuente(prob, informacionBaseN(prob, 2))







#GENERA ALFABETO Y PROBABILIDADES A PARTIR DE UNA CADENA
# recorre caracter por caracter
# si el simbolo existe en alfabeto, busca su indice y suma la probabilidad 1/longitud a probabilidades[indice]
# si no existe, lo agrega al alfabeto y establece su probabilidad inicial en 1/longitud
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
# se genera el producto cartesiano del alfabeto, repetido "orden" veces
# se calculan las probabilidades de cada cadena resultante multiplicando las probabilidades de cada simbolo
# Extender la fuente permite comprimir mejor. Segun el Primer Teorema de Shannon, al codificar bloques mas largos la longitud promedio por simbolo del codigo resultante se acerca mucho más a la Entropia teorica de la fuente, reduciendo la redundancia

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
# fuente de markov -> la probabilidad del siguiente símbolo depende del símbolo anterior.
# La entropía suele ser menor, porque conocer el estado actual nos da pistas sobre el siguiente (reduce la incertidumbre).

# implementa la formula: H(S) = sumatoria desde i = 1 hasta n de P(si) * H(S|si) siendo P(si) la probabilidad estacionaria de estar en el estado i
# H(S|si) la entropia condicional de las transiciones desde el estado i
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



