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
    analyzer = {'events': None,
                'eventkind': None
                }

    analyzer['events'] = lt.newList('SINGLE_LINKED', compareIds)
    analyzer['eventkind'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareEvent)
    return analyzer


# Funciones para agregar informacion al catalogo


def addCrime(analyzer, crime):
    """
    """
    lt.addLast(analyzer['events'], crime)
    updateDateIndex(analyzer['eventkind'], crime)
    return analyzer


def updateDateIndex(map, crime):
    """
    Se toma la fecha del crimen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    occurreddate = crime['instrumentalness']
    entry = om.get(map, occurreddate)
    if entry is None:
        datentry = newDataEntry(crime)
        om.put(map, occurreddate, datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, crime)
    return map


def addDateIndex(datentry, crime):
    """
    Actualiza un indice de tipo de crimenes.  Este indice tiene una lista
    de crimenes y una tabla de hash cuya llave es el tipo de crimen y
    el valor es una lista con los crimenes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry['lstevents']
    lt.addLast(lst, crime)
    offenseIndex = datentry['eventIndex']
    offentry = m.get(offenseIndex, crime['instrumentalness'])
    if (offentry is None):
        entry = newOffenseEntry(crime['instrumentalness'], crime)
        lt.addLast(entry['eventlist'], crime)
        m.put(offenseIndex, crime['instrumentalness'], entry)
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
    entry['lstevents'] = lt.newList('SINGLE_LINKED')
    return entry


def newOffenseEntry(offensegrp, crime):
    """
    Crea una entrada en el indice por tipo de crimen, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    ofentry = {'event': None, 'eventlist': None}
    ofentry['event'] = offensegrp
    ofentry['eventlist'] = lt.newList('SINGLELINKED', compareEvent)
    return ofentry

#............#
"""def newAnalyzer():
   """ """ Inicializa el analizador

    Crea una lista vacia para guardar todos los eventos y 
    los analisis de los eventos. Además se crea un mapa que
    guarda los hashtags

    Retorna el analizador inicializado.
    """"""
    analyzer = {'Eventos': None,
                'AnalisisEventos': None,
                'HashTags': None
                }

    analyzer['Eventos'] = lt.newList('ARRAY_LIST', compareIds)

    analyzer['AnalisisEventos'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareEvent)

    analyzer['Hashtags'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareHashtags)

    return analyzer

# Funciones para agregar informacion al catalogo

def addEvent(analyzer, event):
    """
"""    Añade los eventos a la lista de eventos del analyzer
"""    """
    lt.addLast(analyzer['Eventos'], event)
    return analyzer

def addEventAnalisis(analyzer, event):
    """
"""    Añade los análisis de los eventos a la lista de AnalisisEventos del analyzer
"""    """
    inst = analyzer["AnalisisEventos"]
    eve = event["instrumentalness"]
    entry = om.get(inst,eve)
    if entry is None:
        neweve = newEventEntry(eve)
        om.put(inst,eve, neweve)

    return analyzer
def newEventEntry(event):

def addhashtag(analyzer, hashtag):
    """
"""    Añade al map de Hashtags un diccionario con el nombre del hashtag y su informacion
"""    """
    hass = analyzer["Hashtags"]
    hashy = hashtag['hashtag']
    existhashhash = om.get(hass, hashy)
    if existhashhash is None:
        eltag = newHashtagEntry(hashy)
        om.put(hass, hashy, eltag)
    else: 
        toxic = mp.get(hass, hashy)
        eltag = me.getValue(toxic)
        lt.addLast(eltag["HashtagInfo"], hashtag)  #añade un nuevo a la lista que esta dentro de la llave "videos" en el dict "pais"

def newHashtagEntry(hashtag):
    """
"""    Crea un diccionario para agregar cada hashtag con su información en el map Hashtags del analyzer.
"""    """
    hashentry = {'Hashtag': None, 'HashtagInfo': None}
    hashentry['offense'] = hashtag
    hashentry['lstoffenses'] = lt.newList('ARRAY_LIST', compareHashtags)
    return hashentry
"""
#............#


# Funciones para creacion de datos

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