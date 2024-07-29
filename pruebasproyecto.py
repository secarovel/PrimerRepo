"""colores = ['Amarillo', 'Azul', 'Rojo', 'Blanco', 'Negro']

for numero, color in enumerate(colores, start=1):
    print(f'{numero}. {color}')
    
micolor = int(input('Cual es tu color?: '))

scolor = colores[micolor - 1]

print(f'Tu color es el {scolor.lower()}')

#Probemos con planetas

planetas =['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter']

for indice, planeta in enumerate(planetas, start=1):
    print (f'{indice}. {planeta}')
    
Miplaneta = int(input('Selecciona el numero de tu planeta: '))

Splaneta = planetas[Miplaneta - 1]

print(Splaneta)"""

planetas =['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter']

for numero, planeta in enumerate(planetas, start=1):
    print(f'{numero}. {planeta}')
    
miplaneta = input('Escribe tu planeta: ')

if miplaneta.capitalize() in planetas:
    print(f'Tu planeta es {miplaneta} y esta en la lista')
else:
    print(f'El planeta {miplaneta} no esta en la lista')