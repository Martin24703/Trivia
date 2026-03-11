puntos = 0

usuario = input('ingrese su nombre')
print(f'bienvenido al juego', {usuario})

primera_pregunta = input('cual es la capital de paraguay? a) capiata b) carapegua c) asuncion')
if (primera_pregunta == 'c' or primera_pregunta == 'c'):
    puntos += 1 
    segunda_pregunta = input('en que departamento esta ita?: a) central b) itapua c) guaira')
    if (segunda_pregunta == 'a' or segunda_pregunta == 'c'):
        puntos += 1
    tercera_pregunta = input('cual es la capital de argentina?: a) usuaia b) buenos aires c) cordoba')
    if (tercera_pregunta == 'b' or tercera_pregunta == 'b'):
        puntos += 1
else: 
    print('incorrecto')