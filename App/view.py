"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import map as m
import datetime



"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar el analizador.")
    print("2- Cargar información en el catálogo.")
    print("3- Caracterizar las reproducciónes.")
    print("4- Encontrar musica para festejar.")
    print("5- Encontar música para estudiar.")
    print("6- Encontrar características de los géneros y crear un nuevo género")
    print("7- el 5")
    print("0- Salir")
    print("*******************************************")

analyzer = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    
    if int(inputs[0]) == 1:
        #Inicializar el analizador
        print("Inicializando...")
        #Se carga el analyzer que se va a usar de aqui en adelante
        analyzer = controller.iniciar()
        for llaves in analyzer:
            print(llaves)


    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ...")

        #Carga de datos
        """controller.loadEventAnalisis(analyzer)"""
        #lists = ["instrumentalness","liveness","speechiness","danceability","valence","loudness","tempo","acousticness","energy","created_at"]
        lists = ["tempo","created_at"]
        for i in lists:
            controller.loadEvents(analyzer,i)
        """controller.loadSentiment(analyzer)
        controller.loadUser(analyzer)
        #print(controller.maxKey(analyzer["created_at"]))
        print(m.size(analyzer["user"]))"""

        

    elif int(inputs[0]) == 3:
        #Requerimiento 1
        carac = (input("¿Cual es la caracteristica de contenido que desea conocer? ")).lower()
        mink = float(input("Introduzca el valor mínimo de la característica de contenido que desea saber "))
        maxk = float(input("Introduzca el valor maximo de la característica de contenido que desea saber "))
        print('Altura del arbol: ' + str(controller.indexHeight(analyzer[carac])))
        print('Elementos en el arbol: ' + str(controller.indexSize(analyzer["events"])))
        print("Min key: ", str(controller.minKey(analyzer[carac])))
        print("Max key: ", str(controller.maxKey(analyzer[carac])))
        (a,b) = controller.req1(analyzer,carac,mink,maxk)
        print("total repro",a,"artistas",b)
        
        

    elif int(inputs[0]) == 4:
        #Requerimiento 2
        mne = float(input("Introduzca el valor minimo de 'energy':\n"))
        mxe = float(input("Introduzca el valor máximo de 'energy':\n"))
        mnd = float(input("Introduzca el valor minimo de 'danceability':\n"))
        mxd = float(input("Introduzca el valor minimo de 'danceability':\n"))
        controller.req2(analyzer,mne,mxe,mnd,mxd)

        pass

    elif int(inputs[0]) == 5:
        #Requerimiento 3
        minimus = float(input("Introduzca el valor mínimo del rango para 'instrumentalness': \n"))
        magnus = float(input("Introduzca el valor máximo del rango para 'instrumentalness': \n"))
        minima = float(input("Introduzca el valor mínimo del rango para 'tempo': \n"))
        magna = float(input("Introduzca el valor máximo del rango para 'tempo': \n"))
        controller.req3(analyzer, minimus, magnus, minima, magna)

        
    elif int(inputs[0]) == 6:
        generos = (input("Introduzca los géneros de los cuales desea saber las canciones y los artistas separados por comas (,): \n")).split(",")
        novus = int(input("¿Desea crear un nuevo género? \nIngrese 1 si sí lo desea crear, o 0 si no: \n"))
        newgen = {}
        if novus == 1:
            nomen = input("Introduzca el nombre del nuevo género: \n")
            minimum = float(input("Introduzca el valor mínimo del tempo para este nuevo género: \n"))
            magnum = float(input("Introduzca el valor máximo del tempo para este nuevo género: \n"))
            newgen["name"] = nomen
            newgen["rango"] = [minimum,magnum]
            generos.append(newgen)
            controller.req4(analyzer,generos)
        elif novus == 0:
            nominis = None
            generos.append(nominis)
            controller.req4(analyzer,generos)
            

    elif int(inputs[0]) == 7:
        #Requerimiento 5

        minn = input("Introduzca el valor mínimo del rango para 'hora': \n")
        mintime = datetime.datetime.strptime(minn, '%H:%M:%S').time()
        maxx = input("Introduzca el valor máximo del rango para 'hora': \n")
        maxtime = datetime.datetime.strptime(maxx, '%H:%M:%S').time()
        controller.req5(analyzer,mintime,maxtime)

    else:
        sys.exit(0)
sys.exit(0)
