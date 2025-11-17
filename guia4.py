from codigos import *;
from fuente import *;


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
    
##CHEQUEADAS
def rendimientoCodigo(probabilidades, palabras_codigo):
    return entropiaFuente(probabilidades, informacionBaseN(probabilidades, getr(palabras_codigo))) / longitudMedia(palabras_codigo, probabilidades)

def redundanciaCodigo(probabilidades, palabras_codigo):
    return 1 - rendimientoCodigo(probabilidades, palabras_codigo)

## FIN CHEQUEADAS

# alfabeto: cadena de caracteres que contenga un alfabeto fuente
# codificacion: una lista de cadenas de caracteres que almacena una codificación en el alfabeto binario
# mensaje: cadena de caracteres con un mensaje escrito en el alfabeto fuente
# devolver una secuencia de bytes (bytearray) que contenga el mensaje codificado
def ej15(alfabeto, codificacion, mensaje):
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
def ej15B(alfabeto, codificacion, byte_array):
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



#p = [0.385, 0.154, 0.128, 0.154, 0.179]


# mensaje = "58784784525368669895745123656253698989656452121702300223659"
# alfabeto, p = generaAlfabeto(mensaje)
# print("ENTROPIA: ", entropiaFuente(p, informacionBaseN(p, 2)))
# huffman = codigoHuffman(p)
# shannon = codigoShannonFano(p)
# print("Longitud: \n")
# print("HUFFMAN: ", longitudMedia(codigoHuffman(p), p), "\n")
# print("SHANNON: ", longitudMedia(codigoShannonFano(p), p), "\n")
# print("rendimiento: \n")
# print("HUFFMAN: ", rendimientoCodigo(p, codigoHuffman(p)), "\n")
# print("SHANNON: ", rendimientoCodigo(p, codigoShannonFano(p)), "\n")
# print("redundancia: \n")
# print("HUFFMAN: ", redundanciaCodigo(p, codigoHuffman(p)), "\n")
# print("SHANNON: ", redundanciaCodigo(p, codigoShannonFano(p)), "\n")

def codificar(alfabeto, palabrasCodificadas):
    