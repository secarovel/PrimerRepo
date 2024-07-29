# Write code below 💖
import random

ph = random.randint(0, 15)
ph = int(input('Ingresa el PH: '))

if ph > 7:
  print('Basic')
elif ph < 7:
  print('Acidic')
else:
  print('Neutral')