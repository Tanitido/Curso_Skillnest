animal = "chanchito feliz"
animal1 = " chanCHito triste"
print(animal.upper())  # mayuscula todo
print(animal.lower())  # minuscula todo
print(animal.capitalize())  # primera letra en mayuscula
print(animal.title())  # primera letra de cada palabra en mayuscula
print(animal1.strip())  # elimina espacios al principio y al final
print(animal1.strip().capitalize())  # aca se concatenan ambos metodos
print(animal1.lstrip())  # elimina espacios al principio
print(animal1.rstrip())  # elimina espacios al final
# busca la palabra y devuelve la posicion, si aparece -1 es no encontrado.
print(animal1.find("cH"))
print(animal.replace("a", "4").replace("e", "3").replace(
    # reemplaza las vocales por numeros
    "i", "1").replace("o", "0").replace("u", "ü"))
print("NH" in animal1)  # busca si la palabra esta en la cadena
print("NH" not in animal1)  # busca si la palabra no esta en la cadena
