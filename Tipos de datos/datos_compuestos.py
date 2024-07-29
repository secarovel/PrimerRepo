#Las istas indexa desde el 0 y se enlista dentro de []

lista = ["10 de sptiembre", "Un día antes del aniversario 22", 11, "Septiembre"]
print (lista[3])
print (lista[2])

tupla = ("10 de sptiembre", "Un día antes del aniversario 22", 11, "Septiembre")

#tupla[2] = "never"    NO se puede modificar los valores asignado en tupla
lista[2] = "Jamas"

print (lista[2])
print (tupla[2])

#creando un conjunto {set} (No se puede llamar elementos por su indice, no se pueden repetir elementos)
conjunto = {"10 de sptiembre", "Un día antes del aniversario 22", 11, "Septiembre"}
print (conjunto)
#print (conjunto[2]) -> No puede acceder al elemento

#Creando diccionario {dict} (La estructura es key : value y se separa por comas)
diccionario = {
    'nombre' : "sebastián",
    'apellido' : "rojas",
    'edad' : 29,
    'Le gusta aprender' : True
}

print (diccionario['Le gusta aprender'])