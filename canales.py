import math
from fuente import generaAlfabeto
from math import log2




# Genera la matriz del canal partiendo de una cadena de entrada y una de salida
# CHEQUEADA. Cada [] corresponde a una fila de la matriz.
# EXPLICACION:

# Este código calcula la matriz de transición de un canal. Su objetivo es determinar la probabilidad de recibir un símbolo de salida (Y) dado que se envió un símbolo de entrada (X).
# Funciona en tres pasos principales:
# Identificar Símbolos: Encuentra todos los símbolos únicos de entrada (filas) y de salida (columnas).
# Contar Frecuencias: Recorre las listas entrada y salida al mismo tiempo. Cuenta cuántas veces ocurrió cada par (ej. "se envió 'A' y se recibió 'B'") y lo guarda en una matriz de conteo.
# Calcular Probabilidades (Normalizar): Divide el conteo de cada celda por el número total de veces que se envió el símbolo de entrada de esa fila. Esto convierte los conteos (ej. "3 veces") en probabilidades (ej. "0.75" o 75%).

def matrizCanal(entrada, salida):
    # obtengo los simbolos de entrada y salida
    simbolos_entrada = list(sorted(set(entrada)))
    simbolos_salida = list(sorted(set(salida)))
    # creo una matriz vacia para contar
    matriz = [[0 for _ in range(len(simbolos_salida))] for _ in range(len(simbolos_entrada))]
    # creo un contador de ocurrencias por simbolo de entrada
    total_entrada = {simbolo: 0 for simbolo in simbolos_entrada}

    # cuento las ocurrencias de cada par (entrada, salida)
    for e, s in zip(entrada, salida):
        i = simbolos_entrada.index(e)
        j = simbolos_salida.index(s)
        matriz[i][j] += 1
        total_entrada[e] += 1

    # normalizo la matriz para obtener probabilidades condicionales
    for i in range(len(simbolos_entrada)):
        for j in range(len(simbolos_salida)):
            if total_entrada[simbolos_entrada[i]] > 0:
                matriz[i][j] /= total_entrada[simbolos_entrada[i]]

    return matriz








# calcula las probabilidades a priori (o probabilidades marginales) de los símbolos de entrada.
# En términos simples: toma una secuencia (la cadena) y te dice qué tan probable es que aparezca cada símbolo único dentro de esa secuencia, basándose en su frecuencia.

# EXPLICACION:
# Identifica los símbolos únicos en la cadena (y los ordena).
# Cuenta cuántas veces aparece cada uno.
# Divide ese conteo por la longitud total de la cadena, generando la lista de probabilidades.
# CHEQUEADA
def probabilidadesAPriori(cadena):
    simbolos = list(sorted(dict.fromkeys(cadena))) # Conserva el orden de aparicion
    total = len(cadena)

    prob_entrada = []
    for s in simbolos:
        prob_entrada.append(cadena.count(s) / total)
    
    return prob_entrada







# Devuelve las probabilidades de los simbolos de salida partiendo de las probabilidades a priori y la matriz del canal

# EXPLICACION:
# Implementa la siguiente formula:
# P(Yj) = sumatoria (i) de (P(Xi) . P(Yj|Xi))

# CHEQUEADA
def probabilidadesSalida(prob_entrada, matriz_canal):
    prob_salida = [0 for j in matriz_canal[0]]
    
    for j in range(len(matriz_canal[0])):
        for i in range(len(matriz_canal)):
            prob_salida[j] = prob_salida[j] + (prob_entrada[i] * matriz_canal[i][j])

    return prob_salida









# Devuelve una matriz con las probabilidades a posteriori del canal partiendo de las probabilidades a priori y la matriz del canal
# Esta matriz responde a la pregunta más importante en la decodificación de un mensaje: "Dado que recibí el símbolo 'Y', ¿cuál es la probabilidad de que se haya enviado el símbolo 'X'?"
# La función aplica directamente el Teorema de Bayes a un canal de comunicación para invertir la probabilidad

