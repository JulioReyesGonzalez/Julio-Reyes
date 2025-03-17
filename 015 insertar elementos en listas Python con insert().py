# Lista original de colores
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

# Usamos el metodo 'insert()' para insertar 'magenta' despu�s de 'lila'.
# 'lila' est� en la posici�n -4 (contando desde el final), por lo que 'magenta' va a la posicion siguiente (-3)
colores.insert(-3, 'magenta')

# Usamos el metodo 'insert()' para insertar 'turquesa' en la penultima posici�n.
# La penultima posici�n se puede obtener con el �ndice -2
colores.insert(-2, 'turquesa')

# Imprimimos la lista despues de a�adir los nuevos colores
print(colores)

