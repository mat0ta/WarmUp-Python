# Importamos el codigo de la tarea shipping.py
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