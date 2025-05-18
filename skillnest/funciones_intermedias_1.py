# def de variables/listas/
matriz = [[10, 15, 20], [3, 7, 14]]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

# Actualizar valores en diccionarios y listas
matriz[1][0] = 6
cantantes[0]["nombre"] = "Enrique Martin Morales"
ciudades["México"][2] = "Monterrey"
coordenadas[0]["latitud"] = 9.9355431

print(matriz)
print(cantantes)
print(ciudades)
print(coordenadas)

# 2 Funcion que recorre listas


def iterarDiccionario(lista):
    for dic in lista:
        for a, b in dic.items():
            print(str(a) + " " + str(b))


iterarDiccionario(cantantes)

# 3 Función para obtener valores de una lista de diccionarios según una clave


def iterarDiccionario2(a, b):
    for dic in b:
        if a in dic:
            print(dic[a])


iterarDiccionario2("nombre", cantantes)

# 4 Iterar a través de un diccionario con valores de lista


def imprimirInformacion(diccionario):
    for a, b in diccionario.items():
        print(str(len(b)) + " " + a.upper())
        for i in b:
            print(i)
        print()


imprimirInformacion(costa_rica)
