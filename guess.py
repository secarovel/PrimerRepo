adivina = 0
tries = 0

while adivina != 7 and tries < 3:
    adivina = int(input('Carajo vamos con esto, ¡ADIVINA!'))
    tries += 1
    
if adivina == 7 and tries == 3:
    print('Casi que no pendejo')
elif adivina == 7 and tries ==2:
    print('A la segunda tontin')
elif adivina == 7:
    print('Lo lograste camarada gil')
else:
    print('te quedo grande esta pendejada, fallaste')