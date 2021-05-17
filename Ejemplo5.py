# Inicio de condicional

# Caso  : La sentencia 'if'
# Caso : Multiples condiciones dentro de la misma linea del if
# Si experiencia es mayor a 5 años o sabe manejar algun lenguaje como JAva , Pyton , C lo vamos a contratar, de lo contrario sera en otra oportunidad.

experiencia = int(input('Escriba los años de experiencia: '))

lenguaje = (input('Escriba el lenguaje : '))

if experiencia >= 5  or lenguaje in  ['java','python','c']:
    
        print('lo vamos a contratar')

   
else :
        print ('en otra oportunidad')
