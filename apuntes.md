**PRIMER PARCIAL**

**Fuentes**

Para obtener el alfabeto de la fuente hice una funcion que recorre una cadena o mensaje y guarda en una lista los caracteres que no formen parte de la misma. Ademas, se cuenta en una lista la cantidad de apariciones del caracter dividida por la longitud del mensaje para obtener las probabilidades.

Para obtener la matriz de transicion de la fuente, se recorre toda la palabra desde el primer caracter hasta el anteultimo. Se guarda en a el caracter señalado y en b el siguiente. Luego se le suma 1 a la posicion debida de la matriz y tras recorrer toda la matriz, esta se divide por la suma de todos los elementos de la fila.

Para saber si la fuente es de memoria nula tome una fila de referencia y compare el resto de filas con ella. Si el valor en la posicion j de la fila difiere por una cantidad mayor que la tolerancia de la misma posicion pero en la fila de referencia, la matriz NO es de memoria nula. En caso contrario, continua con la ejecucion. Si finaliza el algoritmo sin haber encontrado una diferencia mayor que la tolerancia diremos que es de memoria nula.

Para conocer la entropia de la fuente debemos diferenciar si es la fuente es Markoviana o no (memoria nula o no). Si es de memoria nula, la formula a seguir es H(S) = sumatoria desde i=1 hasta n de pi _ I(i) donde pi es la probabilidad del simbolo i e I(i) es la informacion del simbolo i.
En caso de NO ser de memoria nula, para calcular la entropia se implementa la formula H(S) = sumatoria desde i = 1 hasta n de P(si) _ H(S|si) siendo P(si) la probabilidad estacionaria de estar en el estado i, H(S|si) la entropia condicional de las transiciones desde el estado i.

Para generar la extension de orden N genere una lista de productos cartesianos repetida N veces. Despues converti cada uno de esos productos cartesianos en una cadena. Cada una de esas cadenas sera un simbolo de la extension. Luego calculo las probabilidades de cada cadena resultante multiplicando las probabilidades de cada simbolo. De esta forma obtengo el alfabeto de la extension junto con su distribucion de probabilidades.

Para generar el vector estacionario hice una funcion que simula el paso del tiempo. Esta multiplica el vector estacionario por la matriz de transicion repetidamente. El algoritmo finaliza cuando el cambio entre las iteraciones es muy pequeño (ya se estabilizaron las probabilidades) o si se alcanzaron las 10000 iteraciones.

**_Conclusiones_**

    Para poder hablar de las fuentes anteriores primero debemos determinar si estas son de memoria nula o no. Si son de memoria nula, podemos decir que la probabilidad de aparicion de cada simbolo, es independiente de los demas.

    La extension de una fuente de memoria nula corresponde a una fuente donde cada elemento de su alfabeto se corresponde con una secuencia de n simbolos de la fuente inicial, siendo n el orden de la extension. Logramos determinar la probabilidad de cada elemento del alfabeto multiplicando las probabilidades de los simbolos que lo componen. La entropia de este tipo de fuentes puede calcularse igual que para las fuentes de memoria nula, dado que estas tambien son de este tipo. Como podemos observar en el ejercicio 1, las probabilidades de los simbolos de la fuente inicial, son mucho mayores a los de la extension de orden 2, y esto tiene sentido dado que en la extension tenemos mayor cantidad de simbolos.

    La entropia de las fuentes determina la informacion media por simbolo. Tambien representa la cantidad de bits (en caso de ser H2(s)) necesarios para representar el mensaje a transmitir. La entropia de las fuentes extendidas a un orden N (N > 1) es mayor a la de las fuentes originales. Esto se debe a que al aumentar la cantidad de simbolos (secuencias de caracteres), las probabilidades de aparicion de cada uno de los simbolos extendidos sera considerablemente menor a las probabilidades originales, por lo que aportaran una mayor informacion.

    La matriz de transicion determina la probabilidad de que salga un simbolo i habiendo salido antes un simbolo j. Estas matrices solo son utiles para entender las fuentes con memoria, dado que en las de memoria nula, las probabilidades de aparicion de cada simbolo son independientes. Ademas, estas matrices sirven para construir el vector de estados estacionarios. En la matriz del ejercicio 2 vemos que algunos campos tienen 0s, esto se debe a que en la palabra dada nunca vemos el simbolo j tras haberse generado el simbolo i.

    En las fuentes con memoria de Markov, la distribucion de probabilidades varia a medida que se emiten los simbolos, pero en un punto, estas probabilidades se estabilizan en lo que se conoce como estado estacionario, representado por el vector estacionario. Para que este estado pueda existir, debe existir un conjunto finito de estados, y estos estados deben ser alcanzables desde otro estado.