# Cálculo de P(Y): Llama a la función probabilidadesSalida para obtener las probabilidades marginales de salida (P(Yj)).
# Inicialización: Crea la matriz matriz_posteriori vacía (llena de ceros).
# Aplicación de Bayes: Itera sobre cada celda (i = entrada, j = salida).
# División Segura: Si la probabilidad de salida P(Yj) no es cero, calcula el cociente del Teorema de Bayes. Si es cero, la probabilidad se establece en cero para evitar la división por cero.

# Resultado: Una matriz donde cada columna (Yj, el símbolo recibido) suma 1, ya que dado que recibiste un símbolo, la probabilidad de que haya sido cualquier símbolo de entrada debe sumar el 100%.
# CHEQUEADA
def matrizPosteriori(prob_entrada, matriz_canal):
    # Obtengo las probabilidades de salida
    prob_salida = probabilidadesSalida(prob_entrada, matriz_canal)

    filas = len(matriz_canal)        # cantidad de símbolos de entrada
    columnas = len(matriz_canal[0])  # cantidad de símbolos de salida

    # Inicializo la matriz posteriori vacía
    matriz_posteriori = [[0 for _ in range(columnas)] for _ in range(filas)]

    # Aplico la fórmula de Bayes
    for i in range(filas):
        for j in range(columnas):
            if prob_salida[j] > 0:
                matriz_posteriori[i][j] = (prob_entrada[i] * matriz_canal[i][j]) / prob_salida[j]
            else:
                matriz_posteriori[i][j] = 0  # evito división por cero

    return matriz_posteriori












# Devuelve una matriz con las probabilidades de los eventos simultáneos
# Este código calcula la matriz de probabilidad conjunta (P(X,Y)).

# Esta matriz es crucial porque determina la probabilidad de que ocurran simultáneamente un símbolo de entrada específico (X) y un símbolo de salida específico (Y). En esencia, responde a la pregunta: "¿Cuál es la probabilidad de que haya enviado el símbolo 'X' Y haya recibido el símbolo 'Y'?"
# La función utiliza la regla de la multiplicación para eventos dependientes: P(Xi, Yj) = P(Xi).P(Yj|Xi)

# Inicialización: Obtiene las dimensiones de la matriz de transición y crea la matriz matriz_conjunta llena de ceros.
# Cálculo: Itera sobre cada posible par de entrada (i) y salida (j).
# Multiplicación Clave: Multiplica la probabilidad a priori de la fila (P(Xi)) por la probabilidad de transición del canal (P(Yj|Xi)) para llenar la celda [i][j].
# Resultado: Una matriz donde la suma de todos sus elementos es igual a 1, ya que cubre todas las combinaciones posibles de entrada y salida del canal.
# CHEQUEADA
def matrizConjunta(prob_entrada, matriz_canal):

    filas = len(matriz_canal)        # cantidad de símbolos de entrada
    columnas = len(matriz_canal[0])  # cantidad de símbolos de salida

    # Inicializo la matriz de ceros
    matriz_conjunta = [[0 for _ in range(columnas)] for _ in range(filas)]

    # Aplico la fórmula de la probabilidad de sucesos simultaneos
    for i in range(filas):
        for j in range(columnas):
            matriz_conjunta[i][j] = prob_entrada[i] * matriz_canal[i][j]

    return matriz_conjunta













# Devuelve una lista con las entropias a posteriori a partir de las probabilidades a priori y la matriz de prob. condicionales
# El resultado es un vector de valores de entropía, donde cada elemento te dice la incertidumbre que queda sobre el símbolo que se envió (X), después de haber recibido un símbolo específico (Y).
# Fórmula Aplicada: La función aplica la fórmula de la entropía de Shannon, utilizando las probabilidades a posteriori P(X|Y) (calculadas internamente con el Teorema de Bayes):
# H(X|Yj) = - sumatoria (i) de (P(Xi|Yj) . log2(P(Xi|Yj)))

