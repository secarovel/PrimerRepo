planetas = ['Mercurio', 'Venus', 'Tierra', 'Marte']

for planeta in planetas:
    #While no funciona amenos que se use true and break
    if planeta != 'Marte':
        print(f'El planeta {planeta} no es correcto, intenta con otro astro.')
    else:
        print(f'El planeta {planeta} es correcto! Eres todo un marciano.')
