# -*- coding: utf-8 -*-
#-------Ejercicio 7---------
#En Python realice el cálculo de Pi, mediante sumas sucesivas.

#Usamos la Formula Leibniz
# X= 4 - 4/3 + 4/5 - 4/7 + 4/9 - ....

igual, aux = 0, 0

texto = input("Ingrese una palabra: ")
for ind in reversed(range(0, len(texto))):
  if texto[ind].lower() == texto[aux].lower():
    igual += 1
  aux += 1


if len(texto) == igual:
  print("VERDADERO")
else:
  print("FALSO")