# Calculo de probabilidades de salida usando P(X) P(Y|X)
# Cálculo de P(X|Y) (Matriz a Posteriori): Calcula la probabilidad inversa P(X|Y) usando el Teorema de Bayes
# Cálculo de Entropía: Itera sobre cada columna (cada símbolo de salida Yj). Para cada columna, usa sus probabilidades a posteriori P(X|Yj) como el conjunto de probabilidades para calcular una entropía separada (H).
# Retorno: Devuelve una lista (entropias) donde cada elemento es la equivocación asociada a la recepción de un símbolo de salida específico.

# CHEQUEADA
def entropiasPosteriori(prob_entrada, matriz_canal):
    # Calculo probabilidades marginales de salida
    prob_salida = [0 for _ in range(len(matriz_canal[0]))]
    for j in range(len(matriz_canal[0])):
        for i in range(len(matriz_canal)):
            prob_salida[j] += prob_entrada[i] * matriz_canal[i][j]

    # Calculo la matriz a posteriori
    matriz_posteriori = [[0 for _ in range(len(matriz_canal[0]))] for _ in range(len(matriz_canal))]
    for i in range(len(matriz_canal)):
        for j in range(len(matriz_canal[0])):
            if prob_salida[j] > 0:
                matriz_posteriori[i][j] = (prob_entrada[i] * matriz_canal[i][j]) / prob_salida[j]

    # Calculo las entropías
    entropias = []
    for j in range(len(matriz_canal[0])):
        h = 0
        for i in range(len(matriz_canal)):
            p = matriz_posteriori[i][j]
            if p > 0:
                h -= p * math.log2(p)
        entropias.append(h)

    return entropias




# El código calcula la Entropía Condicional de la Fuente dada la Salida (H(X|Y)), también conocida como la Equivocación o Ruido del Canal.
# El valor final devuelto es una medida de la incertidumbre promedio sobre el símbolo que se envió (X), después de haber observado lo que se recibió (Y). Es la cantidad de información que se pierde en el canal.
# El primer bloque de código (etiquetado # Calculo P(b)) usa la Ley de Probabilidad Total (P(Y) = sumatoria de(P(X)P(Y|X))) para encontrar la probabilidad de recibir cada símbolo, sin importar cuál fue enviado.
# El segundo bloque (etiquetado # Calculo P(A | b)) usa el Teorema de Bayes para calcular la probabilidad inversa: la probabilidad de que se haya enviado X, dado que se recibió Y.
# El último bloque (etiquetado # Calculo H(A|B)) calcula la entropía condicional promedio, que se define como: H(X|Y) = sumatoria (j) de (P(Yj).H(X|Yj)
# CHEQUEADA
def ruido(prob_entrada, matriz_canal):
    # Calculo P(b)
    prob_salida = [0 for _ in range(len(matriz_canal[0]))]
    for j in range(len(matriz_canal[0])):
        for i in range(len(matriz_canal)):
            prob_salida[j] += prob_entrada[i] * matriz_canal[i][j]

    # Calculo P(A | b)
    matriz_posteriori = [[0 for _ in range(len(matriz_canal[0]))] for _ in range(len(matriz_canal))]
    for i in range(len(matriz_canal)):
        for j in range(len(matriz_canal[0])):
            if prob_salida[j] > 0:
                matriz_posteriori[i][j] = (prob_entrada[i] * matriz_canal[i][j]) / prob_salida[j]

    # Calculo H(A|B)
    H_X_dado_Y = 0
    for j in range(len(matriz_canal[0])):
        H_cond_j = 0
        for i in range(len(matriz_canal)):
            p = matriz_posteriori[i][j]
            if p > 0:
                H_cond_j -= p * math.log2(p)
        H_X_dado_Y += prob_salida[j] * H_cond_j

    return H_X_dado_Y










