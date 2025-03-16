# Definir la lista de colores
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

# Eliminar 'azul' por �ndice positivo
del colores[1]  # 'azul' est� en la posici�n 1

# Eliminar 'marr�n' por �ndice positivo (despu�s de eliminar 'azul', su �ndice cambia)
del colores[3]  # Ahora 'marron' est� en la posici�n 3

# Eliminar 'negro' usando un �ndice negativo (-4 en la lista actual)
del colores[-4]

# Eliminar 'rosa' usando otro �ndice negativo (-3 en la lista actual)
del colores[-3]

# Imprimir la lista despues de las eliminaciones
print("Lista despues de eliminar colores:", colores)
