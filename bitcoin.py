# Exports
from typing_extensions import runtime

# Declaramos las variables
bitcoin_to_usd= 63000
usd_to_auro = 0.86

# Creamos la función para pasar de Bitcoin a USD y a su vez a EURO
def usdToEuro():
    bitcoinAmount = input('Introduce la cantidad de Bitcoin que posees: ')
    while not str(bitcoinAmount).replace('.', '', 1).isdigit() and not str(bitcoinAmount).isdigit():
        bitcoinAmount = input('Introduce una cantidad apropiada: ')
    bitcoinToUsd = (float(bitcoinAmount) * int(bitcoin_to_usd))
    bitcoinToEuro = (float(bitcoinToUsd) * float(usd_to_auro))
    print("Posees " + str(bitcoinAmount) + " Bitcoin(s) valorados en " + str(bitcoinToEuro) + " €")

    if float(bitcoinToEuro) < float(30000.0):
        print("Alerta: El valor de tu(s) Bitcoin(s) está por debajo de los 30.000 €")

usdToEuro() 
# Output: Posees 1.2 Bitcoin(s) valorados en 65016.0 €
#         Alerta: El valor de tu(s) Bitcoin(s) está por encima de los 30,000 €