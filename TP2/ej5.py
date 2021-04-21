frase = input('Ingresa una frase: ')
string = input('Ingresa un string: ')
cantidad = frase.lower().split(' ').count(string.lower())
print('"' + string + '" está ' + str(cantidad) + ' veces en la frase.')
