lista_de_nombres_1 = """
'Agustin',
 'Alan',
 'Andrés',
 'Ariadna',
 'Bautista',
 'CAROLINA',
 'CESAR',
 'David',
 'Diego',
 'Dolores',
 'DYLAN',
 'ELIANA',
 'Emanuel',
 'Fabián',
 'Facundo',
 'Facundo',
 'FEDERICO',
 'FEDERICO',
 'GONZALO',
 'Gregorio',
 'Ignacio',
 'Jonathan',
 'Jonathan',
 'Jorge',
 'JOSE',
 'JUAN',
 'Juan',
 'Juan',
 'Julian',
 'Julieta',
 'LAUTARO',
 'Leonel',
 'LUIS',
 'Luis',
 'Marcos',
 'María',
 'MATEO',
 'Matias',
 'Nicolás',
 'NICOLÁS',
 'Noelia',
 'Pablo',
 'Priscila',
 'TOMAS',
 'Tomás',
 'Ulises',
 'Yanina'
"""

lista_de_nombres_2 = """
'Agustin',
 'AGUSTIN',
 'Agustín',
 'Ailen',
 'Alfredo',
 'Amalia',
 'Ariana',
 'Bautista',
 'Braian',
 'Carla',
 'CESAR',
 'Daniel',
 'Diego',
 'ELIANA',
 'Facundo',
 'Facundo',
 'Facundo',
 'Facundo',
 'Federico',
 'Federico',
 'Flavia',
 'Francisco',
 'Germán',
 'Guido',
 'GUSTAVO',
 'Hilario',
 'Ignacio',
 'IVAN',
 'Jimmy',
 'Joaquín',
 'Jose',
 'Josue',
 'JUAN',
 'Juan',
 'Laura',
 'LAURA',
 'Lautaro',
 'Lautaro',
 'Ludmila',
 'Marcos',
 'Marcos',
 'MARIANELA',
 'MARTIN',
 'MATEO',
 'Mateo',
 'Matias',
 'MAURO',
 'Maximiliano',
 'NESTOR',
 'Nicolas',
 'Pedro',
 'Ramiro',
 'Sofía',
 'Tobias',
 'Tomás',
 'Tomás',
 'Ulises',
 'Yanina'
"""
lista_de_notas1 = """
81,
 60,
 72,
 24,
 15,
 91,
 12,
 70,
 29,
 42,
 16,
 3,
 35,
 67,
 10,
 57,
 11,
 69,
 12,
 77,
 13,
 86,
 48,
 65,
 51,
 41,
 87,
 43,
 10,
 87,
 91,
 15,
 44,
 85,
 73,
 37,
 42,
 95,
 18,
 7,
 74,
 60,
 9,
 65,
 93,
 63,
 74
"""
lista_de_notas2 = """
30,
 95,
 28,
 84,
 84,
 43,
 66,
 51,
 4,
 11,
 58,
 10,
 13,
 34,
 96,
 71,
 86,
 37,
 64,
 13,
 8,
 87,
 14,
 14,
 49,
 27,
 55,
 69,
 77,
 59,
 57,
 40,
 96,
 24,
 30,
 73,
 95,
 19,
 47,
 15,
 31,
 39,
 15,
 74,
 33,
 57,
 10
"""

#Indique los nombres que se encuentran en ambos. Nota: pruebe utilizando list comprehension.
lista_noms1 = []
lista_noms2 = []

nombres1 = lista_de_nombres_1.split('\n')
for nom in nombres1:
    if (len(nom) != 0):
        if (nom[-1] == ','):
            nom = nom[:-2]
        nom = (nom.strip('\', '))
        lista_noms1.append(nom)

nombres2 = lista_de_nombres_2.split('\n')
for nom in nombres2:
    if (len(nom) != 0):
        if (nom[-1] == ','):
            nom = nom[:-2]
        nom = (nom.strip('\', '))
        lista_noms2.append(nom)

print(lista_noms1)
print(lista_noms2)
#lista_ambos = []
#for nom1 in lista1:
#    for nom2 in lista2:
#        if nom1.lower() == nom2.lower():
#            if (lista_ambos.count(nom1) == 0):
#                lista_ambos.append(nom1)

set_ambos = set(lista_noms1).intersection(lista_noms2)
print('\nNombres en ambas listas:')
#print(lista_ambos)
print(set_ambos)

#Genere dos variables con la lista de notas que se incluyen en los archivos: nombres_1, eval1.txt
#y eval2.txt e imprima con formato los nombres de los estudiantes con las correspondientes
#nota y la suma de ambas como se ve en la imagen

print('\n')
lista_eval1 = []
lista_eval2 = []
eval1 = lista_de_notas1.split('\n')
for eval in eval1:
    if (len(eval) != 0):
        if (eval[-1] == ','):
            eval = eval[:-1]
        eval = (eval.strip())
        lista_eval1.append(int(eval))

eval2 = lista_de_notas2.split('\n')
for eval in eval2:
    if (len(eval) != 0):
        if (eval[-1] == ','):
            eval = eval[:-1]
        eval = (eval.strip())
        lista_eval2.append(int(eval))

print(lista_eval1)
print(lista_eval2)
indice = -1
print('  ' + 'Nombre'.center(20,' ') + 'Nota 1'.center(12,' ') + 'Nota 2'.center(10,' ') + 'Nota 2'.center(10,' ' ))
for nombre, nota1, nota2 in zip(lista_noms1, lista_eval1, lista_eval2):
    indice = indice + 1
    total = nota1 + nota2
    print('{:2} {:15} {:10} {:10} {:10}'.format(indice, nombre, nota1,nota2, total))


