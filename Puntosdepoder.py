inteligencia = 0
fuerza = 0
belleza = 0

puntosmagicos = 9
puntosrestantes = 9

print(f'''Tienes {puntosmagicos} puntos asignables a cualidades
que determinaran tu desempeño en el juego.
Asigna los puntos en favor de la estrategía que mejor creas.

Intelligencia: {inteligencia}
Fuerza: {fuerza}
Belleza: {belleza}
''')

inteligencia = int(input(f'Ingresa cuantos de los {puntosmagicos} puntos le asignas a la inteligencia: '))

while inteligencia < 0 or inteligencia > 9:
    int(input(f'Ingresa un numero entre 0 y 9: '))
    
puntosrestantes -= inteligencia

print(f'''Tienes {puntosrestantes} puntos asignables a cualidades
que determinaran tu desempeño en el juego.
Asigna los puntos en favor de la estrategía que mejor creas.

Intelligencia: {inteligencia}
Fuerza: {fuerza}
Belleza: {belleza}
''')

fuerza = int(input(f'Ingresa cuantos de los {puntosrestantes} puntos le asignas a la fuerza: '))

while fuerza < 0 or fuerza > puntosrestantes:
    fuerza = int(input(f'Ingresa un numero entre 0 y {puntosrestantes}: '))
    
puntosrestantes -= fuerza

print(f'''Tienes {puntosrestantes} puntos asignables a cualidades
que determinaran tu desempeño en el juego.
Asigna los puntos en favor de la estrategía que mejor creas.

Intelligencia: {inteligencia}
Fuerza: {fuerza}
Belleza: {belleza}
''')

belleza = int(input(f'Ingresa cuantos de los {puntosrestantes} puntos le asignas a la belleza: '))

while belleza < 0 or belleza > puntosrestantes:
    belleza = int(input(f'Ingresa un numero entre 0 y {puntosrestantes}: '))
    
puntosrestantes -= belleza

print(f'''Tienes {puntosrestantes} puntos asignables a cualidades
que determinaran tu desempeño en el juego.
Asigna los puntos en favor de la estrategía que mejor creas.

Intelligencia: {inteligencia}
Fuerza: {fuerza}
Belleza: {belleza}
''')
    
