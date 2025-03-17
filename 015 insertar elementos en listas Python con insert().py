# Lista original de colores
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

# Usamos el metodo 'insert()' para insertar 'magenta' después de 'lila'.
# 'lila' está en la posición -4 (contando desde el final), por lo que 'magenta' va a la posicion siguiente (-3)
colores.insert(-3, 'magenta')

# Usamos el metodo 'insert()' para insertar 'turquesa' en la penultima posición.
# La penultima posición se puede obtener con el índice -2
colores.insert(-2, 'turquesa')

# Imprimimos la lista despues de añadir los nuevos colores
print(colores)