# El código calcula la Entropía Condicional de la Salida dada la Entrada (H(Y|X)), también conocida como la Pérdida o Equivocación del canal.
# Este valor representa la incertidumbre promedio sobre lo que se recibirá (Y), dado que ya se conoce lo que se envió (X). Es la medida del ruido intrínseco del canal.
# La función implementa la fórmula de la entropía condicional promedio:
# H(Y|X) = sumatoria(i) de(P(Xi) . H(Y|Xi))
# Bucle Externo (i): Itera sobre cada posible símbolo de entrada (Xi) y usa su probabilidad a priori P(Xi) para ponderar el resultado final.
# Bucle Interno (j): Para cada símbolo de entrada Xi (fila i de la matriz): Calcula la entropía local Hcondi (Equivocación de la Fuente) usando la fórmula de Shannon, pero solo con las probabilidades de esa fila específica (matriz_canal[i][j]). Esta fila i es precisamente la distribución de probabilidad P(Y|Xi).
# Ponderación y Suma: Multiplica cada entropía local Hcondi por la probabilidad de que esa entrada Xi realmente ocurra (P(Xi)).
# Retorno: Devuelve la Pérdida total promedio H(Y|X), que cuantifica el ruido o la ambigüedad que el canal introduce en el mensaje. Un valor cercano a cero indica que el canal es casi perfecto.
def perdida(prob_entrada, matriz_canal):
    H_Y_dado_X = 0
    
    for i in range(len(matriz_canal)):  # para cada entrada X_i
        H_cond_i = 0
        for j in range(len(matriz_canal[0])):  # para cada salida Y_j
            p = matriz_canal[i][j]
            if p > 0:
                H_cond_i -= p * math.log2(p)
        H_Y_dado_X += prob_entrada[i] * H_cond_i
    
    return H_Y_dado_X
















# El código calcula la Entropía de la Salida (H(Y)).
# La Entropía de Salida es una medida de la incertidumbre promedio de los símbolos que se reciben a través del canal, después de que la fuente de entrada ha sido afectada por la matriz de transición.
# El primer bloque de código calcula las probabilidades de que se reciba cada símbolo (P(Y)) utilizando la Ley de Probabilidad Total (P(Y) = sumatoria de( P(X)P(Y|X))). Este paso es crucial, ya que la entropía de la salida solo depende de la distribución de probabilidad de la salida Y.
# El segundo bloque de código utiliza la lista prob_salida (P(Y)) para calcular la Entropía de Shannon H(Y): H(Y) = - sumatoria (j) de (P(Yj).log2(P(Yj)))

def entropiaAfin(prob_entrada, matriz_canal):
    # Calculo P(Y_j)
    prob_salida = [0 for _ in range(len(matriz_canal[0]))]
    for j in range(len(matriz_canal[0])):
        for i in range(len(matriz_canal)):
            prob_salida[j] += prob_entrada[i] * matriz_canal[i][j]

    # Calculo entropía H(Y)
    H_Y = 0
    for p in prob_salida:
        if p > 0:
            H_Y -= p * math.log2(p)

    return H_Y














# La Información Mutua es la métrica más importante de un canal. Mide la cantidad de información que se transfiere o se comparte entre la entrada (X) y la salida (Y).
# I(X,Y) representa cuánto se reduce la incertidumbre sobre la entrada (X) cuando se observa la salida (Y). El valor se mide en bits y un valor más alto significa un canal más eficiente y menos ruidoso.
# I(X,Y) = H(X) - H(X|Y)
# El primer bloque calcula la incertidumbre inicial de la fuente de entrada (prob_entrada).
# El código calcula implícitamente P(Y) y P(X|Y) para luego calcular la incertidumbre restante sobre la entrada, dado lo que se recibió. Este es el valor de la equivocación que se pierde en el canal.
# Resta la incertidumbre restante (H(X|Y)) de la incertidumbre inicial (H(X))
# La diferencia es la información que sí se transmitió con éxito.

