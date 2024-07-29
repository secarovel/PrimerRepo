lado_a = int(input('Ingresa el valor de el lado a del triangulo: '))
lado_b = int(input('Ingresa el valor de el lado b del triangulo: '))

hipotenusa = (lado_a ** 2 + lado_b ** 2) ** 0.5
resultado = ('la Hipotenusa del triangulo es: ') + str(hipotenusa)
print(resultado)