# Imports
import random
import datetime

# Tarea 1
print("Roses are #ff0000 Vialoets are #0000ff why my code's working I haven't a clue")

# Tarea 2
print("\033[92mHello World\033[0m") # Empleamos el codigo de color ANSI de Python

#Tarea 3
print(21 + 43)
print(142 - 52)
print(10 * 342)
print(5**2)

# Tarea 4
altura = 200
altura += 50
print(altura)

# Tarea 5
dinero = 2000
precioHelado = 100
edad = 18
hambre = edad
helado = 20 # Suponemos que el helado te satisface un 20%

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

# Tarea 6
# Importamos shipping.py
customer_basket_cost = 101
customer_basket_weight = 44

if float(customer_basket_cost) > 100.0:
    print('El precio total de la compra es de: ' + str(customer_basket_cost) + '€ (Envío gratutito)')
else:
    shippingPrice = float(customer_basket_weight) * 1.2
    totalPrice = float(customer_basket_cost) + shippingPrice
    print('El precio total ' + str(totalPrice) + '€ (Precio de envio: ' + str(shippingPrice) + ')')

# Diagrama creado: https://matota.xyz/assets/uploads/uax/programacion-computadores/diagrama-tarea1.png

# Se observa como cuando se ejecuta el código con un valor de customer_basket_cost inferior a 100 te responde añadiendo el valor del coste de shipping mientras que 
# cuando es superior, te lo da como gratutito.

#Tarea 7
for i in range(0, 51):
    print(i)

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

# Tarea 8
# Importamos el código de bitcoin.py (He hecho algo precido directamente en la primera actividad, pero lo repito)
investment_in_bitcoin = 1.2
bitcoin_to_usd= 63000
usd_to_auro = 0.86

def bitcoinToEuros(monto_bitcoin, valor_bitcoin_euros):
    liquidez =  float(monto_bitcoin) * float(valor_bitcoin_euros)
    if float(liquidez) < float(30000.0):
        print("Alerta: El valor de tu(s) Bitcoin(s) está por debajo de los 30.000 € (" + str(liquidez) + "€)")
    return liquidez

bitcoinToEuros(1, 25000)

# Tarea 9
# Creamos el archivo flag.txt
f = open('./flag.txt', 'a')
f.write("Este es un documento .txt")
f.close()

f = open('./flag.txt', 'r')
print(f.read())
f.close()

# Tarea 10
current_time = datetime.datetime.now()
print(current_time)

# Tarea 11
repeticiones = 10000

variables = ['salario', 'compañeros', 'distancia', 'comodidad', 'flexibilidad', 'vacaciones']

def Comparativa(grado):
    importancia = [0.8, 0.5, 0.3, 0.7, 0.7, 0.8]
    resultados_finales = []
    for n in range(repeticiones):
        resultados = []
        for i in range(len(variables)):
            value = importancia[i] * (random.uniform(grado[i][0], grado[i][1]))
            resultados.append(value)
        
        resultados_finales.append(sum(resultados))
    return resultados_finales

a = Comparativa([[1,4], [1,3], [7,9], [5,7], [2,8], [3,5]])