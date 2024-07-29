def descifrar_mensaje(mensaje_cifrado):
    alfabeto = 'abcdefghijklmnopqrstOuvwxyz'
    mensaje_descifrado = ""
    numeros = mensaje_cifrado.split()
    for numero in numeros:
        # Si el valor es un espacio en blanco, agregar un espacio al mensaje descifrado
        if numero == " ":
            mensaje_descifrado += " "
        else:
            # Convertir el número a entero y restar 1 para obtener el índice en el alfabeto
            indice = int(numero) - 1
            # Obtener la letra correspondiente al índice y agregarla al mensaje descifrado
            letra = alfabeto[indice]
            mensaje_descifrado += letra
    return mensaje_descifrado

# Pedir al usuario que ingrese el mensaje cifrado
mensaje_cifrado = input("Ingrese el mensaje cifrado que desea descifrar: ")

# Descifrar el mensaje
mensaje_descifrado = descifrar_mensaje(mensaje_cifrado)

# Mostrar el mensaje descifrado
print("Mensaje descifrado:", mensaje_descifrado)