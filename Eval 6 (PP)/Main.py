import pandas as pd
from matplotlib import pyplot as plt

#Enunciado 5:  dado el archivo de registros de jugadas (eventos) 
#de MemPy, mostrar un gráfico con los usuarios que más veces jugaron el juego 
#(independientemente del resultado de la partida.

archivo = "datos de prueba.csv"
data = pd.read_csv(archivo)
#print(data.groupby("Usuarie - nick").size().sort_values(ascending=False).head(6))
top = data.groupby("Usuarie - nick").size().sort_values(ascending=False).head(6)
explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05)

plt.pie(top.values, labels=top.keys(), autopct='%1.1f%%',
        shadow=True, explode=explode, startangle=180, labeldistance= 0.8)
plt.axis('equal')
plt.legend(top.keys())
plt.title("Usuaries que más partidas jugaron")
plt.show()

