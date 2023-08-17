edad = int(input("Ingrese su edad: "))
Antiguedad = int(input("ingrese su antiguedad: "))
salario = int(input("Ingrese su salario: "))


if edad >= 18:
    if Antiguedad >= 3 and salario > 2500:
        print("Credito Aprobado")
    else:
        print ("No aprobado")


frase_original = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"

renglones = frase_original.split("&")

frase_resultado = ""

for pos, renglon in enumerate(renglones):

  renglon = renglon.capitalize()

  if pos == 0:

    frase_resultado += f'{renglon}...\n'

  else:

    frase_resultado += f'- {renglon}.\n'

print(frase_resultado)

"""

Gordon lanzó su curva...

- Strawberry ha fallado por un pie! -gritó Joe Castiglione.

- Dos pies le corrigió Troop.

- Strawberry menea la cabeza como disgustado… -agrega el comentarista.

"""



import json  #Importar las funciones de json en la 

#Clase 15 entenderemos mejor el IMPORT

data = {}

data['clients'] = []

data['locations'] = []

data['clients'].append({

    'first_name': 'Sigrid',

    'last_name': 'Mannock',

    'age': 27,

    'amount': 7.17})

data['clients'].append({

    'first_name': 'Joe',

    'last_name': 'Hinners',

    'age': 31,

    'amount': [1.90, 5.50]})

data['clients'].append({

    'first_name': 'Theodoric',

    'last_name': 'Rivers',

    'age': 36,

    'amount': 1.11})

with open('Lesson08' + "/primerJson.json", 'w') as file:

  json.dump(data, file, indent=4)

#  ----------------------------------------------------------------

# with open('Lesson08' + "/primerJson.json") as file:

#     dataLectura = json.load(file)

#     for client in dataLectura['clients']:

#         print('First name:', client['first_name'])

#         print('Last name:', client['last_name'])

#         print('Age:', client['age'])

#         print('Amount:', client['amount'])

#         print('')