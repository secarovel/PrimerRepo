print('BANCO DE VALENTINA')
pin = int(input('Ingresa tu contraseña: '))

while pin != 1234:
    pin = int(input('Contraseña incorrecta, vuelve a intentar: '))

if pin == 1234:
    print('Bienvenido a su cuenta del BANCO DE VALENTINA')