import string

alfabeto = list(string.ascii_lowercase)


def cifrado_cesar(alfabeto,n,text):
    texto_cifrado = ""
    for letra in text:
        if letra in alfabeto:
            indice_actual = alfabeto.index(letra)
            indice_cesar = indice_actual + n
            if indice_cesar > 25:
                indice_cesar -= 25
            texto_cifrado += alfabeto[indice_cesar]
        else:
            texto_cifrado += letra
    return texto_cifrado
frase = "hola"
frase_cifrada = cifrado_cesar(alfabeto,3,frase)

print (frase_cifrada)