# Declaramos las variables
customer_basket_cost = 125
customer_basket_weight = 44

# if statement
if float(customer_basket_cost) > 100.0:
    print('El precio total de la compra es de: ' + str(customer_basket_cost) + '€ (Envío gratutito)')
else:
    shippingPrice = float(customer_basket_weight) * 1.2
    totalPrice = float(customer_basket_cost) + shippingPrice
    print('El precio total ' + str(totalPrice) + '€ (Precio de envio: ' + str(shippingPrice) + ')')