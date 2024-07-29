# Diccionario para mapear caracteres a código Morse
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

# Diccionario para mapear código Morse a caracteres
morse_code_dict_reverse = {value: key for key, value in morse_code_dict.items()}

def descifrar_morse(codigo_morse):
    palabras = codigo_morse.strip().split(' / ')
    texto_descifrado = []
    for palabra in palabras:
        letras = palabra.split()
        for letra in letras:
            if letra in morse_code_dict_reverse:
                texto_descifrado.append(morse_code_dict_reverse[letra])
            else:
                texto_descifrado.append(letra)  # Conservar el espacio entre las letras
        texto_descifrado.append(' ')  # Agregar espacio entre palabras
    return ''.join(texto_descifrado).strip()

# Solicitar al usuario que ingrese el código Morse a descifrar
codigo_morse_para_descifrar = input("Ingrese el código Morse que desea descifrar (separe las palabras con '/'): ")
texto_descifrado = descifrar_morse(codigo_morse_para_descifrar)
print("Texto descifrado:")
print(texto_descifrado)