def informacionMutua(prob_entrada, matriz_canal):

    # --- H(X)
    H_X = -sum(p * math.log2(p) for p in prob_entrada if p > 0)

    # --- Calcular P(Y_j)
    prob_salida = [0 for _ in range(len(matriz_canal[0]))]
    for j in range(len(matriz_canal[0])):
        for i in range(len(matriz_canal)):
            prob_salida[j] += prob_entrada[i] * matriz_canal[i][j]

    # --- Calcular H(X|Y)
    H_X_dado_Y = 0
    for j in range(len(matriz_canal[0])):
        H_cond_j = 0
        # Calcular P(X_i|Y_j)
        for i in range(len(matriz_canal)):
            if prob_salida[j] > 0:
                p_xy = prob_entrada[i] * matriz_canal[i][j]
                p_x_dado_y = p_xy / prob_salida[j]
                if p_x_dado_y > 0:
                    H_cond_j -= p_x_dado_y * math.log2(p_x_dado_y)
        H_X_dado_Y += prob_salida[j] * H_cond_j

    # --- Información mutua
    I_XY = H_X - H_X_dado_Y
    return I_XY







# Verifica si una matriz (lista de listas) representa un canal sin ruido.
# Devuelve True si todos los valores son iguales, False en caso contrario.
# chequeada
# EXPLICACION:


# Comprueba que la matriz no esté vacía (es decir, que haya filas y columnas). Si está vacía, no tiene sentido analizarla, así que devuelve False.
# Recorre todas las filas dentro de esa columna (i es el índice de la fila). Cuenta cuántos valores en esa columna son distintos de 0. Si encuentra un valor distinto de 0, incrementa el contador distintos_de_cero.
# Al terminar de revisar una columna: Si no hay exactamente un valor distinto de 0, devuelve False inmediatamente. (porque la condición de “sin ruido” no se cumple)
def canal_sin_ruido(canal):
    if not canal or not canal[0]:
        return False  # matriz vacía
    
    filas = len(canal)
    columnas = len(canal[0])
    
    for j in range(columnas):  
        distintos_de_cero = 0
        for i in range(filas):
            if canal[i][j] != 0:
                distintos_de_cero += 1
        if distintos_de_cero != 1:  
            return False
    return True









# Verifica si una matriz (canal) es determinante. Es determinante si en cada fila hay un solo elemento distinto de 0. Retorna True si cumple la condición, False en caso contrario.
# chequeada
# EXPLICACION:


# La función recorre cada fila de la matriz.
# Cuenta cuántos valores son distintos de 0.
# Si alguna fila tiene cero o más de uno → no es determinante.
# Si todas tienen exactamente uno → es determinante.

def canal_determinante(canal):
    if not canal or not canal[0]:
        return False  
    
    for fila in canal:
        distintos_de_cero = 0
        for valor in fila:
            if valor != 0:
                distintos_de_cero += 1
        if distintos_de_cero != 1:
            return False
    return True








# Multiplica dos matrices (canales) para formar el canal compuesto en serie. Retorna la matriz resultado del producto matricial canal1 * canal2.
# chequeada
# EXPLICACION:

# Se verifica que el número de columnas del primer canal sea igual al número de filas del segundo (requisito para multiplicar matrices).
# Se crea una nueva matriz de ceros con las dimensiones correctas.
# Para cada posición (i, j) de la matriz resultante, se hace la suma de los productos correspondientes:

def canal_en_serie(canal1, canal2):
    # Verificar compatibilidad de dimensiones
    filas1 = len(canal1)
    columnas1 = len(canal1[0])
    filas2 = len(canal2)
    columnas2 = len(canal2[0])

    if columnas1 != filas2:
        raise ValueError("Las dimensiones no son compatibles para la multiplicación.")

    # Crear matriz resultado (inicializada en 0)
    resultado = [[0 for _ in range(columnas2)] for _ in range(filas1)]

    # Producto matricial
    for i in range(filas1):
        for j in range(columnas2):
            suma = 0
            for k in range(columnas1):
                suma += canal1[i][k] * canal2[k][j]
            resultado[i][j] = suma

    return resultado






# Verifica si las columnas c1 y c2 de la matriz canal pueden combinarse en una reducción suficiente (son proporcionales o idénticas).
# canal: lista de listas (matriz). c1, c2: índices de las columnas a comparar. tolerancia: margen de error para comparar flotantes

