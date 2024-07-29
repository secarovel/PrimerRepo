# Write code below 💖
Altura = int(input('Coloque su altura: '))
Creditos = int(input('Coloque sus creditos: '))

if Altura >= 137 and Creditos >= 10:
  print('Disfruta el viaje')
elif Altura < 137 and Creditos >= 10:
  print('No tienes la altura requerida para el viaje')
elif Altura >= 137 and Creditos < 10:
  print('No tienes los creditos necesarios para el viaje')
else:
  print('No cumples ninguno de los dos requisitos')
