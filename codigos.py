import math
import random
import heapq
from fuente import *

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









##VERIFICA SI UN CODIGO CUMPLE EL PRIMER TEOREMA DE SHANNON
# Significado: Comprueba si la longitud media por símbolo original es mayor o igual que la entropía (Hr), y si al mismo tiempo está a menos de 1/n de distancia de esa entropía.
# TEOREMA DE SHANNON FANO: 
# Hr(S) <= Ln / n < Hr(S)+(1/n)
# Ln : número medio de símbolos del alfabeto código que son necesarios para representar un símbolo del alfabeto fuente
# recibe lista de distribucion de probabilidades, lista con palabras codigo p/ la extension de orden N, y el valor de N
def primerTeoremaShannon(prob, palabras, n):
    r = len(getAlfabetoCodigo(palabras))
    Hr = entropiaFuente(prob, informacionBaseN(prob, r))
    ext, extensionProb = extension(palabras, prob, n)
    ln = longitudMedia(ext, extensionProb)
    print("ln", ln)
    if(Hr <= ln/n and ln/n < Hr + 1/n):
        return True
    else:
        return False
    








##GENERA CODIGO DE HUFFMAN  (ENTENDER/EXPLICAR)
# Su objetivo es generar un código binario óptimo y sin prefijos para un conjunto de símbolos, basándose en sus probabilidades. 
# "Óptimo" significa que asigna los códigos más cortos a los símbolos más probables, minimizando la longitud media del mensaje codificado.
# Este código genera los códigos binarios óptimos para un conjunto de probabilidades. Lo hace construyendo un árbol de decisión de abajo hacia arriba.
# Busca las 2 hojas con las probabilidades más bajas (las menos probables).
# Las une en una nueva "rama", sumando sus probabilidades.
# Al unirlas, asigna un '0' a todos los códigos que vienen de una hoja y un '1' a los de la otra.
# Reemplaza las dos hojas viejas por esta nueva rama.
# Repite el proceso: vuelve a buscar las 2 "cosas" (hojas o ramas) menos probables, las une, les asigna '0' y '1', y las reemplaza.
# Sigue haciendo esto hasta que solo queda el árbol completo. El código de cada hoja original es el camino de '0's y '1's que se le fue asignando para llegar hasta él.
# El heap (cola de prioridad) solo sirve para encontrar rápidamente cuáles son las dos cosas menos probables en cada paso.
def codigoHuffman(probabilidades):
    # Crear una cola de prioridad (min-heap)
    heap = [[p, [str(i), ""]] for i, p in enumerate(probabilidades)]
    heapq.heapify(heap)

    # Construcción del árbol
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for par in lo[1:]:
            par[1] = '0' + par[1]
        for par in hi[1:]:
            par[1] = '1' + par[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    # Ordenar por símbolo original
    heap = sorted(heapq.heappop(heap)[1:], key=lambda x: int(x[0]))
    return [codigo for _, codigo in heap]
















##GENERA CODIGO DE SHANNON-FANO
# genera códigos binarios para cada símbolo usando el algoritmo de Shannon–Fano, que divide recursivamente los símbolos para formar códigos prefijos.
# El algoritmo construye los códigos separando símbolos en dos grupos balanceados y agregando 0 y 1 según en qué lado queden. Al repetir el proceso, se genera un código prefijo óptimo dentro del método Shannon–Fano.
# Se arma una lista de tuplas (índice, probabilidad).
# Se ordenan de mayor a menor probabilidad.
# Se prepara un diccionario donde se guardará el código de cada símbolo.
# Si queda un solo símbolo, ya tiene su código completo.
# Se intenta partir la lista en dos grupos con probabilidades lo más parecidas posible.
# Esa separación determina el próximo bit del código.
# Los símbolos del primer grupo reciben un 0.
# Los del segundo grupo reciben un 1.
# Cada grupo vuelve a dividirse y se asignan nuevos bits.
# El proceso continúa hasta que todos quedan solos.
# Se devuelve la lista final de códigos en el mismo orden que las probabilidades originales.
def codigoShannonFano(probabilidades):
    simbolos = [(i, p) for i, p in enumerate(probabilidades)]
    simbolos.sort(key=lambda x: x[1], reverse=True)
    codigos = {i: "" for i, _ in simbolos}

    def dividir(lista):
        if len(lista) == 1:
            return
        
        total = sum(p for _, p in lista)
        acumulado = 0
        mejor_i = 0
        mejor_dif = float('inf')

        for i in range(len(lista)):
            acumulado += lista[i][1]
            dif = abs(acumulado - (total - acumulado))
            if dif < mejor_dif:
                mejor_dif = dif
                mejor_i = i

        grupo1 = lista[:mejor_i+1]
        grupo2 = lista[mejor_i+1:]

        for s, _ in grupo1:
            codigos[s] += '0'
        for s, _ in grupo2:
            codigos[s] += '1'

        dividir(grupo1)
        dividir(grupo2)

    dividir(simbolos)
    return [codigos[i] for i in range(len(probabilidades))]
















# DEVUELVE UNA SECUENCIA DE BYTES (bytearray) QUE CONTIENE EL MENSAJE CODIFICADO
# alfabeto: cadena de caracteres que contenga un alfabeto fuente
# codificacion: una lista de cadenas de caracteres que almacena una codificación en el alfabeto binario
# mensaje: cadena de caracteres con un mensaje escrito en el alfabeto fuente
# zip une cada símbolo del alfabeto con su código.
# Se recorre el mensaje y se va construyendo una cadena de bits
# Se toma la cadena en porciones de 8 bits.
# Rellenar el último byte si no tiene 8 bits
# Convertir cada grupo de 8 bits en un número de 0–255. Cada uno se guarda en un bytearray, que es una forma compacta de almacenar bytes.
# La función devuelve un bytearray que contiene el mensaje codificado en binario, listo para almacenar o enviar.

def generaMensajeCodificado(alfabeto, codificacion, mensaje):
    tabla_codificacion = dict(zip(alfabeto, codificacion))
    mensaje_codificado = ""
    for simbolo in mensaje:
        mensaje_codificado += tabla_codificacion[simbolo]
    # Convertir la cadena de bits en un bytearray
    byte_array = bytearray()
    for i in range(0, len(mensaje_codificado), 8):
        byte = mensaje_codificado[i:i+8]
        if len(byte) < 8:
            byte = byte.ljust(8, '0')  # Rellenar con ceros si es necesario
        byte_array.append(int(byte, 2))
    return byte_array












# Dada una secuencia de bytes, decodificar y retornar el mensaje original
# crea la tabla codigo - simbolo
# Convertir el bytearray en una larga cadena de bits. Cada byte se convierte a binario de 8 bits fijos. Los concatena hasta volver a obtener la cadena completa de bits.
# Recorrer los bits para reconstruir los códigos. Va leyendo bit por bit y acumulándolos.
# Cuando encuentra un código válido, agrega el símbolo. Esto funciona porque los códigos son prefijos, así que no existe ambigüedad.

def decodificaMensaje(alfabeto, codificacion, byte_array):
    tabla_decodificacion = {v: k for k, v in zip(alfabeto, codificacion)}
    mensaje_codificado = ""
    for byte in byte_array:
        mensaje_codificado += format(byte, '08b')
    mensaje_decodificado = ""
    codigo_actual = ""
    for bit in mensaje_codificado:
        codigo_actual += bit
        if codigo_actual in tabla_decodificacion:
            mensaje_decodificado += tabla_decodificacion[codigo_actual]
            codigo_actual = ""
    return mensaje_decodificado

















# Tasa de compresion = N:1 (N = tamaño original / tamaño codificado)
# La funcion SOLO devuleve N
# CHEQUEADA
def tasaCompresion(mensaje_original, mensaje_codificado):
    tOriginal = len(mensaje_original) * 8 # (en bits)
    tCodificado = len(mensaje_codificado) * 8 # (en bits)
    return tOriginal / tCodificado














# CHEQUEADA, comprime un mensaje usando RLC y devuelve un bytearray. Para imprimirlo se puede usar print(list(comprimeRLC("...")))
# la funcion comprime repeticiones consecutivas de caracteres.
# byte_array guardará la compresión.
# i es el índice que recorre el mensaje.
# Recorrido del mensaje. Empieza una nueva secuencia de repeticiones.
# Contar cuántas veces se repite el mismo carácter. Mientras el carácter actual sea igual al siguiente, incrementa el contador.
# Guardar el par (carácter, cantidad). ord(mensaje[i]) convierte el carácter a su código ASCII (número 0–255). count es el número de repeticiones.
# Avanzar al siguiente carácter distinto
def comprimeRLC(mensaje):
    byte_array = bytearray()
    i = 0
    while i < len(mensaje):
        count = 1
        # Contar repeticiones
        while i + 1 < len(mensaje) and mensaje[i] == mensaje[i + 1]:
            count += 1
            i += 1

        # Agregar el carácter y la cantidad
        byte_array.append(ord(mensaje[i]))
        byte_array.append(count)

        i += 1  # avanzar al siguiente carácter distinto

    return byte_array













# CHEQUEADA: Devuelve la distancia de Hamming (minima) entre las cadenas (caracteres codificados) de una lista
# La función recibe una lista de cadenas binarias (o cualquier tipo de cadenas del mismo largo) y calcula La distancia de Hamming mínima entre todas las parejas de cadenas.
# La distancia de Hamming entre dos cadenas es la cantidad de posiciones donde difieren.
# Preparar lista de distancias. distancias almacenará las distancias calculadas. n es la cantidad de cadenas.
# Comparar cada par de cadenas sin repetir. Esto genera todas las combinaciones.
# Calcular la distancia de Hamming entre dos cadenas. zip junta las cadenas carácter a carácter. c1 != c2 vale True (o 1) si son distintos. sum(...) suma todas esas diferencias → la distancia de Hamming.
# Guardar la distancia
# retorna el mínimo valor de distancia entre todas las parejas de cadenas
def distanciaHamming(cadenas):
    distancias = []
    n = len(cadenas)
    for i in range(n):
        for j in range(i + 1, n):
            distancia = sum(c1 != c2 for c1, c2 in zip(cadenas[i], cadenas[j]))
            distancias.append(distancia)
    return min(distancias)













# CHEQUEADA: Devuelve la cantidad maxima de errores detectables dado una distancia de Hamming
def cantErroresDetectables(distanciaHamming):
    return distanciaHamming - 1

# CHEQUEADA: Devuelve la cantidad maxima de errores corregibles dado una distancia de Hamming
def cantErroresCorregibles(distanciaHamming):
    return (distanciaHamming - 1) // 2



# CHEQUEADA: Dado un caracter, devolver un byte que represente su código ASCII (7 bits) y utilice el bit menos significativo para almacenar la paridad del código
# Obtiene el código ASCII del carácter (solo usa 7 bits)
# Cuenta cuántos bits en 1 tiene el código ASCII
# Calcula el bit de paridad
# Produce 1 si la cantidad de bits en 1 es impar (paridad impar).
# Produce 0 si es par.
# Desplaza el código ASCII un bit a la izquierda para dejar espacio al bit de paridad
# Inserta el bit de paridad como LSB usando | paridad.
# Devuelve el byte resultante dentro de un bytearray.

def ascii_con_paridad(c):
    # Obtengo el código ASCII (7 bits)
    codigo = ord(c)
    # Calculo cantidad de bits en 1
    bits_en_1 = bin(codigo).count('1')
    # Calculo bit de paridad (0 o 1)
    paridad = bits_en_1 % 2 
    paridad = 1 if paridad == 1 else 0
    
    # Desplazo el código 1 bit a la izquierda y pongo la paridad en el LSB
    byte_final = (codigo << 1) | paridad
    rta = bytearray()
    rta.append(byte_final)
    return rta











# CHEQUEADA: La función detecta si un byte con paridad tiene un error de 1 bit verificando si el bit de paridad coincide con el que debería tener el código ASCII.
# Separa el byte en dos partes: Los 7 bits del código ASCII: codigo = byte >> 1, El bit de paridad real recibido: paridad_almacenada = byte & 1
# Cuenta los bits en 1 del código ASCII recibido.
# Recalcula el bit de paridad esperado según esos bits.
# Compara: Si la paridad recibida no coincide con la paridad calculada → hubo un error. Si coincide → no hubo error.
# Devuelve si hubo error
def byteTieneErrores(byte_con_paridad):
    # Extraigo el código ASCII (7 bits) y el bit de paridad
    codigo = byte_con_paridad >> 1
    paridad_almacenada = byte_con_paridad & 1
    
    # Calculo cantidad de bits en 1 en el código ASCII
    bits_en_1 = bin(codigo).count('1')
    # Calculo bit de paridad esperado
    paridad_calculada = bits_en_1 % 2
    paridad_calculada = 1 if paridad_calculada == 1 else 0
    
    # Comparo la paridad almacenada con la calculada
    return paridad_almacenada != paridad_calculada










# Dada una cadena de caracteres, generar una secuencia de bytes (bytearray) que
# contenga su representación con código ASCII y sus bits de paridad vertical,
# longitudinal y cruzada.

# Explicacion: 
# Cada carácter se convierte a su ASCII (7 bits) y se agrega un bit de paridad vertical.
# Luego se calcula un byte extra (la paridad longitudinal) mirando todas las columnas de bits.
# Finalmente, se calcula un último bit (LSB del PL) que actúa como paridad cruzada

# Obtiene su ASCII en 7 bits.
# Cuenta cuántos bits en 1 tiene.
# Calcula paridad vertical par (0 si tiene cantidad par de 1s, 1 si es impar).
# Crea un byte de 8 bits donde:
# Bits 7–1 = ASCII del carácter.
# Bit 0 = paridad vertical.
# Lo agrega a la lista de bytes.

# Se calcula la paridad longitudinal mirando columna por columna (bit 0…bit 7) de todos los bytes generados:
# Para cada posición de bit, cuenta cuántos 1 hay en esa columna.
# Si es impar → el bit de paridad longitudinal debe ser 1.
# Esto crea un byte PL, que asegura paridad par en cada columna.

# PARIDAD CRUZADA: Se calcula para el byte PL:
# Cuenta cuántos bits en 1 tiene PL.
# Ajusta el bit 0 del PL para que la paridad total del PL también sea par.

# agrega el byte PL

def codifica_con_paridades(cadena):
    bytes_codificados = []

    # Genero bytes con paridad vertical
    for c in cadena:
        codigo = ord(c) & 0x7F  # 7 bits ASCII
        bits_en_1 = bin(codigo).count('1')
        paridad_vertical = bits_en_1 % 2  # 1 si hay cantidad impar
        byte_con_paridad = (codigo << 1) | paridad_vertical
        bytes_codificados.append(byte_con_paridad)

    # Calculo paridad longitudinal (por columnas)
    pl = 0
    for bit_pos in range(8):
        unos = sum((b >> bit_pos) & 1 for b in bytes_codificados)
        if unos % 2 != 0:  # si es impar, el bit de PL debe ser 1
            pl |= (1 << bit_pos)

    # Calculo paridad cruzada (bit 0 del PL) sobre los bits 1..7 de PL
    bits_en_1 = bin(pl >> 1).count('1')
    paridad_cruzada = bits_en_1 % 2  # 1 si impar
    pl = (pl & 0xFE) | paridad_cruzada  # bit 0 = paridad cruzada

    # Agrego PL al final 
    bytes_codificados.append(pl)

    return bytearray(bytes_codificados)









# La función recibe un conjunto de bytes codificados con: 
# Paridad vertical (por carácter)
# Paridad longitudinal (por columnas)
# Paridad cruzada (sobre el PL)
# Y verifica si el conjunto tiene errores.
# Si todo está correcto, reconstruye el mensaje original.

# Separación de datos
# Toma todos los bytes menos el último como los bytes codificados.
# Toma el último byte como el PL (paridad longitudinal).

# Verificación de paridad vertical (fila por fila)
# Para cada byte:
# Separa los 7 bits ASCII.
# Cuenta sus 1s.
# Extrae el bit de paridad vertical.
# Verifica que tenga paridad par.
# Si alguna fila falla → retorna "" (error).

# Verificación de paridad longitudinal (columna por columna)
# Para cada bit (0 a 7):
# Cuenta los 1s en esa columna entre todos los bytes de datos.
# Extrae el bit correspondiente del PL.
# Verifica que la suma (datos + PL) tenga paridad par.
# Si alguna columna falla → error.

# Verificación de paridad cruzada (bit 0 del PL)
# Revisa todos los bits del PL excepto el bit 0.
# Extrae el bit de paridad cruzada.
# Verifica que toda la paridad del PL sea par.
# Si falla → error.

# Si todas las paridades son correctas
# Se reconstruye el mensaje:
# Para cada byte se toma b >> 1 (los 7 bits ASCII)
# Se convierte a carácter
# Se agrega al mensaje final
# Finalmente se retorna el mensaje original.

def decodifica_con_paridades(data):
    # Valido longitud mínima
    if len(data) < 2:
        return ""
    
    n = len(data) - 1
    bytes_codificados = data[:-1]
    pl = data[-1]

    # Verifico paridad vertical (por fila)
    for b in bytes_codificados:
        bits_en_1 = bin(b >> 1).count('1')  # contar bits de los 7 bits ASCII
        paridad_vertical = b & 1
        total_1 = bits_en_1 + paridad_vertical
        if total_1 % 2 != 0:
            # Error de paridad vertical → no se puede corregir
            return ""

    # Verifico paridad longitudinal (por columna)
    for bit_pos in range(8):
        unos = sum((b >> bit_pos) & 1 for b in bytes_codificados)
        bit_pl = (pl >> bit_pos) & 1
        total_1 = unos + bit_pl
        if total_1 % 2 != 0:
            # Error de paridad longitudinal → no se puede corregir
            return ""

    # Verifico paridad cruzada (bit 0 de PL)
    bits_en_1 = bin(pl >> 1).count('1')
    paridad_cruzada = pl & 1
    total_1 = bits_en_1 + paridad_cruzada
    if total_1 % 2 != 0:
        # Error de paridad cruzada
        return ""

    # Si todo está bien, reconstruyo el mensaje
    mensaje = ""
    for b in bytes_codificados:
        codigo_ascii = b >> 1
        mensaje += chr(codigo_ascii)

    return mensaje


