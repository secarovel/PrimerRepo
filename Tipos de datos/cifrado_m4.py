def cifrar_mensaje(mensaje):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    mensaje_cifrado = ""
    for letra in mensaje:
        # Si la letra no es un espacio, obtener el índice de la letra en el alfabeto y agregarlo al mensaje cifrado
        if letra != " ":
            letra = letra.lower()  # Convertir a minúscula para manejar mayúsculas y minúsculas de manera uniforme
            indice = alfabeto.index(letra) + 1  # Sumar 1 para que la 'a' sea 1 en lugar de 0
            mensaje_cifrado += str(indice) + " "
        # Si la letra es un espacio, agregarlo directamente al mensaje cifrado
        else:
            mensaje_cifrado += " "
    return mensaje_cifrado.strip()

# Pedir al usuario que ingrese un mensaje
mensaje_original = input("Ingrese el mensaje que desea cifrar: ")

# Cifrar el mensaje
mensaje_cifrado = cifrar_mensaje(mensaje_original)

# Mostrar el mensaje cifrado
print("Mensaje cifrado:", mensaje_cifrado)