**CODIGOS**

Para calcular Hr(S) use dos funciones. Siendo N = r;

- informacionBaseN: Esta funcion calcula el logaritmo en base N de 1 sobre la probabilidad de aparicion del simbolo si. El resultado corresponde a la informacion con base N.
- entropiaFuente: implementa la definicion de entropia, Hr(S) = sumatoria de i=1 hasta m de P(Si) \* I(Si). Utiliza la informacion anteriormente calculada.

Para calcular la longitud media del codigo lo que hice fue: por cada palaba codigo, multiplicar la probabilidad de aparicion de esta por la longitud de la misma y acumularlo en una variable.

Para determinar si el codigo cumple con la inecuacion de Kraft, recorri la lista de palabras codigo. Por cada una de ellas, añadi a la variable "suma", 1 sobre la potencia de la longitud del alfabeto codigo a la longitud de la palabra actual. Si al terminar el algoritmo "suma" es menor o igual a 1, quiere decir que verifica la inecuacion de Kraft.

Para determinar si el codigo es compacto o no, la funcion recorre palabra por palabra verificando si la longitud de cada palabra es menor o igual que el techo del logaritmo en base 2 de 1 sobre la probabilidad de esa palabra. si todas las palabras cumplen la condicion, el codigo es compacto

Para determinar si el codigo es singular, recorre todas las palabras codigo. Si encuentra dos palabras codigo iguales, entonces el codigo es singular. Si no las encuentra, entonces es no singular.

Sabiendo que el codigo es no singular, podemos analizar si el codigo es univoco o no. Para determinarlo,

Ya sabemos que el codigo es univoco. Ahora podemos saber si es instantaneo o no. El codigo es instantaneo si ninguna palabra codigo es prefija de otra. Para determinarlo hice una funcion que recorre todas las palabras entre si, toma la palabra i y la compara con un recorte de la palabra j. Si son iguales significa que i es prefijo de j, entonces es no instantaneo

**_Conclusiones_**

    Hr(S) representa el promedio ponderado de la informacion. Es el promedio de informacion que aporta cada uno de los simbolos del codigo.

    La longitud media se define como Lm = sumatoria desde i = 1 hasta q de pi * li siendo pi la probabilidad de aparicion del simbolo i, y li la longitud de la palabra codigo i. Es muy util para determinar la eficiencia de un codigo, para la verificacion del teorema de Shannon y para calcular el costo de transmision de un mensaje. La formula es valida para las fuentes de markov y las fuentes de memoria nula. Ademas, si Lm <= longitud media de todos los codigos univocos que pueden aplicarse a la misma fuente y el mismo alfabeto, el codigo es compacto.

    Cuanto mas breve sea el codigo menos costara transmitirlo o almacenarlo, por ende es mejor.

    La inecuacion de Kraft-McMillan es la condicion suficiente para la existencia de un codigo instantaneo de longitudes l1, l2, ..., lq. La inecuacion determina si existe, pero no asegura que el codigo que armamos es instantaneo.

    Los codigos no singulares son aquellos que no contienen palabras codigo repetidas. El incumplimiento de esta condicion conduce a una gran dificultad a la hora de la decodificacion del codigo, ya que si tenemos una palabra codigo "01" que significa "a" y "b" simultaneamente, no sabremos como decodificarlo.

    Se dice que un codigo es univocamente decodificable si se puede asegurar que su extension de orden N es no singular para cualquier valor finito de N. Esto asegura que dos secuencias de simbolos cualquiera de la fuente (de igual longitud) dan lugar a secuencias de simbolos codigo distintas, lo cual hace posible su decodificacion.

    Un codigo es instantaneo si nignuna palabra codigo es prefijo de otra.  La instantaneidad del codigo permite decodificar una secuencia de simbolos sin necesidad de conocer los simbolos siguientes.