# EXPLICACION:

# Calcula cuántas filas tiene la matriz.
# Verifica que los índices de las columnas existan (no estén fuera de rango).
# Creamos una variable k que guardará la razón (proporción) entre ambas columnas, por ejemplo, si col2 = 2 * col1, entonces k = 2.
# Recorremos cada fila de la matriz, tomando los valores correspondientes en las dos columnas.
# Si ambos valores son cero, no afectan la proporción, los saltamos.
# Si uno es cero y el otro no, las columnas no pueden ser proporcionales → devolvemos False.
# Calculamos el cociente b/a.
# Si es la primera vez, lo guardamos como k.
# En las siguientes filas, comparamos si la proporción se mantiene igual.
# Si no, ya no son proporcionales → False.
# Si terminamos el bucle sin encontrar contradicciones, las columnas son proporcionales → se pueden reducir → devolvemos True.


def columnas_reductibles(canal, c1, c2, tolerancia=1e-6):
    filas = len(canal)

    # Evitar columnas fuera de rango
    if c1 >= len(canal[0]) or c2 >= len(canal[0]):
        raise IndexError("Los índices de columnas no son válidos.")
    
    # Buscar la constante de proporcionalidad (si existe)
    k = None
    for i in range(filas):
        a, b = canal[i][c1], canal[i][c2]
        if a == 0 and b == 0:
            continue  # ambos 0 no aportan información
        elif a == 0 or b == 0:
            return False  # una columna tiene 0 donde la otra no
        else:
            ratio = b / a
            if k is None:
                k = ratio
            elif abs(ratio - k) > tolerancia:
                return False  # no son proporcionales
    return True



# Genera la matriz determinante necesaria para combinar las columnas c1 y c2 de la matriz 'canal'.
# Devuelve la matriz determinante D tal que: P' = P * D

# EXPLICACION
# La función crea la matriz determinante D que indica cómo combinar dos columnas (c1 y c2) de una matriz de canal.
# Tiene el mismo número de filas que columnas originales, pero una columna menos (porque se fusionan dos).
# Al multiplicar P × D, obtenés la matriz del canal reducido, donde las columnas c1 y c2 se suman en una sola.

def canal_determinante_para_combinar(canal, c1, c2):    
    columnas = len(canal[0])
    D = []

    # Construimos una matriz identidad reducida en la que las columnas c1 y c2 se combinan
    for j in range(columnas):
        fila = [0] * (columnas - 1)  # matriz determinante tendrá una columna menos
        if j == c1:
            fila[c1] = 1
        elif j == c2:
            fila[c1] = 1  # la segunda columna también contribuye a la nueva
        elif j < c2:
            fila[j] = 1
        else:
            fila[j - 1] = 1
        D.append(fila)

    return D



# Realiza todas las reducciones suficientes posibles sobre una matriz de canal. Devuelve la matriz del canal reducido.
# EXPLICACION:

#while cambio: → se repite mientras se encuentre al menos una combinación posible.
# for c1 y for c2 → se prueban todas las parejas de columnas (c1, c2).
# columnas_reductibles() → verifica si esas columnas son combinables (según tus criterios de reducción suficiente).
# canal_determinante_para_combinar() + canal_en_serie() → genera la nueva matriz del canal reducido (fusionando las columnas elegidas).
# cambio = True y break → si se hizo una reducción, vuelve a empezar el proceso con la nueva matriz reducida.


def canal_reducido(canal):
    cambio = True

    while cambio:
        cambio = False
        columnas = len(canal[0])

        # Intentar combinar todas las parejas posibles de columnas
        for c1 in range(columnas - 1):
            for c2 in range(c1 + 1, columnas):
                if columnas_reductibles(canal, c1, c2):
                    D = canal_determinante_para_combinar(canal, c1, c2)
                    canal = canal_en_serie(canal, D)
                    cambio = True
                    break  # Reiniciar búsqueda desde el principio
            if cambio:
                break

    return canal




