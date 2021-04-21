nombres = """'Agustin',
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

eval1 = """81,
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

eval2 = """30,
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
#Generar una estructura con los nombres de los estudiantes y la suma de ambas.
#Calcular el promedio de las notas totales e informar quiénes obtuvieron menos que el promedio.

alumnos_sucio = nombres.split('\n')
notas1 = eval1.split('\n')
notas2 = eval2.split('\n')
suma = []
alumnos = []
for pri, sec in zip(notas1, notas2):
    if ((len(pri) != 0) & (len(sec) != 0)):
        pri.strip()
        sec.strip()
        if (pri[-1] == ','):
            pri = pri[:(-1)]
        if (sec[-1] == ','):
            sec = sec[:(-1)]     
        resultado = (int(pri) + int(sec))
        suma.append(resultado)
for alu in alumnos_sucio:
    if (len(alu) != 0):
        if (alu[-1] == ','):
            alu = alu[:-1]
        alu = alu.strip("\' ")
        alumnos.append(alu)
alumnos_y_notas = []
for nom, nota in zip(alumnos, suma):
    alumnos_y_notas.append((nom,nota))
print(alumnos_y_notas)
print('\n')

total = 0
for nota in suma:
    total += nota
promedio = total / len(suma)
print('Promedio: ' + str(round(promedio,2)))
print('Los siguientes alumnos están por debajo del promedio')
for alum in alumnos_y_notas:
    if (alum[1] < promedio):
        print('\t' + str(alum[0]) + ' con ' + str(alum[1]))
