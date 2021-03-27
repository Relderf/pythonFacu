frase_orig = """
Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
un montón de archivos con fotos de una manera compleja. Tal vez quieras
escribir alguna pequeña base de datos personalizada, o una aplicación
especializada con interfaz gráfica, o UN juego simple. 
"""

lista = []
frase = frase_orig.lower().split(' ')
for palabra in frase:
    if lista.count(palabra) == 0:
        if ((palabra[len(palabra)-1] == ',') | (palabra[len(palabra)-1] == '.')):
            palabra = palabra[:(len(palabra)-1)]
        lista.append(palabra)
print()
print('Palabras distintas encontradas:')
for palabra in lista:
    print(palabra)
