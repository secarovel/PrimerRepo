biblioteca = ['Fundación', 'Rayuela', '2001, Odisea espacial', 'Hielo y fuego']

print('''Bienvenido a la biblioteca universal
''')

respuesta = input('Desea ver nuestro catalogo? s/n: ')

while respuesta.upper() != 'S':
    respuesta = input('No te puedes escapar de esta, intenta de nuevo. s/n: ')
else:
    for numero, libro in enumerate(biblioteca, start=1):
        print(f'''{numero}. {libro}''')
        
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
        for numero, libro in enumerate(biblioteca, start=2):
            print(f'''{numero}. {libro}''')
    elif prestamo1 == 2:
        print(f'''
Usted ha prestado el libro "{biblioteca[1]}" 
              ''')
        biblioteca.pop(1)
        print('Libros que quedan en catalogo: ')
        for numero, libro in enumerate(biblioteca, start=1):
            print(f'''{numero}. {libro}''')