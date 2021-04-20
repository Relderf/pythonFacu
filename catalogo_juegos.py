import csv
from collections import Counter

# Ayuda para el punto 2
#import requests

#juego = "Gloomhaven"
#icon_url = "https://cf.geekdo-images.com/original/img/lDN358RgcYvQfYYN6Oy2TXpifyM=/0x0/pic2437871.jpg"
#icono = requests.get(icon_url)
#with open(f'ejemplos/clase6/{juego}.jpg', 'wb') as f:
#    f.write(icono.content)


archivo = open("bgg_db_1806.csv", "r", encoding='utf-8')
csvreader = csv.reader(archivo, delimiter=',')

next(csvreader)
pocos_jugadores = list(filter(lambda x: int(x[5]) < 3 and "Card Game" in x[17], csvreader))
#print('Juegos con menos de 3 jugadores: ')
#print(*pocos_jugadores, sep='\n')


archivo = open("bgg_db_1806.csv", "r", encoding='utf-8')

csvreader = csv.reader(archivo, delimiter=',')
next(csvreader)
juegos = list(csvreader)
#3 name
#12 rating
#13 url

juegos_por_nombre = {r[3]: r for r in juegos}
mas_votados = Counter({r[3]: r[12] for r in juegos}).most_common(10)

for key, value in mas_votados:
    print(f"[{key}]\n\tPuntaje: {value}\n\tImagen: {juegos_por_nombre[key][13]}")


archivo.close()