import math
import random

##VERIFICA SI UN CODIGO ES NO SINGULAR
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

##VERIFICA SI UN CODIGO ES INSTANTANEO
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

##VERIFICA SI UN CODIGO ES UNIVOCO

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

##DEVUELVE EL ALFABETO DEL CODIGO DADAS SUS PALABRAS
def getAlfabetoCodigo(palabras):
    alfabeto = []
    for palabra in palabras:
        for letra in palabra:
            if letra not in alfabeto:
                alfabeto.append(letra)
    return alfabeto

##DEVUELVE LAS LONGITUDES DE CADA PALABRA DEL CODIGO
def getLongitudes(palabras):
    longitudes = [len(palabra) for palabra in palabras]
    return longitudes

##VERIFICA SI UN CODIGO CUMPLE LA INECUACION DE KRAFT
def inecuacionKraft(palabras):
    alfabeto = getAlfabetoCodigo(palabras)
    longitudes = getLongitudes(palabras)
    r = len(alfabeto)
    suma = 0
    for _ in palabras:
        suma = suma + pow(r, longitudes[palabras.index(_)] * -1)

    if(suma <= 1):
        return True
    else:
        return False
    

##DEVUELVE LA LONGITUD MEDIA DE UN CODIGO
def longitudMedia(palabras_codigo, probabilidades):
    q = len(palabras_codigo)
    longitud = 0
    for _ in range(q):
        longitud = longitud + probabilidades[_] * len(palabras_codigo[_])
    return longitud

##VERIFICA SI UN CODIGO ES COMPACTO
def esCompacto(palabras_codigo, probabilidades):
    cumple = True

    for _ in palabras_codigo:
        if(len(_) > math.ceil(math.log2(1/probabilidades[palabras_codigo.index(_)]))):
            cumple = False
    return cumple


##GENERA UN MENSAJE DE LONGITUD DADA A PARTIR DE UN CODIGO Y SUS PROBABILIDADES
def generaMensaje(palabras_codigo, probabilidades, longitud):
    mensaje = random.choices(palabras_codigo, weights=probabilidades, k=longitud)
    return mensaje