"""
b) Escribir una función que indique si dos fichas de dominó encajan o no.
Las fichas son recibidas en una cadena, por ejemplo: 3-4 2-5.
Nota: utilizar la función split de las cadenas.
"""


def domino(token):
    token = token.split()
    token_1 = token[0].split("-")
    token_2 = token[1].split("-")
    return (token_1[0] == token_2[0] or token_1[0] == token_2[1]
            or token_1[1] == token_2[0] or token_1[1] == token_2[1])