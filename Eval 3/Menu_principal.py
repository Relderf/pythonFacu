import csv
import os.path
import os
import json
import PySimpleGUI as sg

carpeta_datasets = "datasets"
carpeta_archivos = 'archivos'
path_main = os.path.join(os.getcwd(), carpeta_datasets)
path_archivos = os.path.join(os.getcwd(), carpeta_archivos)


def crear_archivo_juegos():
    """ Inicializa variables relacionadas al archivo de juegos, abre el dataset correspondiente,
    lo procesa conforme el criterio establecido y deja a disposición del usuario un archivo
    con dicha información, en formato .json."""
    
    nombre_archivo_juegos = "android-games.csv"
    archivo_palabras_juegos = 'mining_juegos.json'
    
    if os.path.exists(os.path.join(os.getcwd(), carpeta_datasets)):
        try:
            nombre_archivo_juegos = open(os.path.join(path_main, nombre_archivo_juegos), "r", encoding="utf-8")
        except (FileNotFoundError):
            print('El archivo dataset (' + nombre_archivo_juegos + ') '
                + 'debe estar en la carpeta "' + carpeta_datasets + '", dentro del directorio del archivo .py')
        except: 
            print('Pasó algo. Fijate que los archivos estén bien, haceles un tecito y no les cambies el nombre')
    else:
        print('Se necesita una carpeta "' + carpeta_datasets + '" en el directorio del archivo .py')
        exit()
    
    data_juegos = csv.reader(nombre_archivo_juegos, delimiter=',')
    header_juegos , datos_juegos = next(data_juegos), list(data_juegos)
    
    nombre_archivo_juegos.close()
    path_juegos = os.path.join(carpeta_archivos, archivo_palabras_juegos)
    
    juegos_de_mesa = list(sorted(map(lambda y: y[1], filter(lambda x: x[8] == 'GAME BOARD', datos_juegos)), key=lambda z: z[2]))[:14]
    
    if os.path.exists(os.path.join(os.getcwd(), carpeta_archivos)):
        with open(path_juegos, 'w') as j:
            json.dump(juegos_de_mesa, j, indent=4)
        print('Archivo de juegos creado con éxito.')
    else:
        print('Se necesita una carpeta "' + carpeta_archivos + '" en el directorio del archivo .py')
        exit()
    
    #----------Otras opciones para listados de información----------
    #def presente_en_tupla(campo, dato):    
    #"""Método genérico para valores de diccionario con tuplas"""
    #    if not campo == '':
    #        for p in campo.split(','):
    #            if p.strip() == dato:
    #                return True
    #buscado = "Knight"
    #juegos_knight = list(set(map(lambda y: y[1], filter(lambda x: presente(x[1], buscado), datos_juegos))))
    #juegos_knight = list(set(map(lambda y: y[1], filter(lambda x: buscado in x[1], datos_juegos))))
    #print(*sorted(juegos_knight, reverse= True)[:10], sep='\n')
    
    
def crear_archivo_tweets():
    """ Inicializa variables relacionadas al archivo de tweets, abre el dataset correspondiente,
    lo procesa conforme el criterio establecido y deja a disposición del usuario un archivo
    con dicha información, en formato .json."""
    
    nombre_archivo_tweets = "tweets.csv"
    archivo_palabras_tweets = 'mining_tweets.json'

    if os.path.exists(os.path.join(os.getcwd(), carpeta_datasets)):
        try:
            nombre_archivo_tweets = open(os.path.join(path_main, nombre_archivo_tweets), "r", encoding="utf-8")
        except (FileNotFoundError):
            print('El archivo dataset (' + nombre_archivo_tweets + ') '
                + 'debe estar en la carpeta "' + carpeta_datasets + '", dentro del directorio del archivo .py')
        except: 
            print('Pasó algo. Fijate que los archivos estén bien, haceles un tecito y no les cambies el nombre')
    else:
        print('Se necesita una carpeta "' + carpeta_datasets + '" en el directorio del archivo .py')
        exit()

    dict_tweets = []
    for i in csv.DictReader(nombre_archivo_tweets):
        dict_tweets.append(dict(i))
    
    nombre_archivo_tweets.close()
    path_tweets = os.path.join(carpeta_archivos, archivo_palabras_tweets)
    
    #Voy a elegir bajar al json todos los valores de los diccionarios, para esta tarea, porque no estaba seguro qué se pedía.
    #Pero queda claro que sé cómo sacarlos (para el otro csv solo dejé en el json el dato que quiero usar, dejo ambas opciones
    # para que conste que sé hacerlo)
    twits_famosos = list(sorted(dict_tweets, key=lambda e: int(e['replies_count']), reverse=True))
    twiteros_famosos = []
    nicks = set()
    while len(twits_famosos) > 0 and len(twiteros_famosos) < 14:
        twit = twits_famosos.pop(0)
        if twit['username'] in nicks:
            continue
        else:
            twiteros_famosos.append(twit)
            nicks.add(twit['username'])

    if os.path.exists(os.path.dirname(path_main + os.sep + carpeta_archivos)):
        with open(path_tweets, 'w') as j:
            json.dump(twiteros_famosos, j, indent=4)
        print('Archivo de tweets creado con éxito.')
    else:
        print('Se necesita una carpeta "' + carpeta_archivos + '" en el directorio del archivo .py')
        exit()
    
    #----------Otras opciones para listados de información----------
    #tweets_respondidos = list(filter(lambda x: int(x[7]) > 0, datos_tweets))[:10]
    #print(*tweets_respondidos, sep='\n')
    #print(*dict_tweets[:10], sep='\n\n')
    #palabras_tweets = list(map(lambda x: x['username'], filter(lambda y: int(y['replies_count']) > 0, dict_tweets)))[:14]
    #with_twits = filter(lambda y: int(y['replies_count'])>0, dict_tweets)
    #twits = [next(with_twits) for i in range(14)]
    #print(*twiteros_famosos, sep='\n\n')
    
    
def main():
    """ Inicializa el programa y mantiene abierta una ventana con opciones para crear un archivo
    json con información sobre juegos del Playstore, para crear un archivo json con información
    sobre tweets sobre covid en India, o para salir del programa.
    Los botones generan 14 resultados cada uno. Esto condice con una cierta lógica que tomamos
    para el MemPy en mi grupo, en el cual no son necesarios más de eso, debido a las
    combinaciones de dificultad y tamaños de tableros que decidimos usar."""

    layout = [[sg.Button('Generar archivo de tweets famosos sobre Covid en India', 
                        key='tweets', size=(30,3))],
            [sg.Button('Generar archivo con nombres de juegos de mesa en Playstore', 
                        key='juegos', size=(30,3))],
            [sg.Button('Salir', size=(30,3))]]

    sg.theme('DarkGreen')
    window = sg.Window('Hola profe Clau', layout, no_titlebar=True)

    while True:
        event, values = window.read()
        if event == 'Salir':
            break
        elif event == 'tweets':
            crear_archivo_tweets()
        elif event == 'juegos':
            crear_archivo_juegos()
        else:
            pass
    window.close()


if __name__ == '__main__':
    main() 