# Verifica si una matriz representa un canal uniforme. Un canal es uniforme si cada fila es una permutación de la primera fila.
# Ejemplo de uniforme: 
# [0.2, 0.5, 0.3]
# [0.3, 0.2, 0.5]
# [0.5, 0.3, 0.2]
def canal_uniforme(canal):
    primera = sorted(canal[0])  # ordenamos la primera fila

    for fila in canal[1:]:
        if sorted(fila) != primera:
            return False
    return True



# Calcula la capacidad de un canal determinante.
# C=log2​(s) donde s es el número de salidas distintas efectivamente utilizadas.
def capacidad_determinante(canal):
    salidas_distintas = set()
    for fila in canal:
        salidas_distintas.add(tuple(fila))
    s = len(salidas_distintas)
    return log2(s)


# Calcula la capacidad de un canal sin ruido (canal perfecto).
# C=log2(r) donde r = número de entradas (o salidas, si son iguales).
def capacidad_sin_ruido(canal):
    r = len(canal)
    return log2(r)




# Calcula la capacidad de un canal uniforme.
# C=log2​(s)−H(fila) donde s es el número de salidas y
# H(fila)=−∑pj log2(pj) es la entropía de una fila.
def capacidad_uniforme(canal):
    fila = canal[0]
    s = len(fila)
    H = 0
    for p in fila:
        if p > 0:
            H -= p * log2(p)
    return log2(s) - H




# Estima la capacidad de un canal binario (2xN) probando valores de p(x1) desde 0 hasta 1 con el paso especificado. Devuelve (capacidad_estimada, probabilidad_asociada).

# EXPLICACION:
# Se recorre p(x1) desde 0 hasta 1 en pasos del tamaño dado.
# Para cada valor de p(x1):
# Se calcula p(y) (probabilidad total de cada salida).
# Luego se calcula I(X;Y) sumando sobre todas las combinaciones entrada-salida.
# Se guarda el valor máximo de información mutua y la probabilidad correspondiente.
# Devuelve la capacidad estimada y el p(x1) asociado.
def capacidad_binaria(canal, paso):
    mejor_I = 0
    mejor_p = 0
    p = 0.0

    while p <= 1.000001:  # cubrir 1.0 al final
        # probabilidades de entrada
        px = [p, 1 - p]

        # calcular p(y) para cada salida y
        num_salidas = len(canal[0])
        py = [0.0] * num_salidas
        for j in range(num_salidas):
            for i in range(2):
                py[j] += px[i] * canal[i][j]

        # calcular I(X;Y)
        I = 0
        for i in range(2):
            for j in range(num_salidas):
                if canal[i][j] > 0 and py[j] > 0:
                    I += px[i] * canal[i][j] * log2(canal[i][j] / py[j])

        if I > mejor_I:
            mejor_I = I
            mejor_p = p

        p += paso

    return mejor_I, mejor_p






# Calcula la probabilidad de error aplicando la regla de decisión de máxima posibilidad. Parámetros: p_entrada: lista con las probabilidades a priori P(x_i)
# canal: matriz con P(y_j | x_i) 
# Retorna: probabilidad de error promedio

# EXPLICACION:
# Se recorre cada salida yj.
# Para cada posible entrada xi, se calcula el producto: P(xi​)P(yj​∣xi​)
# Se elige el mayor de esos valores (la decisión correcta según la regla de máxima posibilidad).
# La suma de esos máximos sobre todas las salidas da la probabilidad total de decisión correcta.
# Finalmente: Pe​=1−P(decision correcta)



def prob_error_max_posibilidad(p_entrada, canal):
    num_entradas = len(canal)
    num_salidas = len(canal[0])
    prob_correcta = 0

    for j in range(num_salidas):
        # Calcular P(x_i) * P(y_j|x_i) para cada posible entrada
        productos = [p_entrada[i] * canal[i][j] for i in range(num_entradas)]
        # Tomar el máximo → decisión correcta
        prob_correcta += max(productos)

    # Probabilidad de error = 1 - probabilidad de decisión correcta
    return 1 - prob_correcta




