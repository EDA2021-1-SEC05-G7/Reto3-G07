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
from DISClib.DataStructures import listiterator as it
from pprint import pprint 
from random import randint
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
    # llaves: extrae una lista de los valores en el rango dado del arbol
    iterator = it.newIterator(llaves)
    # iterator: crea un iterador para la lista llaves
    contador = m.newMap(numelements= lt.size(llaves),maptype="CHAINING",loadfactor=2)
    # contador: mapa - tabla de hash, donde se van a almacenar los datos de las canciones, con los artistas como llaves
    contador2 = 0
    # contador2: var que llevará la cuenta de cuantas canciones se van añadiendo
    while it.hasNext(iterator):
        element = it.next(iterator)
        # element: var que toma como valor cada elemento dentro de la lista llaves (ver ss1)
        kset = m.keySet(element["eventIndex"])
        # kset: lista con los valores dentro de la tabla de hash "eventIndex" dentro de cada elemento guardado en element (ver linea 124,ss2)
        itit = it.newIterator(kset)
        # itit: nuevo iterador para la lista de los valores del map "eventIndex"
        while it.hasNext(itit):
            elel = it.next(itit)
            dic = me.getValue(m.get(element["eventIndex"],elel))
            # dic: el diccionario con dos llaves: event->el valor numerico, eventlist: la lista con los events con ese valor
            contador2 += lt.size(dic["eventlist"])
            # se agrega al contador la cantidad de elementos que tenga la lista eventlist equivalente a la cantidad de events que hay con ese valor numerico
            itr = it.newIterator(dic["eventlist"])
            #itr: nuevo iterador para la lista de los eventos en con ese valor
            while it.hasNext(itr):
                elell = it.next(itr)
                # cada valor numerico dentro del rango, siendo un diccionario cuyo valor es toda la informacion relacionada a ese numero en el rango (controller->newdict)
                m.put(contador,elell["artist_id"],0)
                # se inserta dentro de la tabla de hash, un elemento con cada iteracion en la lista de events relacionado a un rango, cuya llave es el artist id con la final de que se sobreescriban los datos para conocer el tamaño final de la tabla y asi saber la cantidad de artistas sin repetirse
    (a,b) = (contador2,m.size(contador))  
    # tupla con la cantidad de events en total y la cantidad total de artists
    return (a,b)

def req2(analyzer,mne,mxe,mnd,mxd):
    llaves = om.values(analyzer["energy"],mne,mxe)
    """lista con valores dentro del rango en arbole energy"""
    listt =  m.newMap(numelements= lt.size(llaves),maptype="CHAINING",loadfactor=2)
    iterator = it.newIterator(llaves)
    """ iterador para la lista de valores en arbol energy (llaves)"""
    while it.hasNext(iterator):
        element = it.next(iterator)
        kse = m.keySet(element["eventIndex"])
        """lista con valores de tabla de hash contenida en cada elemento"""
        itt = it.newIterator(kse)
        while it.hasNext(itt):
            newel = it.next(itt)
            dit = me.getValue(m.get(element["eventIndex"],newel))
            newit = it.newIterator(dit["eventlist"])
            while it.hasNext(newit):
                nnewl = it.next(newit)
                vd = nnewl["danceability"]
                if  vd >= mnd and vd <= mxd:
                    m.put(listt,nnewl["track_id"],nnewl)
    print("++++++ Req 2. results... ++++++")
    print("Energy is between",mne,"and",mxe)
    print("Danceability is between",mnd,"and",mxd)
    print("Total of unique tracks in events:", m.size(listt),"\n")
    print("--- Unique track_id ---")
    newkk = m.valueSet(listt)
    i = 0
    while i <= 4:
        el = lt.getElement(newkk,randint(0,lt.size(newkk)))
        print("Track",i+1,":", el["track_id"],"whit energy of",el["energy"],"and danceability of",el["danceability"])
        i += 1
    return None
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
    return lt.size(analyzer)


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