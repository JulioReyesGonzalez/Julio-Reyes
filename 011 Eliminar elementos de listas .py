# Definir la lista de colores
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

# Eliminar 'azul' por índice positivo
del colores[1]  # 'azul' está en la posición 1

# Eliminar 'marrón' por índice positivo (después de eliminar 'azul', su índice cambia)
del colores[3]  # Ahora 'marron' está en la posición 3

# Eliminar 'negro' usando un índice negativo (-4 en la lista actual)
del colores[-4]

# Eliminar 'rosa' usando otro índice negativo (-3 en la lista actual)
del colores[-3]

# Imprimir la lista despues de las eliminaciones
print("Lista despues de eliminar colores:", colores)
