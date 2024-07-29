# Write code below 💖
pesos = int(input('Cuanto te sobra en pesos?: '))
soles = int(input('Cuanto te sobra en soles?: '))
reales = int(input('Cuanto te sobra en reales?: '))

dolares = int((pesos / 4125) + (soles / 3.84) + (reales / 5.67))
print(dolares)