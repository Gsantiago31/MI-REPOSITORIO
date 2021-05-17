# Inicio de condicional

# Caso  : La sentencia 'if'
# Caso : Ahorro

ahorro = float(input('Escriba lo que tiene ahorrado : '))

if ahorro > 0:

        if ahorro < 1000000:
           ahorro = ahorro * 1.10
        elif ahorro < 3000000:
           ahorro = ahorro * 1.07
        elif ahorro < 10000000:
           ahorro = ahorro * 1.05
        else:
          ahorro = ahorro * 1.03
        
        print('El ahorro se a incrementado en :', ahorro)

   
else :
        print ('su ahorro es menor a cero')
