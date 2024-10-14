
''' 2. Escribe un programa que pregunte el nombre y después de que el usuario lo introduzca muestre por pantalla el nombre 
en mayúsculas y el número de caracteres que tiene. Después deberá escribir el nombre tantas veces como letras contiene el nombre en líneas distintas. '''


nombre = input("Cuál es tu nombre? ")
longitud = len(nombre)
print (nombre.upper() + " número de caracteres: " + str(longitud))

for i in range(longitud):
    print(nombre)

