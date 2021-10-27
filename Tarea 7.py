# Realizamos los imports
import random

for i in range(0, 50 + 1):
    print(i)

# Declaramos las variables de la Tarea 5
dinero = 2000
precioHelado = 100
edad = 18
hambre = edad
helado = 20 # Suponemos que el helado te satisface un 20%

# Importamos el código de la Tarea 5
edad = random.randint(0, 50)
print(edad)

if edad >= 85:
    print('No tienes hambre')
else: 
    if float(dinero) >= float(precioHelado) and float(hambre) < 85.0:
        satisfaccion = 85.0 - float(hambre)
        cantidadAComer = float(satisfaccion) / float(helado)
        cantidadAComer = cantidadAComer.__round__() + 1
        for i in range(1, cantidadAComer + 1):
            print(i)
            dinero = float(dinero) - float(precioHelado)
            precioAñadido = float(precioHelado) * 0.20
            precioHelado += float(precioAñadido)
            hambre += helado
        if cantidadAComer == 1:
            print('Has comido 1 helado. Ahora estás un ' + str(hambre) + '%' + ' satisfecho y tienes ' + str(dinero) + '€; por lo que:')
        else:
            print('Has comido ' + str(cantidadAComer) + ' helados. Ahora estás un ' + str(hambre) + '%' + ' satisfecho y tienes ' + str(dinero) + '€; por lo que:')
        if float(hambre) < 85.0:
            print('Sigues teniendo hambre')
        else:
            print('Ya no tienes hambre')
