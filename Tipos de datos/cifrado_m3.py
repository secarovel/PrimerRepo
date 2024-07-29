def cifrar_mensaje(mensaje):
    mensaje_cifrado = ""
    for letra in mensaje:
        if letra != " ": 
            # Obtener el valor ASCII de la letra
            valor_ascii = ord(letra)
            # Agregar el valor ASCII al mensaje cifrado
            mensaje_cifrado += str(valor_ascii-96) + " "
        else:
            mensaje_cifrado += " "
    return mensaje_cifrado.strip()

# Pedir al usuario que ingrese un mensaje
mensaje_original = input("Ingrese el mensaje que desea cifrar: ")

# Cifrar el mensaje
mensaje_cifrado = cifrar_mensaje(mensaje_original)

# Mostrar el mensaje cifrado
print("Mensaje cifrado:", mensaje_cifrado)