"""
Ejercicio 6b
Escribir funciones que dada una cadena de caracteres:
b) Devuelva solamente las letras vocales. Por ejemplo, si recibe "sin
consonantes" debe devolver "i ooae".
"""

cad = 'Sin consonantes murciélago Guadalajara San Sebastián'

def vocales(cad):
    consonantes = ""
    for letra in cad:
        if letra in "aeiouáéíóúAEIOUÁÉÍÓÚ ":
            consonantes += letra
    return consonantes

print(vocales(cad))
