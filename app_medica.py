import os
import time
import numpy as np
import funciones_medicas as fm
# ------------ VARIABLES -----------------}
opcion = ""  # Selección del usuario
tamaño = 2  # Cantidad máxima de registros
rut = ""      # Rut del paciente
arr_ruts = np.empty(tamaño, dtype=object)
nombre = ""   # Nombre del paciente
arr_nombres = np.empty(tamaño, dtype=object)
edad = 0      # Edad del paciente
arr_edades = np.empty(tamaño, dtype=int)
# -------- CÓDIGO PRINCIPAL ---------------
while True:
    os.system("cls")
    opcion = str(input('''
    --------- MENÚ ---------
    1.- Cargar datos
    2.- Buscar a un paciente por su rut 
    3.- Listar pacientes menores de edad
    4.- Salir                     
    \n Elija opción: '''))

    if opcion == "1":
        os.system("cls")

        os.system("pause")
    if opcion == "2":
        os.system("cls")

        os.system("pause")
    if opcion == "3":
        os.system("cls")

        os.system("pause")
    if opcion == "4":
        break
