## GUIA DE TEORIA DE LA INFORMACION

Fuentes:

**Informacion fuente** [_Obtiene la informacion de una fuente a partir de las probabilidades_](fuente.py#L8)
**Informacion base N** [_Obtiene In(S)_](fuente.py#L16)
**Entropia fuente** [_Obtiene la entropia de la fuente_](fuente.py#L26)
**Entropia binaria** (fuente.py#L39)
**Generar alfabeto y probabilidades** [_A partir de una cadena devuelve el alfabeto junto con sus probabilidades_](fuente.py#L53)
**Genera palabra** [_Genera palabra basandose en probabilidades_](fuente.py#L70)
**Extension orden N** [_Genera la extension de orden N de una fuente_](fuente.py#L82)
**Entropia fuente de Markov** [_Consigue la entropia de una fuente de markov_](fuente.py#L107)

Matriz de transicion:

**Vector Estacionario** [_Genera el vector estacionario_](matrizTransicion.py#L12)
**Genera matriz de transicion** [_Genera la matriz de transicion_](matrizTransicion.py#L37)
**Genera palabra** [_Genera palabra a partir de la matriz de transicion_](matrizTransicion.py#L67)
**Memoria nula** [_Determina si la fuente es de memoria nula_](matrizTransicion.py#L89)

Canales:

**Matriz del canal** [_Genera la matriz del canal partiendo de una cadena de entrada y una de salida_](canales.py#L18)
**Probabilidades a priori** [_P(ai) calcula las probabilidades a priori (o probabilidades marginales) de los símbolos de entrada._](canales.py#L57)
**Probabilidades a posteriori** [_P(ai/bj) Devuelve las probabilidades de los simbolos de salida partiendo de las probabilidades a priori y la matriz del canal_](canales.py#L80)
**Matriz Posteriori** [_Devuelve una matriz con las probabilidades a posteriori del canal partiendo de las probabilidades a priori y la matriz del canal_](canales.py#L97)
**Matriz Conjunta** [_P(ai, bj) Devuelve una matriz con las probabilidades de los eventos simultáneos_](canales.py#L150)
**Entropias a posteriori** [_H(A/Bj) Devuelve una lista con las entropias a priori a partir de las probabilidades a priori y la matriz de prob. condicionales_](canales.py#L188)
**Ruido de un canal** [_H(A/B) calcula la Entropía Condicional de la Fuente dada la Salida (H(X|Y)), también conocida como la Equivocación o Ruido del Canal._](canales.py#L223)
**Perdida de un canal** [_calcula la Entropía Condicional de la Salida dada la Entrada (H(Y|X)), también conocida como la Pérdida o Equivocación de la Fuente._](canales.py#L266)
**Entropia Afin de un canal** [_El código calcula la Entropía de la Salida (H(Y))_](canales.py#L299)
**Informacion mutua de un canal** [_MIDE I(X,Y)_](canales.py#L335)
**Canal sin ruido** [_Determina si un canal tiene ruido o no_](canales.py#L378)
**Canal determinante** [_Determina si un canal es determinante o no_](canales.py#L412)
**Canal en serie** [_Retorna la matriz resultado del producto matricial canal1 . canal2_](canales.py#L440)
**Columnas reductibles** [_Verifica si las columnas c1 y c2 de la matriz canal pueden combinarse en una reducción suficiente (son proporcionales o idénticas)_](canales.py#L486)
**Canal determinante para combinar** [_Genera la matriz determinante necesaria para combinar las columnas c1 y c2 de la matriz 'canal'._](canales.py#L519)
**Canal reducido** [_Realiza todas las reducciones suficientes posibles sobre una matriz de canal. Devuelve la matriz del canal reducido._](canales.py#L550)
**Canal uniforme** [_Determina si un canal es uniforme o no_](canales.py#L578)
**Capacidad determinante** [_Calcula la capacidad de un canal determinante. (C)_](canales.py#L590)
**Capacidad sin ruido** [_Calcula la capacidad de un canal sin ruido (C)_](canales.py#L600)
**Capacidad Uniforme** [_Calcula la capacidad de un canal uniforme (C)_](canales.py#L610)
**Capacidad Binaria** [_Estima la capacidad de un canal binario (C)_](canales.py#L631)
**Probabilidad de error** [_Calcula la probabilidad de error (Pe) aplicando la regla de decisión de máxima posibilidad_](canales.py#L689)

Codigos:
**Es no singular** [_Determinar si todas las palabras del código son únicas_](codigos.py#L11)
**Es instantaneo** [_Determina si un codigo es instantaneo_](codigos.py#L35)
**Es univoco** [_Determina si un codigo es univocamente decodificable_](codigos.py#L60)
**Get alfabeto Codigo** [_Obtiene el alfabeto codigo a partir de palabras_](codigos.py#L106)
**Get longitudes** [_Obtiene las longitudes de las palabras codigo_](codigos.py#L119)
**Inecuacion de Kraft** [_verifica si un codigo cumple la inecuacion de kraft_](codigos.py#L131)
**Longitud media** [_Devuelve la longitud media de un codigo_](codigos.py#L151)
**Es compacto** [_determina si un codigo es compacto_](codigos.py#L168)
**Genera Mensaje** [_Genera mensaje codigo_](codigos.py#L182)
**1er Teorema Shannon-Fano** [_Verifica si un codigo cumple el primer teorema de Shannon_](codigos.py#L197)
**Codigo de Huffman** [_Genera un codigo de Huffman basandose en las probabilidades_](codigos.py#L227)
**Codigo de Shannon-Fano** [_Genera códigos binarios para cada símbolo usando el algoritmo de Shannon–Fano_](codigos.py#L275)
**Genera msg codificado** [_Genera un bytearray que contiene el mensaje codificado_](codigos.py#L336)
**Decodifica mensaje** [_Dada una secuencia de bytes, decodifica y retorna el mensaje original_](codigos.py#L367)
**Tasa de compresion** [_Tasa de compresion = N:1_](codigos.py#L400)
**Compresion RLC** [_Comprime un mensaje usando RLC y devuelve un bytearray_](codigos.py#L426)
**Distancia de Hamming** [_Devuelve la distancia de Hamming (minima) entre las cadenas (caracteres codificados) de una lista_](codigos.py#L464)
**Errores detectables** [_Devuelve la cantidad de errores detectables_](codigos.py#L486)
**Errores corregibles** [_Devuelve la cantidad de errores corregibles_](codigos.py#L490)
**ASCII con paridad** [_Retorna un byte que represente el código ASCII (7 bits) y utilice el bit menos significativo para almacenar la paridad del código_](codigos.py#L505)
**Byte con errores** [_detecta si un byte con paridad tiene un error de 1 bit_](codigos.py#L536)
**Codifica con paridades** [_Dada una cadena de caracteres, generar una secuencia de bytes (bytearray) que contenga su representación con código ASCII y sus bits de paridad vertical, longitudinal y cruzada._](codigos.py#L587)
**Decodifica con paridades** [_verifica si el conjunto tiene errores_](codigos.py#L662)
**Rendimiento y redundancia del codigo** [_Rendimiento (η) y Redundancia (R)_](codigos.py#L707)

**Apuntes:**

- Huffman sirve para obtener un codigo instantaneo optimo dado un alfabeto codigo binario
- Codigo instantaneo -> es posible decodificar las palabras de una secuencia sin precisar el conocimiento de los símbolos que las suceden
- Shannon-Fano -> procedimiento subóptimo para construir un código, que alcanza una cota de L ≤ H(S) + 2

  **_Compresion_**
  La compresión es el proceso de reducir el tamaño de un archivo para ahorrar espacio o tiempo de transmisión. Se basa en que la mayoría de los datos tienen redundancia, es decir, información que se repite o es predecible.

        Compresión sin pérdida
        - Los datos descomprimidos son idénticos a los originales.
        - Es imprescindible en textos, código fuente, bases de datos o imágenes donde la exactitud es crítica.
        - Permite tasas de compresión moderadas.
        - Está limitada por la entropía, una medida de la incertidumbre de la fuente.
        - No puede usar códigos con longitud promedio menor que la entropía.
        Métodos típicos:
            Shannon-Fano
            Huffman (estático, semi-estático, dinámico)
            RLC (Run Length Coding, aunque su desempeño depende del tipo de datos)
            Pueden ser:
                Estáticos
                Semi-estaticos
                Dinamicos o adaptativos

        Compresion con perdida
        - Los datos descomprimidos no son exactamente iguales, pero sí similares.
        - Permite compresiones muy altas.
        - Aquí no existe limitación de entropía, porque se descarta información "irrelevante" según el modelo perceptual.

        RLC:
        - Aunque suele considerarse “sin pérdida”, su efectividad depende mucho de los datos.
        - Idea: cada vez que un símbolo se repite muchas veces, se reemplaza por el par → (símbolo, cantidad de repeticiones)
        - Funciona muy bien cuando hay largas secuencias de símbolos iguales, como en imagenes en blanco y negro.
        - En texto casi siempre empeora la compresión, porque las repeticiones largas son raras.

La compresión sin pérdida usa modelos probabilísticos y códigos óptimos para representar datos exactamente, mientras que la compresión con pérdida sacrifica exactitud para lograr compresiones mucho mayores aprovechando las características perceptuales humanas.

**_Errores_**

Por qué existen los **errores** en la comunicación?
Cuando la información viaja por un canal o se almacena en un dispositivo, puede sufrir alteraciones. En el mundo digital, eso significa que bits cambian su valor (de 0 a 1 o de 1 a 0).
Los errores pueden ser:
_Aislados_: afectan a uno o varios bits, pero separados.
_En ráfaga_: afectan a varios bits consecutivos.
Para enfrentar estos problemas, se diseñan códigos que permiten detectar o corregir errores.

Detectores:

- Permiten saber que hubo un error.
- Generalmente requieren pedir retransmisión.
- Son más simples y menos costosos.

Correctores:

- Permiten identificar qué bits fallaron y corregirlos sin retransmisión.
- Requieren más redundancia (más bits extra).
- Son fundamentales cuando no es posible retransmitir (por ejemplo, en comunicaciones unidireccionales o en aplicaciones críticas).

**_Distancia de Hamming_**

Distancia de Hamming:
La distancia de Hamming entre dos palabras indica cuántos bits deben cambiarse para pasar de una palabra a la otra.
La distancia mínima entre todas las palabras válidas de un código determina sus capacidades
La idea es que las palabras válidas deben estar “lejos” entre sí, para que un error no las confunda.

**_Bit de paridad_**

Chequeo de Paridad (idea principal)
La paridad agrega bits extra para verificar si el número de bits en 1 es par o impar.
Es la herramienta más simple de detección de errores.
Tipos:

- VRC (Vertical Redundancy Check)
  Se agrega un bit por palabra.
  Detecta errores simples.
- LRC (Longitudinal Redundancy Check)
  Las palabras se organizan en una matriz y se calcula una paridad por columna.
  Paridad cruzada

- Un bit adicional que verifica coherencia entre VRC y LRC.

La combinación de los tres (VRC + LRC + paridad cruzada) permite:
Detectar hasta 3 errores,
Corregir 1 error simple,
Aunque errores dobles o triples se pueden detectar pero no corregir de forma unívoca.

**_Matriz de paridades_**
Los datos se acomodan en una matriz:
Cada fila tiene un bit de paridad vertical (VRC)
Cada columna tiene un bit de paridad horizontal (LRC)
Un bit final controla la paridad cruzada
Esto permite ubicar errores como si se tratara de cruzar las coordenadas de fila y columna donde falló la paridad.
Lógica:
Si solo una fila y una columna fallan, su intersección indica exactamente el bit erróneo → se corrige.
Si fallan varias filas y/o columnas → se detectan múltiples errores, pero no se puede saber exactamente cuáles bits cambiaron → solo se detecta.

**_Deteccion y correccion de errores_**
Gracias a estas paridades:

- Corrección: un error simple se identifica y corrige.
- Detección: dos o tres errores pueden detectarse, ya que rompen coherencias en las paridades.
- No se pueden corregir múltiplos, porque no es posible ubicarlos de forma inequívoca.

**_La codificación para control de errores agrega redundancia organizada. Cuanta más redundancia: mayor distancia de Hamming, más errores detectables, más errores corregibles. Pero siempre hay un costo: más bits transmitidos y mayor complejidad._**

**_Canales_**

Un canal se define por un conjunto de símbolos de entrada (lo que se envía), un conjunto de símbolos de salida (lo que se recibe) y las reglas probabilísticas que los relacionan

- Canal Discreto sin Memoria: Se asume que la salida actual depende únicamente de la entrada actual, sin ser afectada por lo que sucedió antes (sin memoria).
- La Matriz del Canal: El comportamiento del canal se describe mediante una matriz. Esta matriz contiene las probabilidades condicionales de recibir un símbolo específico dado que se envió otro. Es decir, define la "tendencia" del canal a cometer errores o transmitir correctamente.

Probabilidad de Transición: Es la probabilidad de recibir un símbolo "Y" dado que se envió "X"
Probabilidad A Priori (La Fuente): Es la probabilidad de que la fuente emita un símbolo determinado antes de que ocurra la transmisión. Es nuestro conocimiento inicial.
Probabilidad A Posteriori (La Deducción): Es la probabilidad de que se haya enviado un símbolo "X" sabiendo que ya recibimos "Y". Esta es la clave para el receptor: una vez que veo la salida, ¿qué tan probable es que provenga de cierta entrada?

Entropía A Priori: Representa la incertidumbre promedio sobre qué símbolo enviará la fuente antes de recibir nada. Es el número medio de bits necesarios para identificar el símbolo basándose solo en las estadísticas de la fuente
Entropía A Posteriori: Representa la incertidumbre que permanece después de haber observado la salida del canal
Al recibir un símbolo, nuestra incertidumbre sobre qué se envió cambia.
Si el canal es muy ruidoso, ver la salida no ayuda mucho y la entropía a posteriori sigue siendo alta
Si el canal es limpio, ver la salida nos da casi certeza de qué se envió, y la entropía baja.

El Canal (definido por su matriz) actúa como un filtro imperfecto. Partimos de una Incertidumbre Inicial (Entropía A Priori). Al pasar la información por el canal y observar el resultado, actualizamos nuestras probabilidades (a Probabilidades A Posteriori). Esta actualización modifica nuestra incertidumbre, resultando en una nueva Entropía A Posteriori, la cual nos indica qué tanta duda nos queda sobre el mensaje original tras la recepción.

Si en la clase anterior definimos la incertidumbre que nos queda después de recibir un mensaje (entropía a posteriori), la **_Equivocación H(A/B)_** es el promedio de esa duda residual.
Concepto: Mide la cantidad de información sobre la entrada que no logró cruzar el canal.
Interpretación: Es la pérdida de información causada por el canal. Si la equivocación es alta, significa que, aunque mires el resultado (salida), sigues teniendo muchas dudas sobre qué fue lo que originó ese resultado (entrada).
Ruido: En el contexto de intentar averiguar qué entró sabiendo qué salió, a esta equivocación se la denomina Ruido.

**_Información Mutua (Lo que se aprovecha)_**
Este es el concepto central de la eficiencia en la comunicación. Representa la conexión real entre la entrada y la salida.
Definición: Es la cantidad de información sobre la entrada que sí atraviesa el canal.
Como resta de incertidumbres: Se puede entender como la diferencia entre la incertidumbre total original (lo que no sabíamos antes de empezar) y la equivocación (lo que seguimos sin saber después de recibir el mensaje)
.Lo "Mutuo": Es la información compartida; la reducción de incertidumbre sobre la entrada gracias a que observamos la salida.Propiedad
clave: Nunca es negativa. Observar la salida nunca te hace saber menos que antes; en el peor de los casos (si son independientes), te quedas igual, pero no pierdes conocimiento.

**_Relaciones entre Entropías_**
Para visualizar el sistema completo, se introduce la Entropía Afín o Conjunta H(A,B), que mide la incertidumbre de todo el evento simultáneo (entrada Y salida ocurriendo juntas)
La Información Mutua no es un número fijo y estático solo del cable o medio físico; es flexible.
Depende tanto del canal (la matriz de probabilidades de error) como de la fuente (qué tan probables son los símbolos que enviamos).
Esto es crucial porque nos permite obtener un índice de "qué tan bien" estamos usando un canal. Podemos ajustar la fuente para maximizar la información mutua y así aprovechar mejor un medio de transmisión imperfecto

En resumen: Si el canal fuera perfecto, la Información Mutua sería igual a la Entropía de la fuente (todo lo que entra, se entiende). Como el canal tiene ruido, aparece la Equivocación

**_Canales perfectos_**
Canal Sin Ruido:

- Concepto: Es aquel donde, si observas la salida, sabes con certeza absoluta qué entrada se envió.
- Relación: No existe "equivocación" (H(A/B) =0). Toda la incertidumbre de la fuente se resuelve al ver la salida. Por tanto, la Información Mutua es igual a la Entropía de la Fuente. Nada se pierde en el camino.

Canal Determinante:

- Concepto: Es aquel donde cada entrada produce una única salida posible, sin dispersión.
- Relación: Si conoces la entrada, sabes con certeza qué saldrá (H(B/A)=0).
- Toda la información que llega a la salida proviene puramente de la fuente.

**_Canales en Serie_**
¿Qué pasa si la salida de un canal se convierte en la entrada de otro (A -> B -> C)?

- Acumulación de Pérdida: La intuición nos dice (y la teoría confirma) que al pasar la información por múltiples etapas, la calidad de la señal tiende a degradarse o, en el mejor de los casos, mantenerse igual.

- El Principio de Procesamiento de Datos: Nunca puedes ganar información sobre el mensaje original añadiendo más etapas de procesamiento ruidoso. La información que llega al final de la cadena (C) sobre el origen (A) siempre será menor o igual a la que había en el punto intermedio (B).

**_Canales reducidos_**
A veces, las matrices que describen los canales son muy grandes y complejas. Se busca simplificarlas agrupando varias salidas en una sola.

- El Costo de Simplificar: Generalmente, al fusionar dos salidas distintas en una sola categoría, se pierde detalle. Esto reduce la Información Mutua: simplificar el modelo suele tener el "precio" de perder información.

- Extensión del Canal: Conceptualmente opuesto a la reducción, implica mirar bloques de símbolos (secuencias) en lugar de símbolos individuales para analizar el comportamiento del canal a mayor escala.

**_Reduccion suficiente_**
Existe una excepción crucial a la regla de "simplificar es perder información".

- Condición de Suficiencia: Si dos salidas diferentes nos dan exactamente la misma información probabilística sobre qué entrada las generó (sus probabilidades a posteriori son idénticas o proporcionales), entonces son redundantes entre sí.

- El Resultado: Podemos combinar estas salidas "gemelas" en una sola sin que la Información Mutua disminuya. A esto se le llama Reducción Suficiente. Es posible tener una matriz más pequeña que sea "tan buena" como la original para transmitir información.

La información es frágil. Si encadenamos canales, la información decae (Canales en Serie). Si intentamos simplificar el canal agrupando salidas, generalmente perdemos información, a menos que detectemos redundancias específicas (Reducción Suficiente) que nos permitan simplificar el sistema manteniendo intacta su capacidad informativa.

**_Capacidad del canal_**
Hasta ahora vimos que la Información Mutua cambia si cambiamos las probabilidades de la fuente (qué tan a menudo enviamos cada símbolo). Surge entonces una pregunta: ¿Cuál es la mejor configuración posible?

Definición: La capacidad del canal es el valor máximo de información que el canal es capaz de transmitir. Representa el mayor "acople" posible entre la entrada y la salida.

- El Factor "Estratégico": La capacidad no depende solo de la física del canal (la matriz de probabilidades), sino de encontrar la distribución de entrada "perfecta" (las probabilidades a priori) que maximice la información mutua

- Casos Especiales:
  En canales con estructuras ordenadas (como los simétricos o uniformes), el cálculo se simplifica enormemente porque la entropía se vuelve predecible en función de la estructura de la matriz.

  En el Canal Binario Simétrico (BSC), la capacidad depende directamente de la probabilidad de error ($p$). Si $p=0.5$, el canal es inútil (capacidad 0); si $p=0$ o $p=1$, el canal es perfecto (capacidad máxima)

**_Mensajes Confiables en Canales No Confiables_**
Dado que los canales reales tienen ruido y no son ideales, existe el riesgo de que lo recibido no sea lo que se envió

El Objetivo: Queremos transmitir mensajes fiables a pesar de la falta de fiabilidad del medio
La Solución: Se necesitan mecanismos externos (como repetir símbolos o códigos correctores) para combatir el ruido. Esto nos lleva al concepto de "Reglas de Decisión".

**_Reglas de decision_**
Cuando el receptor ve un símbolo de salida (por ejemplo, un '0'), debe adivinar qué símbolo entró (¿fue un '0' que llegó bien o un '1' que se distorsionó?).
Definición: Una regla de decisión es una función que asigna una respuesta única ("creo que fue A") a cada símbolo de salida recibido.
El Dilema: Un canal permite muchas estrategias (reglas) diferentes para adivinar el mensaje original. ¿Cuál elegimos?

**_La Probabilidad de Error y la Regla Óptima_**
Para elegir la mejor estrategia, usamos la estadística para minimizar equivocaciones.

- Probabilidad de Error (P_E): Es el promedio de veces que nuestra regla de decisión fallará.
- La Regla de Máxima Posibilidad Condicional: Para minimizar el error, la lógica es simple: al recibir un símbolo, debemos apostar por el símbolo de entrada que tenga la mayor probabilidad a posteriori de haber causado esa salida. Es decir, si recibo "B", calculo la probabilidad de que haya venido de "A1", "A2", etc. Elijo el "A" que haga esa probabilidad más alta.
- Dependencia: Esta decisión depende de dos cosas: qué tan propenso es el canal a distorsionar (matriz) y qué tan probable era que se enviara ese símbolo en primer lugar (probabilidades a priori). Si todas las entradas son igualmente probables, simplemente elegimos el valor más alto en la columna correspondiente de la matriz del canal.

Todo canal tiene un "techo" de rendimiento (Capacidad) que alcanzamos optimizando qué enviamos. Además, del lado del receptor, la mejor forma de combatir el ruido es usar una Regla de Decisión basada en la probabilidad más alta (apostar a lo más seguro) para minimizar la Probabilidad de Error.
