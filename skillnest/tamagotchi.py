class Tamagotchi:
    def __init__(self, nombre, color, salud=100, felicidad=50, energia=100):
        self.nombre = nombre
        self.color = color
        self.salud = salud
        self.felicidad = felicidad
        self.energia = energia

    def jugar(self):
        self.felicidad += 10
        self.salud -= 5
        print(
            f"{self.nombre} ha jugado. Felicidad: {self.felicidad}, Salud: {self.salud}")

    def comer(self):
        self.felicidad += 5
        self.salud += 10
        print(
            f"{self.nombre} ha comido. Felicidad: {self.felicidad}, Salud: {self.salud}")

    def curar(self):
        self.salud += 20
        self.felicidad -= 5
        print(
            f"{self.nombre} ha sido curado. Salud: {self.salud}, Felicidad: {self.felicidad}")
