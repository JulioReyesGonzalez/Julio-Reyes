# Definimos la lista original 'colores'
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

# Creamos una lista vacia para almacenar los colores eliminados
colores_eliminados = []

# Usamos el metodo 'pop()' para eliminar 'azul', sabemos que estz en la posición 1
# El valor de 'pop()' es el color que se elimina, asi que lo guardamos en 'colores_eliminados'
colores_eliminados.append(colores.pop(1))  # 'azul' está en la posición 1

# Usamos el metodo 'pop()' para eliminar 'blanco', sabemos que esta en la posición 8
# Lo guardamos en 'colores_eliminados'
colores_eliminados.append(colores.pop(7))  # 'blanco' esta en la posición 8

# Imprimimos la lista original despues de eliminar los colores
print("Lista de colores despues de eliminar 'azul' y 'blanco':", colores)

# Imprimimos la nueva lista que contiene los colores eliminados
print("Colores eliminados:", colores_eliminados)

