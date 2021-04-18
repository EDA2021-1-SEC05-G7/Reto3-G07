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


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar el analizador")
    print("2- Cargar información en el catálogo")
    print("3- Caracterizar las reproducciónes")
    print("4- ")
    print("5- ")
    print("6- ")
    print("7- ")
    print("0- Salir")
    print("*******************************************")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    
    if int(inputs[0]) == 1:
        #Inicializar el analizador
        print("Inicializando...")
        #Se carga el catalogo que se va a usar de aqui en adelante
        catalog = controller.iniciar()
        
    
    elif int(inputs[0]) == 2:
        #Carga de datos
        print("Cargando información de los archivos ...")

    elif int(inputs[0]) == 3:
        #Requerimiento 1
        pass

    elif int(inputs[0]) == 4:
        #Requerimiento 2
        pass

    elif int(inputs[0]) == 5:
        #Requerimiento 3
        pass

    elif int(inputs[0]) == 6:
        #Requerimiento 4
        pass

    elif int(inputs[0]) == 7:
        #Requerimiento 5
        pass

    else:
        sys.exit(0)
sys.exit(0)
