# Definir la lista de colores
colores = ["rojo", "azul", "verde", "amarillo", "marron", "lila", "negro", "rosa"]

# Obtener el color en la posición 3 (recordando que los índices comienzan en 0)
color_pos_3 = colores[3]
print("El color en la posicion 3 es:",color_pos_3)  # Salida esperada: amarillo

# Obtener la posición del color "rojo"
pos_rojo = colores.index("rojo")

# Obtener la posición del color "rosa"
pos_rosa = colores.index("rosa")

# Imprimir las posiciones encontradas
print(f"Posicion de 'rojo': {pos_rojo}")  # Salida esperada: 0
print(f"Posicion de 'rosa': {pos_rosa}")  # Salida esperada: 7

# Crear una lista vacía con 5 posiciones
mi_lista = [None] * 5  

# Asignar los valores en las posiciones indicadas
mi_lista[4] = "uno"
mi_lista[1] = "dos"
mi_lista[0] = "tres"
mi_lista[3] = "cuatro"
mi_lista[2] = "cinco"

# Imprimir la lista resultante
print(f"Lista final: {mi_lista}")  # Salida esperada: ['tres', 'dos', 'cinco', 'cuatro', 'uno']

