# Inicio de condicional

# Caso  : La sentencia 'if'
# Caso : Ahorro

nombre_producto_1 = (input('Escriba el nombre del primer producto 1 : '))
precio_producto_1 = int(input('Escriba el precio del producto 2 : '))
nombre_producto_2 = (input('Escriba el nombre del segundo producto : '))
precio_producto_2 = int(input('Escriba el precio del producto 3 : '))
nombre_producto_3 = (input('Escriba el nombre del tercer producto : '))
precio_producto_3 = int(input('Escriba el precio del producto : ' ))

if precio_producto_1 > precio_producto_2 and precio_producto_1 > precio_producto_3:
 print('El precio del producto 1 es el mayor', ahorro)
elif precio_producto_2 > precio_producto_1 and precio_producto_2 > precio_producto_3:
   print('El precio del producto 2 es el mayor')
elif precio_producto_3 > precio_producto_1 and precio_producto_3 > precio_producto_2:
   print('El precio del producto 3 es el mayor')
else:
  print('los precios son iguales')
