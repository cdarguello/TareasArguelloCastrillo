# MT7003
# Tarea 1
# Estudiantes:
#  -	José Rodolfo Castrillo Cubero (2020154039)
#  -	Carlos David Argüello Hidalgo (2021045923)

import string


# Toma un string y retorna otro igual donde se inviertieron mayúsculas por
#  minúsculas y viceversa
def invert_case(Cadena):
    CadenaInvert = ""
    caracterInvert = ""
    # Se verifica que la entrada sea un string
    if isinstance(Cadena, str):
        # Se verifica que la entrada no sea una string vacía
        if Cadena == "":
            # Entrada es string vacía, código de error -48
            return -48, None

        # Se verifica que la entrada solo tenga caracteres del abecedario
        for caracter in Cadena:
            if caracter not in string.ascii_letters + 'ñ':
                # Entrada con caracter no del abecedario, código de error -32
                return -32, None
            # Invertir mayúsculas/minúsculas para la letra ñ (no en ASCII)
            if caracter == "ñ":
                caracterInvert = "Ñ"
            elif caracter == "Ñ":
                caracterInvert = "ñ"
            # Invierte usando el índice de cada caracter en la concatenación
            # de las mayúsculas y minúsculas de ASCII
            elif caracter in string.ascii_lowercase:
                pos = string.ascii_lowercase.find(caracter)
                caracterInvert = string.ascii_uppercase[pos]
            else:
                pos = string.ascii_uppercase.find(caracter)
                caracterInvert = string.ascii_lowercase[pos]
            CadenaInvert += caracterInvert
        return 0, CadenaInvert

    else:
        # Entrada no es string, código de error -16
        return -16, None


def numero_primo(base):
    # variables internas
    salida = []

    # verifica que base no sea un string
    if isinstance(base, str):
        # Entrada no es un entero, código de error -64
        return -64, None
    # Verifica que base no sea Booleano
    if isinstance(base, bool):
        # Entrada no es un entero, código de error -64
        return -64, None
    # verifica que base no sea None
    if base is None:
        # Entrada no es un entero, código de error -64
        return -64, None
    # Verifica que base sea Entero
    if isinstance(base, int):
        # Verifica que base sea un número menor a 100.
        if base > 100:
            return -80, None
        else:
            for i in range(2, base + 1):
                # Repite para todos los número en rango
                divisor_found = False
                es_primo = False
                x = 2
                while not divisor_found and not es_primo:
                    # Verifica el módulo de la división de todos los números
                    # menores al número que se está probando
                    if i % x != 0:
                        x = (x + 1)
                    # Si ningún número es divisor,
                    # adjunta el número a la lista de salida
                    elif x >= i - 1:
                        salida.append(i)
                        es_primo = True
                    else:
                        # Indica si un número es divisor.
                        divisor_found = True
            return 0, salida
    else:
        # Entrada no es un entero, código de error -64
        return -64, None
