#-------Ejercicio 5------
#En Python paralelo despliegue verdad o falso si una apalabra es palindrome.

palabra = input("Ingrese una palabra cualquiera: ")
palabra = palabra.lower()
if str(palabra) == str (palabra)[::-1]:
  print("es Verdadero")
else:
  print("es Falso")