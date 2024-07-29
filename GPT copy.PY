biblioteca = ['1. Fundación', '2. Rayuela', '3. 2001, Odisea espacial', '4. Hielo y fuego']

print('''Bienvenido a la biblioteca universal
''')

respuesta = input('Desea ver nuestro catalogo? s/n: ')

while respuesta.upper() != 'S':
    respuesta = input('No te puedes escapar de esta, intenta de nuevo. s/n: ')
else:
    for libro in biblioteca:
        print(f'''{libro}''')
        
prestamo1 = int(input('''
Cual de los libros desea prestar?: '''))

while prestamo1 < 0 or prestamo1 > 4:
    prestamo1 = int(input('''
Intenta de nuevo, cual de los libros desea prestar?: '''))
else:
    if prestamo1 == 1:
        print(f'''
Usted ha prestado el libro "{biblioteca[0]}" 
              ''')
        biblioteca.pop(0)
        print('Libros que quedan en catalogo: ')
        for libro in biblioteca:
            print(f'''{libro}''')
    elif prestamo1 == 2:
        print(f'''
Usted ha prestado el libro "{biblioteca[1]}" 
              ''')
        biblioteca.pop(1)
        print('Libros que quedan en catalogo: ')
        for libro in biblioteca:
            print(f'''{libro}''')
    elif prestamo1 == 3:
        print(f'''
Usted ha prestado el libro "{biblioteca[2]}" 
              ''')
        biblioteca.pop(2)
        print('Libros que quedan en catalogo: ')
        for libro in biblioteca:
            print(f'''{libro}''')
    else:
        print(f'''
Usted ha prestado el libro "{biblioteca[3]}" 
              ''')
        biblioteca.pop(3)
        print('Libros que quedan en catalogo: ')
        for libro in biblioteca:
            print(f'''{libro}''')