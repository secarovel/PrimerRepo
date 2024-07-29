Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

Q1 = int(input('''Te gusta el amanecer o el atardecer?: 
1. Amanecer
2. Atardecer
'''))
if Q1 == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif Q1 == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print('Respesta incorrecta')

Q2 = int(input('''Cuando muera, quiero que la gente me recuerde como alguién...: 
1. Bueno
2. Sensacional
3. Sabio
4. Intrepido
'''))
if Q2 == 4:
  Gryffindor += 2
elif Q2 == 3:
  Ravenclaw += 2
elif Q2 == 1:
    Hufflepuff += 2
elif Q2 == 2:
    Slytherin += 2
else:
    print('Respesta incorrecta')

if Gryffindor > Ravenclaw and Gryffindor > Hufflepuff and Gryffindor > Slytherin:
    print("Eres de Gryffindor")
else:
    print("Eres de los otros")