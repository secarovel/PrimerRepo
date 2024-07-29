def bienvenida ():

    biblioteca = ['1. Biblia', '2. Coran', '3. Baldor', '4. Hamurabi']
    usuario = []
    
    rescat = input('''\nBienvenido a la biblioteca galactica, desea ver nuestro catalogo? s/n: ''')
    
    while rescat.lower() != 's':
        rescat = input('\nIntenta de nuevo con s/n: ')
    else:
        mostrarcatalogo (biblioteca)
    
    return biblioteca, usuario
    
def mostrarcatalogo (biblioteca):
    
    print('\nCatalogo actualizado: ')
    
    for libro in biblioteca:
        if libro is not None:
            print(f'{libro}')
          
def mostrarprestamos (usuario):         
            
    print('\nLibros del usuario, prestados: ')
            
    for libro in usuario:
        print(f'{libro}')
        
    return usuario
    
def prestarlibro (biblioteca, usuario):
    
    prestamo = int(input('\nQue libro desea prestar? Escoja un numero correspondiente a la lista: '))
    
    while prestamo < 1 or prestamo > len(biblioteca):
        prestamo = int(input(f'\nIntena de nuevo el prestamo entre los valores 1 y {len(biblioteca)}: '))
    else:
        print(f'\nHas prestado el libro {biblioteca[prestamo-1]}.')
        usuario.append(biblioteca[prestamo-1])
        biblioteca.pop(prestamo-1)
        biblioteca.insert(prestamo-1, None)
        
    return biblioteca, usuario

def devolverlibro (biblioteca,usuario):
    
    usuario = mostrarprestamos(usuario)
    
    devolucion = int(input('\nIngrese el numero del libro que quiere devolver: '))
    
    while devolucion < 1 or devolucion > len(usuario):
        devolucion = int(input('\nIntente de nuevo con un numero valido: '))
    else:
        print(f'\nUsted ha devuelto el libro {usuario[devolucion-1]}')
        biblioteca.insert(devolucion-1,usuario[devolucion-1])
        usuario.pop(devolucion-1)
        
    return biblioteca, usuario     
        
def main ():
    
    biblioteca, usuario = bienvenida ()
    
    while True:
        biblioteca, usuario = prestarlibro(biblioteca, usuario)
        
        input('\nCatalogo actalziado, presione enter: ')
        mostrarcatalogo(biblioteca)
        
        reiniciar = input('\nDesea prestar otro libro? s/n: ')
          
        if reiniciar.lower() != 's':
            break
    
    biblioteca, usuario = devolverlibro(biblioteca, usuario)
    mostrarprestamos(usuario)
    mostrarcatalogo(biblioteca)

main()

#modificación de prueba
