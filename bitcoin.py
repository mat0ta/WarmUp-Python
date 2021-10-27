# Exports
from typing_extensions import runtime

# Declaramos las variables
investment_in_bitcoin = 1.2
bitcoin_to_usd= 63000
usd_to_auro = 0.86

# Creamos la función para pasar de Bitcoin a USD y a su vez a EURO
def usdToEuro():
    bitcoinToUsd = (float(investment_in_bitcoin) * int(bitcoin_to_usd))
    bitcoinToEuro = (float(bitcoinToUsd) * float(usd_to_auro))
    print("Posees " + str(investment_in_bitcoin) + " Bitcoin(s) valorados en " + str(bitcoinToEuro) + " €")

    if float(bitcoinToEuro) < float(30000.0):
        print("Alerta: El valor de tu(s) Bitcoin(s) está por debajo de los 30,000 €")
    else:
        print("Alerta: El valor de tu(s) Bitcoin(s) está por encima de los 30,000 €")

usdToEuro()
# Output: Posees 1.2 Bitcoin(s) valorados en 65016.0 €
#         Alerta: El valor de tu(s) Bitcoin(s) está por encima de los 30,000 €