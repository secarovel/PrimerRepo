clave=['.','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

frase=input("Ingresa texto a encriptar: ").lower()
encriptado=''
for i in range (0,len(frase)):
    if frase[i] in clave:
        encriptado=encriptado+str(clave.index(frase[i]))
    else:
        encriptado=encriptado+frase[i]
print(encriptado)