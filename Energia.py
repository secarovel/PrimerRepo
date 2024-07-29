televisor_lg = 0.2
televisor_samsung = 0.17
televisor_lgN = 0.15
Doce_bombillaG = 0.004 * 12
lavadora = 4.0
ps4 = 0.0
wii = 0.024
xbox = 0.264
Pc = 0.4
Nevera = 28.8
tcasa = 0.0

consumo_mensual = (televisor_lgN * 4 + televisor_samsung * 3 + televisor_lg * 2 + Doce_bombillaG * 4 + ps4 + wii + xbox + Pc + tcasa) * 30 + lavadora + Nevera
print (f'{consumo_mensual} kW/h')