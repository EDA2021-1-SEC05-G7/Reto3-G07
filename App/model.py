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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as m
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import orderedmap as om
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newAnalyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    analyzer = {'events': None}
    lists = ["instrumentalness","liveness","speechiness","danceability","valence","loudness","tempo","acousticness","energy"]
    for i in lists:
        analyzer[i] = om.newMap(omaptype='RBT',
                                        comparefunction=compareEvent)
                    
        analyzer['events'] = lt.newList('ARRAY_LIST', compareIds)
    return analyzer


# Funciones para agregar informacion al catalogo


def addCrime(analyzer, crime, tipo):
    """
    """
    lt.addLast(analyzer['events'], crime)
    updateDateIndex(analyzer[tipo], crime,tipo)
    return analyzer


def updateDateIndex(map, crime, tipo):
    """
    Se toma la fecha del crimen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    occurreddate = crime[tipo]
    entry = om.get(map, occurreddate)
    if entry is None:
        datentry = newDataEntry(crime)
        om.put(map, occurreddate, datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, crime,tipo)
    return map


def addDateIndex(datentry, crime,tipo):
    """
    Actualiza un indice de tipo de crimenes.  Este indice tiene una lista
    de crimenes y una tabla de hash cuya llave es el tipo de crimen y
    el valor es una lista con los crimenes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry['lstevents']
    lt.addLast(lst, crime)
    offenseIndex = datentry['eventIndex']
    offentry = m.get(offenseIndex, crime[tipo])
    if (offentry is None):
        entry = newOffenseEntry(crime[tipo], crime)
        lt.addLast(entry['eventlist'], crime)
        m.put(offenseIndex, crime[tipo], entry)
    else:
        entry = me.getValue(offentry)
        lt.addLast(entry['eventlist'], crime)
    return datentry


def newDataEntry(crime):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'eventIndex': None, 'lstevents': None}
    entry['eventIndex'] = m.newMap(numelements=30,
                                     maptype='PROBING')
    entry['lstevents'] = lt.newList('ARRAY_LIST')
    return entry


def newOffenseEntry(offensegrp, crime):
    """
    Crea una entrada en el indice por tipo de crimen, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    ofentry = {'event': None, 'eventlist': None}
    ofentry['event'] = offensegrp
    ofentry['eventlist'] = lt.newList('ARRAY_LIST', compareEvent)
    return ofentry



# Funciones para creacion de datos

# Requerimientos

def req1(analyzer,carac,mink,maxk):
    llaves = om.values(analyzer[carac],mink,maxk)
    print(llaves)
    print("aaaa")


# Funciones de consulta

def crimesSize(analyzer):
    """
    Número de crimenes
    """
    return lt.size(analyzer)


def indexHeight(analyzer):
    """
    Altura del arbol
    """
    return om.height(analyzer)


def indexSize(analyzer):
    """
    Numero de elementos en el indice
    """
    return om.size(analyzer)


def minKey(analyzer):
    """
    Llave mas pequena
    """
    return om.minKey(analyzer)

def maxKey(analyzer):

    return om.maxKey(analyzer)




# Funciones utilizadas para comparar elementos dentro de una lista


def compareIds(id1, id2):
    """
    Compara dos Ids
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareHashtags(hashtag1, hashtag2):
    """
    Compara dos etiquetas
    """
    if (hashtag1 == hashtag2):
        return 0
    elif (hashtag1 > hashtag2):
        return 1
    else:
        return -1

def compareEvent(event1, event2):
    """
    Compara dos eventos

    """

    if (event1 == event2):
        return 0
    elif (event1 > event2):
        return 1
    else:
        return -1

# Funciones de ordenamiento