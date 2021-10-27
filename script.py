# Imports
import random
import datetime

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
f.write("Este es un documento .txt\n")
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