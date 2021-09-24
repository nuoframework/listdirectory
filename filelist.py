import os

os.system("clear")

ejemplo_dir = input("Inserte el directorio\n\n>>> ")

for nombre_directorio, dirs, ficheros in os.walk(ejemplo_dir, topdown=False):
    print(nombre_directorio)
    for nombre_fichero in ficheros:
        print(nombre_fichero)
