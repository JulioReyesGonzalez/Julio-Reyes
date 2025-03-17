# Definimos una lista con varios colores
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

# Convertimos la lista en una tupla usando la funcion tuple()
colores_tupla = tuple(colores)

# Imprimimos el tipo de datos de la nueva variable para asegurarnos de que es una tupla
print(type(colores_tupla))  # Esto imprimira: <class 'tuple'>

# Imprimimos la tupla para verificar que conserva los mismos elementos que la lista original
print(colores_tupla)  

