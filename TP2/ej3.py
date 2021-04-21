texto = 'Este es un texto de prueba con palabras de distinto tipo, coala, macaco, a la olla el macaco, uno, dos, tres, a, b, c'
print ('Ingrese una letra:')
letra = input()
palabras = texto.split(' ')
print('\nPalabras que empiezan con '+letra+':')
for p in palabras:
    if p[0] == letra:
        if p[len(p)-1] == ',':
            p = p[:(len(p)-1)]
        print('    '+p)
print()
