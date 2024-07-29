morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

def cifrar_morse(texto):
    texto = texto.upper()  # Convertir el texto a mayúsculas
    codigo_morse = []
    for char in texto:
        if char in morse_code_dict:
            codigo_morse.append(morse_code_dict[char])
        else:
            codigo_morse.append(char)  # Conservar caracteres que no están en el diccionario tal como están
    return ' '.join(codigo_morse)

# Solicitar al usuario que ingrese el texto a cifrar
texto_para_cifrar = input("Ingrese el texto que desea cifrar en código Morse: ")
codigo_morse = cifrar_morse(texto_para_cifrar)
print("Texto cifrado en código Morse:")
print(codigo_morse)