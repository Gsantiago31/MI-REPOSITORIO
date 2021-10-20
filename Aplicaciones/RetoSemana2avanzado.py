Diametro_polea = float(input("Digite aquí el diámetro de la polea en centímetros "))
Valor_pi = float(3.14159)

Avance_por_vuelta = (Diametro_polea*Valor_pi)
print("Cada vuelta que da la polea, la puerta avanza " , Avance_por_vuelta , "cm\n")
print("¿Cuántas vueltas deben darse para cerrar la puerta completamente?\n")
Tamaño_puerta = float(input("Digite el tamaño de la puerta en centímetros \n"))

Recorrido = (Tamaño_puerta*Tamaño_puerta)
Recorrido_puerta = (Recorrido+Recorrido)
Recorrido_final =  (Recorrido_puerta ** (0.5))

Vueltas_necesarias = (Recorrido_final/Avance_por_vuelta)

print("Para levantar por completo la puerta se requiere de " , Vueltas_necesarias , "vueltas\n")

Chewbaccas_necesarios = (Vueltas_necesarias/3)
print("Si cada Chewbacca puede dar tres vueltas a la polea, ¿cuántos se necesitan para levantar la puerta?\n")
print("Se necesitan " , Chewbaccas_necesarios , "Soldados Chewbaccas\n")

print("¿En cuanto tiempo desea que se cierre la puerta?")
Tiempo_estimado = float(input("Digite el tiempo deseado (debe ser en segundos) "))

Velocidad_tiempo_polea = (Recorrido_final/Tiempo_estimado)

print("La polea debe girar a " , Velocidad_tiempo_polea,"centímetros por segundo para cerrarse en" , Tiempo_estimado,"segundos")

