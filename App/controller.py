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
    Carga los datos de los archivos CSV context_content_features-small-small en el modelo
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
        "mode":event["mode"],
        "key":event["key"],
        "artist_id":event["artist_id"],
        "tweet_lang":event["tweet_lang"],
        "track_id":event["track_id"],
        "created_at":event["created_at"],
        "lang":event["lang"],
        "time_zone":event["time_zone"],
        "user_id":event["user_id"],
        "id":event["id"]
        }
        #prueba
        """newdict = {tipo:event[tipo],"id":event["id"]}
        print(newdict)"""
        model.addCrime(analyzer, newdict, tipo)
    
    cantidad = len(tipo)
    mases = cantidad*"-"
    print(mases,".....>")
    print(tipo, "check")
    print(mases,".....>")

    return analyzer

# Requerimientos

def req1(analyzer,carac,mink,maxk):
    (a,b) = model.req1(analyzer,carac,mink,maxk)
    b = m.size(b)
    return (a,b)

def req2(analyzer,mne,mxe,mnd,mxd):
    return model.req2(analyzer,mne,mxe,mnd,mxd)

def req3(analyzer, minimus, magnus, minima, magna):
    
    return model.req3(analyzer, minimus, magnus, minima, magna)

def req4(analyzer,generos):
    model.req4(analyzer,generos)

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

"""analyzer = iniciar()
data = loadEvents(analyzer,"instrumentalness")
data = loadEvents(analyzer,"energy")
data = loadEvents(analyzer,"danceability")
print("reqcontrol",model.req2(analyzer,0.5,0.75,0.75,1))"""