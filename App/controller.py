"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv
from pprint import pprint
from DISClib.ADT import map as m
import datetime as dt
import tracemalloc
import time
from DISClib.DataStructures import listiterator as it



"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo

def iniciar():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    analizator = model.newAnalyzer()
    return analizator

# Funciones para la carga de datos
def loadEvents(analyzer,tipo):
    """
    Carga los datos de los archivos CSV context_content_features-small en el modelo
    """
    userfile = cf.data_dir + "context_content_features-small.csv"

    input_file = csv.DictReader(open(userfile, encoding="utf-8"),
                                delimiter=",")
    for event in input_file:
        newdict = {"instrumentalness":float(event["instrumentalness"]),
        "liveness":float(event["liveness"]),
        "speechiness":float(event["speechiness"]),
        "danceability":float(event["danceability"]),
        "valence":float(event["valence"]),
        "loudness":float(event["loudness"]),
        "tempo":float(event["tempo"]),
        "acousticness":float(event["acousticness"]),
        "energy":float(event["energy"]),
        "artist_id":event["artist_id"],
        "track_id":event["track_id"],
        "created_at":dt.datetime.strptime(event["created_at"], '%Y-%m-%d %H:%M:%S').time(),
        "user_id":event["user_id"],
        "id":event["id"]
        }        
        #prueba
        
        
        
        """newdict = {tipo:event[tipo],"id":event["id"]}
        print(newdict["created_at"])"""
        
        model.addCrime(analyzer, newdict, tipo)
    
    print("",len(tipo)*"-","\n",tipo, "check\n",len(tipo)*"-","\n")

    return analyzer

def loadSentiment(analyzer):
    userfile = cf.data_dir + "sentiment_values.csv"

    input_file = csv.DictReader(open(userfile, encoding="utf-8"),
                                delimiter=",")
    for hashtag in input_file:
        if hashtag["vader_avg"] != "":
            newdic = {"hashtag": hashtag["hashtag"], "vader": float(hashtag["vader_avg"])}
            model.addSentiment(analyzer, newdic)


def loadUser(analyzer):
    userfile = cf.data_dir + "user_track_hashtag_timestamp-small.csv"

    input_file = csv.DictReader(open(userfile, encoding="utf-8"),
                                delimiter=",")

    for track in input_file:
        
        newdicc = {"track_id":track["track_id"],"hashtag":track["hashtag"].lower()}
        model.addUser(analyzer,newdicc)

# Requerimientos

def req1(analyzer,carac,mink,maxk):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    
    #req
    (a,b) = model.req1(analyzer,carac,mink,maxk)
    b = m.size(b)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    print("time",delta_time,"memory",delta_memory)
    
    return (a,b)

def req2(analyzer,mne,mxe,mnd,mxd):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    
    #req
    req = model.req2(analyzer,mne,mxe,mnd,mxd)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    print("time",delta_time,"memory",delta_memory)
    return req

def req3(analyzer, minimus, magnus, minima, magna):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    
    #req
    req = model.req3(analyzer, minimus, magnus, minima, magna)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    print("time",delta_time,"memory",delta_memory)
    return req
    

def req4(analyzer,generos):

    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    
    #req
    req = model.req4(analyzer,generos)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    print("time",delta_time,"memory",delta_memory)
    return req

def req5(analyzer,minn,maxx):

    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    #req
    (b, req) = model.req5(analyzer,minn,maxx)


    print("\n °°°°°° Req No. 5 results °°°°°°")
    print("There is a total of", req["bien"], "reproductions, and", req["docs"], "reproductions according to the 'Reto 3' Document, between ", minn, "and", maxx, "\n")
    
    del req["bien"]
    del req["docs"]
    
    print("~~~~~~~~~~~~~~~~~~~~~~~ GENRES SORTED REPRODUCTIONS ~~~~~~~~~~~~~~~~~~~~~~~")
    mayor = req["mayorn"]
    gmayor = req["mayorg"]
    del req["mayorn"]
    del req["mayorg"]
    i = 1
    for a in req:
        print("Genre", i, ":", a.title(), "with", req[a]["reps"], "reps.")
        i += 1

    print("\n The TOP GENRE is", gmayor, "with", mayor, "reproductions. \n")

    print("~~~~~~~~~~~~~~~~~~~~~~~", gmayor.upper(), "SENTIMENT ANALYSIS ~~~~~~~~~~~~~~~~~~~~~~~")
    print(gmayor.title(), "has", req[gmayor]["unique"], "unique tracks.")
    print("The first TOP 10 tracks are: \n")
    top = 0
    newnew = it.newIterator(b)
    while it.hasNext(newnew):
        elem = it.next(newnew)
        print("TOP",top+1,"track:",elem[0],"with",elem[1],"hashtags and VADER =",round(elem[2],1))
        top += 1

    #print(req)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    print("time",delta_time,"memory",delta_memory)
    return req

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def indexHeight(analyzer):
    return model.indexHeight(analyzer)

def indexSize(analyzer):
    return model.indexSize(analyzer)

def minKey(analyzer):
    return model.minKey(analyzer)

def maxKey(analyzer):
    return model.maxKey(analyzer)


#pruebas

#analyzer = iniciar()
#data = loadEvents(analyzer,"created_at")

#data = loadEvents(analyzer,"energy")
#dataU = loadUser(analyzer)

#"print("reqcontrol",model.req2(analyzer,0.5,0.75,0.75,1))
#"""print("prueba max key", model.maxKey(analyzer["created_at"]))
#""print("prueba min key", model.minKey(analyzer["created_at"]))"""
#print(model.sortHash(analyzer))



def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
