# Write code below 💖
import random
question = input('Preguntame queride:  ')
answer = random.randint(1,9)

if answer == 1:
  print('Magic 8 Ball:        Sí definitivamente.')
elif answer == 2:
  print('Magic 8 Ball:        Es decididamente así.')
elif answer == 3:
  print('Magic 8 Ball:        Sin duda.')
elif answer == 4:
  print('Magic 8 Ball:        Respuesta confusa, intenta otra vez.')
elif answer == 5:
  print('Magic 8 Ball:        Pregunta de nuevo más tarde.')
elif answer == 6:
  print('Magic 8 Ball:        Mejor no decirte ahora.')
elif answer == 7:
  print('Magic 8 Ball:        Mis fuentes dicen que no.')
elif answer == 8:
  print('Magic 8 Ball:        Las perspectivas no son tan buenas.')
else:
  print('Magic 8 Ball:        Muy dudoso.')
