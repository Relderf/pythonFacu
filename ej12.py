#La idea es tratar de programar una de las partes principales del juego “Buscaminas”. La idea
#es que dado una estructura que dice que celdas tienen minas y que celdas no las tienen, como
#la siguiente:

campo = """
'-*-*-',
'--*--',
'----*',
'*----',
"""
def sumar_en_minas (numeros, y, x):
    """ recibe numeros, Y y X, y en base a la posicion de la mina, asigna en sus posibles alrededores,
    sin irse de los límites, +1 en "numeros" a todos los casilleros aledaños. Y en el lugar de la mina, 
    setea un "*". Cada linea de suma (+1) está condicionada por un if, que chequea que esa posición
    de la matriz sea un integer, y solo intenta sumar si ese es el caso.
    Intenté usar un try_catch, pero cuando habia una excepción, si bien hice que la ignore, el cuerpo
    del if se detenía, y dejaba de sumar a los casilleros aledaños.."""
    
    if y == 0:
        if x == 0:                  #arriba a la izquierda
            numeros[y][x] = '*'
            if type(numeros[y][x+1]) == int:
                numeros[y][x+1] += 1
            if type(numeros[y+1][x]) == int:
                numeros[y+1][x] += 1
            if type(numeros[y+1][x+1]) == int:
                numeros[y+1][x+1] += 1
        elif x == len(numeros):  #arriba a la derecha
            numeros[y][x] = '*'
            if type(numeros[y][x-1]) == int:
                numeros[y][x-1] += 1
            if type(numeros[y+1][x-1]) == int:
                numeros[y+1][x-1] += 1
            if type(numeros[y+1][x]) == int:
                numeros[y+1][x] += 1
        else:                       #arriba al medio
            numeros[y][x] = '*'
            if type(numeros[y][x-1]) == int:
                numeros[y][x-1] += 1
            if type(numeros[y][x+1]) == int:
                numeros[y][x+1] += 1
            if type(numeros[y+1][x-1]) == int:
                numeros[y+1][x-1] += 1
            if type(numeros[y+1][x]) == int:
                numeros[y+1][x] += 1
            if type(numeros[y+1][x+1]) == int:
                numeros[y+1][x+1] += 1
    elif y == len(numeros):
        if x == 0:                  #abajo a la izquierda
            numeros[y][x] = '*'
            if type(numeros[y][x+1]) == int:
                numeros[y][x+1] += 1
            if type(numeros[y-1][x]) == int:
                numeros[y-1][x] += 1
            if type(numeros[y-1][x+1]) == int:
                numeros[y-1][x+1] += 1
        elif x == len(numeros[0])-1:  #abajo a la derecha
            numeros[y][x] = '*'
            if type(numeros[y][x-1]) == int:
                numeros[y][x-1] += 1
            if type(numeros[y-1][x-1]) == int:
                numeros[y-1][x-1] += 1
            if type(numeros[y-1][x]) == int:
                numeros[y-1][x] += 1
        else:                       #abajo al medio
            numeros[y][x] = '*'
            if type(numeros[y][x-1]) == int:
                numeros[y][x-1] += 1
            if type(numeros[y][x+1]) == int:
                numeros[y][x+1] += 1
            if type(numeros[y-1][x-1]) == int:
                numeros[y-1][x-1] += 1
            if type(numeros[y-1][x]) == int:
                numeros[y-1][x] += 1
            if type(numeros[y-1][x+1]) == int:
                numeros[y-1][x+1] += 1
    else:
        if x == 0:                  #centro a la izquierda
            numeros[y][x] = '*'
            if type(numeros[y][x+1]) == int:
                numeros[y][x+1] += 1
            if type(numeros[y-1][x]) == int:
                numeros[y-1][x] += 1
            if type(numeros[y-1][x+1]) == int:
                numeros[y-1][x+1] += 1
            if type(numeros[y+1][x]) == int:
                numeros[y+1][x] += 1
            if type(numeros[y+1][x+1]) == int:
                numeros[y+1][x+1] += 1
        elif x == len(numeros[0])-1:  #centro a la derecha
            numeros[y][x] = '*'
            if type(numeros[y][x-1]) == int:
                numeros[y][x-1] += 1
            if type(numeros[y-1][x-1]) == int:
                numeros[y-1][x-1] += 1
            if type(numeros[y-1][x]) == int:
                numeros[y-1][x] += 1
            if type(numeros[y+1][x-1]) == int:
                numeros[y+1][x-1] += 1
            if type(numeros[y+1][x]) == int:
                numeros[y+1][x] += 1
        else:                       #todo el centro
            numeros[y][x] = '*'
            if type(numeros[y-1][x-1]) == int:
                numeros[y-1][x-1] += 1
            if type(numeros[y-1][x]) == int:
                numeros[y-1][x] += 1
            if type(numeros[y-1][x+1]) == int:
                numeros[y-1][x+1] += 1
            if type(numeros[y][x-1]) == int:
                numeros[y][x-1] += 1
            if type(numeros[y][x+1]) == int:
                numeros[y][x+1] += 1
            if type(numeros[y+1][x-1]) == int:
                numeros[y+1][x-1] += 1
            if type(numeros[y+1][x]) == int:
                numeros[y+1][x] += 1
            if type(numeros[y+1][x+1]) == int:
                numeros[y+1][x+1] += 1


lineas = campo.split('\n')
numeros = [ [0,0,0,0,0], 
            [0,0,0,0,0], 
            [0,0,0,0,0], 
            [0,0,0,0,0], 
            [0,0,0,0,0]]
minas = [   ['-','*','-','*','-'], 
            ['-','-','*','-','-'], 
            ['-','-','-','-','-'], 
            ['-','-','-','-','*'], 
            ['*','-','-','-','-']]

fila = 0
for renglon in minas:
    colu = 0 
    for espacio in renglon:
        if espacio == '*':
            sumar_en_minas(numeros,fila,colu)
        colu += 1
    fila += 1
for renglon in numeros:
    reng = ''
    for char in renglon:
        reng += str(char) + ' '
    print(reng)



