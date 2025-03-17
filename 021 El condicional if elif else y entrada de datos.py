# Pedimos al usuario que ingrese su edad y la convertimos a entero
edad = int(input('Cual es tu edad?\n'))

# Verificamos si la edad es un valor valido
if edad <= 0:
    print('Nadie puede tener esa edad.')
elif edad >= 1 and edad < 18:
    print('Eres menor de edad.')
elif edad >= 18 and edad <= 45:
    print('Tienes entre 18 y 45 anos.')
elif edad > 45 and edad < 100:
    print('Eres mayor de 45 anos.')
elif edad >= 100 and edad <= 120:
    print('Has vivido mas de un siglo.')
else:
    print('Edad no valida.')

