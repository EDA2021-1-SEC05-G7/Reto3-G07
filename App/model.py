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
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newAnalyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los eventos y 
    los analisis de los eventos. Además se crea un mapa que
    guarda los hashtags

    Retorna el analizador inicializado.
    """
    analyzer = {'Eventos': None,
                'AnalisisEventos': None
                'HashTags'
                }

    analyzer['Eventos'] = lt.newList('ARRAY_LIST', compareIds)

    analyzer['AnalisisEventos'] = lt.newList('ARRAY_LIST', compareIds)

    analyzer['Hashtags'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareHashtags)

    return analyzer

# Funciones para agregar informacion al catalogo

def addEvent(analyzer, event):
    """
    Añade los eventos a la lista de eventos del analyzer
    """
    lt.addLast(analyzer['Eventos'], event)
    return analyzer

def addEventAnalisis(analyzer, event):
    """
    Añade los análisis de los eventos a la lista de AnalisisEventos del analyzer
    """
    lt.addLast(analyzer['AnalisisEventos'], event)
    return analyzer

def addhashtag(analyzer, hashtag)
    """
    Añade al map de Hashtags un diccionario con el nombre del hashtag y su informacion
    """
    hass = analyzer["Hashtags"]
    hashy = hashtag['hashtag']
    existhashhash = mp.contains(hass, hashy) #revisa si el map "hass" contiene la llave "hashy" (el hashtag) y retorna true o false
    if existhashhash:                        #el "if" inicia si "existhashash" es true
        toxic = mp.get(hass, hashy)          #"toxic" guarda la pareja (llave,valor) de la llave "hashy" (el pais)
        eltag = me.getValue(toxic)           #retorna el Valor de la pareja llave,valor que retorna "toxic"
    else:                              #si el map "hass" no tiene la llave "hashy" entonces se ejecuta este "else"
        eltag = newHashtagEntry(hashy)         #"pais" guarda el diccionario que retorna la funcion "newVidPais()" con "pai" como valor del key "pais"
        mp.put(hass, hashy, eltag)       #pone en el map "hass", en la llave "hashy" el dict "pais"
    lt.addLast(eltag["Hashtag"], hashtag)  #añade un nuevo a la lista que esta dentro de la llave "videos" en el dict "pais"





def newHashtagEntry(hashtag, event):
    """
    Crea un diccionario para agregar cada hashtag con su información en el map Hashtags del analyzer.
    """
    hashentry = {'Hashtag': None, 'HashtagInfo': None}
    hashentry['offense'] = hashtag
    hashentry['lstoffenses'] = lt.newList('ARRAY_LIST', compareOffenses)
    return hashentry



# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
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