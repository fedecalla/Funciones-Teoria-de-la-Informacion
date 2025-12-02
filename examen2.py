import math
import random
import itertools

def getAlfabetoCodigo(palabras):
    alfabeto = []
    for palabra in palabras:
        for letra in palabra:
            if letra not in alfabeto:
                alfabeto.append(letra)
    return alfabeto


def informacionBaseN(probabilidades, base):
    inf = [(-math.log(p, base)) for p in probabilidades]
    return inf

def entropiaFuente(probabilidades, informaciones):
    ent = 0
    for i in range(0, len(probabilidades)):
       ent = ent + probabilidades[i] * informaciones[i] 
    return ent

def longitudMedia(palabras_codigo, probabilidades):
    q = len(palabras_codigo)
    longitud = 0
    for _ in range(q):
        longitud = longitud + probabilidades[_] * len(palabras_codigo[_])
    return longitud


def getLongitudes(palabras):
    longitudes = [len(palabra) for palabra in palabras]
    return longitudes


def inecuacionKraft(palabras):
    alfabeto = getAlfabetoCodigo(palabras)
    longitudes = getLongitudes(palabras)
    r = len(alfabeto)
    suma = 0
    for _ in palabras:
        suma = suma + pow(r, longitudes[palabras.index(_)] * -1)
    
    print("Suma de la inecuacion de Kraft =", suma)

    if(suma <= 1):
        return True
    else:
        return False
    


def esNoSingular(palabras):
    cumple = True
    n = len(palabras)
    i = 0
    while(i < n and cumple):
        j = 0
        while(j < n and cumple):
            if(palabras[i] == palabras[j] and i != j):
                cumple = False
            j += 1
        i += 1
    return cumple

def esInstantaneo(palabras):
    cumple = True
    n = len(palabras)
    i = 0
    while(i < n and cumple):
        j = 0
        while(j < n and cumple):
            if(i != j and (palabras[i] == palabras[j][0:len(palabras[i])] or palabras[j] == palabras[i][0:len(palabras[j])])):
                cumple = False
            j += 1
        i += 1
    return cumple

def esUnivoco(palabras):
    # Algoritmo de Sardinas-Patterson
    # palabras: lista de strings
    U = set()
    n = len(palabras)

    # 1. diferencias iniciales
    for i in range(n):
        for j in range(n):
            if i != j and palabras[j].startswith(palabras[i]):
                resto = palabras[j][len(palabras[i]):]
                if resto:
                    U.add(resto)

    vistos = set()
    while U:
        if any(u in palabras for u in U):
            return False  # encontró contradicción
        if U in vistos:
            return True   # ya repitió → seguro es UD
        vistos.add(frozenset(U))

        # generar nuevos residuos
        nuevo = set()
        for u in U:
            for w in palabras:
                if w.startswith(u):
                    resto = w[len(u):]
                    if resto:
                        nuevo.add(resto)
                if u.startswith(w):
                    resto = u[len(w):]
                    if resto:
                        nuevo.add(resto)
        U = nuevo
    return True

def clasificaCodigo(palabras):
    if(esNoSingular(palabras)):
        if(esUnivoco(palabras)):
            if(esInstantaneo(palabras)):
                return "Instantaneo"
            else:
                return "Univoco no instantaneo"
        else:
            return "No singular"
    else:
        return "Singular"
    

def esCompacto(palabras_codigo, probabilidades):
    # Asumimos que es compacto hasta demostrar lo contrario
    cumple = True
    
    # Iteramos por índice para asegurar que la palabra 'i' 
    # se compara con la probabilidad 'i'
    for i in range(len(palabras_codigo)):
        palabra = palabras_codigo[i]
        probabilidad = probabilidades[i]
        
        # Validación de seguridad para evitar log(0) o división por cero
        if probabilidad <= 0:
            continue 

        # Calculamos la longitud teórica de Shannon (Techo de la información)
        longitud_teorica = math.ceil(math.log2(1/probabilidad))
        
        # Si la palabra es más larga de lo que la teoría permite, no es compacto
        if len(palabra) > longitud_teorica:
            cumple = False
            break # Si ya falló uno, no hace falta seguir revisando
            
    return cumple





print("\n\n\n----------------------------- CODIGO 1 -----------------------------")

probabilidades1 = [0.15, 0.25, 0.05, 0.45, 0.10]
palabrasCodigo1 = [";.", ",", ".:", ":", ",;"]
r = len(getAlfabetoCodigo(palabrasCodigo1))

informaciones1 = informacionBaseN(probabilidades1, r)
entropia1 = entropiaFuente(probabilidades1, informaciones1)
print("Entropia =", entropia1)

longitudMedia1 = longitudMedia(palabrasCodigo1, probabilidades1)
print("L =", longitudMedia1)

print("Inecuacion de Kraft se cumple?", inecuacionKraft(palabrasCodigo1))

print("Clasificacion del codigo:", clasificaCodigo(palabrasCodigo1))

print("Compacto =", esCompacto(palabrasCodigo1, probabilidades1))



print("\n\n\n----------------------------- CODIGO 2 -----------------------------")

probabilidades2 = [0.15, 0.25, 0.05, 0.45, 0.10]
palabrasCodigo2 = [",;", ";", ":.", ".", ",:"]
r = len(getAlfabetoCodigo(palabrasCodigo2))

informaciones2 = informacionBaseN(probabilidades2, r)
entropia2 = entropiaFuente(probabilidades2, informaciones2)
print("Entropia =", entropia2)
longitudMedia2 = longitudMedia(palabrasCodigo2, probabilidades2)
print("L =", longitudMedia2)
print("Inecuacion de Kraft se cumple?", inecuacionKraft(palabrasCodigo2))
print("Clasificacion del codigo:", clasificaCodigo(palabrasCodigo2))
print("Compacto =", esCompacto(palabrasCodigo2, probabilidades2))




