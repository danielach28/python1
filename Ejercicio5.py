''' 5. Escribe un programa que genere una multiplicación de dos números del 2 al 10 al azar, pregunte por el resultado y diga si se ha dado 
la respuesta correcta  o no es correcta, y en este caso escribir la correcta.'''

import random

# Un número aleatorio entre 2 y 10 (ambos incluidos)
numero1 = random.randint(2, 10)
numero2 = random.randint(2, 10)

multiplicacion = numero1 * numero2

resultado = int(input("Cual es el resultado de multiplicar " + str(numero1) +"*" +str(numero2) + "\n6"))
if resultado == multiplicacion:
    print("La respuesta es correcta")
else:
    print ("La respuesta no es correcta")
