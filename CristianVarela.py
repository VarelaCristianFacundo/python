# Objetivo
# Practicar el concepto de funciones. Preparar la parte lógica para el registro de usuarios.

# Consigna

# Crear un programa que permita emular el registro y almacenamiento de usuarios en una base de datos. Crear el programa utilizando el concepto de funciones, diccionarios, bucles y condicionales.
# Formato

# El proyecto debe compartirse utilizando Colab bajo el nombre “Primera pre-entrega+Apellido”.
# Se debe entregar
# Se debe entregar todo el programa.

# Sugerencias
# El formato de registro es: Nombre de usuario y Contraseña.
# Utilizar una función para almacenar la información y otra función para mostrar la información.
# Utilizar un diccionario para almacenar dicha información, con el par usuario-contraseña (clave-valor).
# Utilizar otra función para el login de usuarios, comprobando que la contraseña coincida con el usuario.
# Adicional
# Utilizando los conceptos de la clase 8, guarde la información en un archivo de texto dentro de su Drive."

import os
import json


# Constante para el nombre del archivo
FILE_NAME = "data.json"

# Función para crear un archivo txt donde se almacena la informacion
# def crearArchivo():
#     file = open("data.txt", "w")
#     file.write("[]")
#     file.close()
    
    
# Función para crear un archivo JSON si no existe
def crearArchivo():
    if not os.path.isfile(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            json.dump([], file)
            
                        
                
    # Función para Leer un archivo .txt
# def leerArchivo():
#     file = open("data.txt", "r")
#     data = file.read()
#     file.close()
#     #print(data)
#     return data
  
  # Función para leer el archivo JSON y devolver los datos
def leerArchivo():
    with open(FILE_NAME, "r") as file:
        data = json.load(file)
    return data
  
  
  # Función para identificar si existe el .txt
def existeArchivo():
    if os.path.isfile("data.txt"):
        return True
    else:
        return False
      
      
      
def guardarInformacion(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)
    print("Informacion guardada con exito")
      

# Funcion para almacenar la informacion
# def almacenarInformacion():
#     try:
#         # Valida si existe el archivo
#         if existeArchivo() == False:
#             crearArchivo()
#         # Lee el archivo
#         data = eval(leerArchivo())
#         id = int(len(data)) + 1 
#         nombre = input("Ingrese su nombre: ")
#         user = input("Ingrese su usuario: ")
#         password = input("Ingrese su contraseña: ")
#         data.append({"id": id, "nombre": nombre, "user": user, "password": password})
#         guardarInformacion(data)
#     except Exception as e:
#         print("Error al almacenar la informacion " +  e.__str__() )
        
def almacenarInformacion():
    try:
        crearArchivo()
        data = leerArchivo()
        id = len(data) + 1
        nombre = input("Ingrese su nombre: ")
        user = input("Ingrese su usuario: ")
        password = input("Ingrese su contraseña: ")
        data.append({"id": id, "nombre": nombre, "user": user, "password": password})
        guardarInformacion(data)
    except Exception as e:
        print("Error al almacenar la informacion:", e)

# Escribe en la funcion 
# def guardarInformacion(data):
#     file = open("data.txt", "w")
#     file.write(str(data))
#     file.close()
#     print("Informacion guardada con exito")


#Login de usuario
# def login():
#     try:
#         # Valida si existe el archivo
#         if existeArchivo() == False:
#             crearArchivo()
#         # Lee el archivo
#         data = eval(leerArchivo())
#         user = input("Ingrese su usuario: ")
#         password = input("Ingrese su contraseña: ")
#         for i in data:
#             if i["user"] == user and i["password"] == password:
#                 print("Bienvenido " + i["nombre"])
#                 break
#             else:
#                 print("Usuario o contraseña incorrectos")
#         else:
#             print("No existe datos favor de crear el archivo")
#     except Exception as e:
#         print("Error al almacenar la informacion " +  e.__str__() )

# Función para el inicio de sesión
def login():
    try:
        data = leerArchivo()
        user = input("Ingrese su usuario: ")
        password = input("Ingrese su contraseña: ")
        for i in data:
            if i["user"] == user and i["password"] == password:
                print("Bienvenido", i["nombre"])
                break
        else:
            print("Usuario o contraseña incorrectos")
    except Exception as e:
        print("Error al realizar el inicio de sesión:", e)



# Funcion para validar el usuario
# select = input('Seleccione una opcion: \n 1. Almacenar informacion \n 2. Login \n 3. Salir \n')
# if(select == "1"):
#     almacenarInformacion()
# elif(select == "2"):
#     login()
# elif(select == "3"):
#     exit()


# Menú principal
while True:
    print("Seleccione una opción:\n1. Almacenar información\n2. Login\n3. Salir")
    select = input()
    if select == "1":
        almacenarInformacion()
    elif select == "2":
        login()
    elif select == "3":
        break
    else:
        print("Opción inválida. Por favor, elija una opción válida.")