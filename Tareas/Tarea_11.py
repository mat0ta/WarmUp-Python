# Realizamos los imports
import random

# Declaramos las variables
repeticiones = 10000
variables = ['salario', 'compañeros', 'distancia', 'comodidad', 'flexibilidad', 'vacaciones']

# Functions
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

# Output: Realiza la selección de importancia tras realizar la simulación de Montecarlo