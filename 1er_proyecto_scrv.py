print('''-----------------------------------------------------------
---------- Bienvenido al juego de las decisiones ----------
-----------------------------------------------------------''')
input('Presiona Enter para continuar...')
print('''-                                                         -      
-   En este juego descubriras las glorias e infortunios   -
-     que te puedes encontrar al recorrer un universo     -
-                 de incertidumbre y azar.                -
-                                                         -
----------                Atrévete               ----------
-----------------------------------------------------------
-----------------------------------------------------------
-                                                         -
-                                                         -''')
input('Presiona Enter para continuar...')
print('''-                   Primero lo primero.                   -''')
explorador = input('''-      ¿Qué nombre quieres que tenga tu explorador?       -

                        ''')
print(f'''
Bienvenido {explorador}, comencemos preguntandote otros datos...
''')

edad = int(input('Que edad tienes?: '))

if edad < 30:
    print(f'''Tu edad, mi estimado {explorador} es la de aun un joven.
''')
else:
    print(f'la vida, mi querido {explorador}, ya te ha recorrido en un tercio')

input("Presiona Enter para continuar...")

sexos = ['Mujer', 'Hombre', 'Intersexual', 'Indeterminado']
print('De los siguientes generos, con cual te identificas?: ')
for indice, sexo in enumerate(sexos, start=1):
    print(f'{indice}. {sexo}')

sexo = int(input('Selecciona el numero que corresponda: '))

while sexo < 0 or sexo > 4:
    sexo = int(input('Selecciona un numero entre 1 y 4: '))

sexo_seleccionado = sexos[sexo - 1]
    
print(f'''
Has escogido ser {sexo_seleccionado.lower()}, explendido {explorador}.
''') 
input('Presiona Enter para continuar...')

gama = 9
inteligencia = 0
fuerza = 0
belleza = 0

print(f'''
Ahora asignemos tus puntos Gama.

Cuentas con {gama} puntos Gama, que deberas asignar entre las tres virtudes del universo Epsilon.

Inteligencia: {inteligencia}
Fuerza: {fuerza}
Belleza: {belleza}
''')
inteligencia = int(input('Ingresa un numero entre 0 y 9 para tu inteligencia: '))

while inteligencia < 0 or inteligencia > 9:
    print(f'El valor {inteligencia} no esta entre 0 y 9. ¡Intenta de nuevo!: ')
    inteligencia = int(input('Ingresa un numero entre 0 y 9 para tu inteligencia: '))
    
gamarestante = gama - inteligencia

print(f'''
Ahora cuentas con {gamarestante} puntos Gama, que deberas asignar a la virtud Fuerza del universo Epsilon.

Inteligencia: {inteligencia}
Fuerza: {fuerza}
Belleza: {belleza}
''')

fuerza = int(input(f'Ingresa un numero entre 0 y {gamarestante} para tu fuerza: '))

while fuerza < 0 or fuerza > gamarestante:
    print(f'El valor {fuerza} no esta entre 0 y {gamarestante}. ¡Intenta de nuevo!: ')
    fuerza = int(input(f'Ingresa un numero entre 0 y {gamarestante} para tu fuerza: '))
    
gamarestante -= fuerza

belleza += gamarestante

print(f'''
Al asignar {fuerza} puntos Gama a tu Fuerza, los puntos restantes Gamma han sido asinados a la virtud Belleza del universo Epsilon.

Inteligencia: {inteligencia}
Fuerza: {fuerza}
Belleza: {belleza}
''')

input('Presiona Enter para continuar...')


print(f'''
Muy bien {explorador}, con estas virtudes asignadas ahora viene la generación aleaotoria del universo en el que jugaras.

Para ello ahora al presionar enter, saltaras a uno de estos tres universos:
''') 

mundos = ['Lavionica', 'Desertiland', 'Apogeica']

for asign, mundo in enumerate(mundos, start=1):
    print(f'''{asign}. {mundo}
''')
    
input('''Presiona Enter para escoger el mundo aleatoriamente...
''')

import random

mundo = random.randint(0,2)

mundof = mundos[mundo]

print(f'''Y se ha generado automaticamente el universo {mundof.upper()}''')