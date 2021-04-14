import csv
from collections import Counter

arc_netflix = open("netflix_titles.csv", "r", encoding='utf-8')
arc_pelis = open("pelis_2020.csv", "w", encoding='utf-8')
csvreader = csv.reader(arc_netflix, delimiter=',')

pelis_2020 = filter(lambda x: x[1] == "Movie" and x[7] == "2020", csvreader)
writer = csv.writer(arc_pelis)
for peli in pelis_2020:
    writer.writerow([peli[2]])

#Puede ser un error volver a abrirlo para refrescarlo, solo eso se me ocurrio
arc_netflix = open("netflix_titles.csv", "r", encoding='utf-8') 

csvreader = csv.reader(arc_netflix, delimiter=',')
lista =[]
#for pais in csvreader:
#    lista.append(pais[5])
top_5 = Counter(list(map(lambda x: x[5], csvreader))).most_common(5)
print("Los 5 paises que más películas produjeron son: ")

print(*top_5, sep='\n')
#No sé por qué toma un espacio vacío "" como País, quizás no le estoy pudiendo indicar bien
#cuándo terminar y cuenta hasta vaya uno a saber donde.


arc_netflix.close()
arc_pelis.close()