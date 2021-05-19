# Repaso de listas 
# Las listas son Mutables
nombres = ['Harry','Ron', 'Hemerson']
# imprimir toda la lista
print(nombres)
#imprimir el segundo elemento de la lista i=1
# [i=0, i=1, i=2.....]
print (nombres[1])
# Si es lista se puede modificar un elemeto?
# Modifica rla LIsta numeros en el tercer elemento por LUis

nombres[2] = 'Luis'
print(nombres)

# Agregar un nombre a la lista

nombres.append('Daniel')
print(nombres)

# ordenar la lista 
nombres.sort()
print(nombres)
nombres.remove('Daniel')
print(nombres)

# append(item) -> Adicionar un elemento
# sort()  -> ordenar la lista
# remove(item) -> Remover un elemento
# reverse() -> Nos invierte los elementos de la lista
nombres.reverse()
print(nombres)

# tuplas
tupla_ejemplo = (4,6,7)
print(tupla_ejemplo)
# esto no se puede hacer tupla_ejemplo(1) = 5 por ser tupla

# Definir diccionarios
# calificaciones = {'la clave' : el valor}
calificaciones = {'pedro' : 3.8, 'maria': 4.5, 'luis' : 4.8}
print(calificaciones)
print(calificaciones['pedro'])
calificaciones['maria'] = 4.2
print(calificaciones)
