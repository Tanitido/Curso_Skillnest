class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

    def hacer_compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print(
                f"Compra denegada para {self.nombre} {self.apellido}: excede el límite de crédito.")

    def pagar_tarjeta(self, monto):
        if monto > self.saldo_pagar:
            print(
                f"{self.nombre} {self.apellido} está pagando más del saldo actual. Se ajustará al saldo total.")
            self.saldo_pagar = 0
        else:
            self.saldo_pagar -= monto

    def mostrar_saldo_usuario(self):
        print(
            f"Usuario: {self.nombre} {self.apellido}, Saldo a Pagar: ${self.saldo_pagar}")

    def transferir_deuda(self, otro_usuario, monto):
        if monto > self.saldo_pagar:
            print(
                f"No se puede transferir más deuda de la que tiene {self.nombre} {self.apellido}.")
        else:
            self.saldo_pagar -= monto
            otro_usuario.saldo_pagar += monto


# Crear 3 instancias de Usuario
usuario1 = Usuario("Nariyoshi", "Miyagi", "miyagi@example.com")
usuario2 = Usuario("Daniel", "LaRusso", "daniel@example.com")
usuario3 = Usuario("Johnny", "Lawrence", "johnny@example.com")

# Usuario 1: 2 compras y 1 pago
usuario1.hacer_compra(100)
usuario1.hacer_compra(150)
usuario1.pagar_tarjeta(200)
usuario1.mostrar_saldo_usuario()

# Usuario 2: 1 compra y 2 pagos
usuario2.hacer_compra(300)
usuario2.pagar_tarjeta(100)
usuario2.pagar_tarjeta(250)
usuario2.mostrar_saldo_usuario()

# Usuario 3: 3 compras y 4 pagos
usuario3.hacer_compra(50)
usuario3.hacer_compra(75)
usuario3.hacer_compra(25)
usuario3.pagar_tarjeta(30)
usuario3.pagar_tarjeta(50)
usuario3.pagar_tarjeta(20)
usuario3.pagar_tarjeta(10)
usuario3.mostrar_saldo_usuario()
