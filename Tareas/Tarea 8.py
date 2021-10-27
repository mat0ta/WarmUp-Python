# Declaramos las variables del ejercicio de butcoin.py
investment_in_bitcoin = 1.2
bitcoin_to_usd= 63000
usd_to_auro = 0.86

# Importamos el código de bitcoin.py (He hecho algo precido directamente en la primera actividad, pero lo repito)
def bitcoinToEuros(monto_bitcoin, valor_bitcoin_euros):
    liquidez =  float(monto_bitcoin) * float(valor_bitcoin_euros)
    if float(liquidez) < float(30000.0):
        print("Alerta: El valor de tu(s) Bitcoin(s) está por debajo de los 30.000 € (" + str(liquidez) + "€)")
    return liquidez

bitcoinToEuros(1, 25000)