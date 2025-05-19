class TarjetaCredito:
    tarjetas_creadas = []

    def __init__(self, limite_credito, intereses, saldo_pagar=0):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses
        TarjetaCredito.tarjetas_creadas.append(self)

    def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        return self

    def pago(self, monto):
        self.saldo_pagar -= monto
        return self

    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar:.2f}")
        return self

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self

    @classmethod
    def mostrar_todas_las_tarjetas(cls):
        print("\n--- TODAS LAS TARJETAS ---")
        for idx, tarjeta in enumerate(cls.tarjetas_creadas, start=1):
            print(
                f"Tarjeta {idx}: Saldo ${tarjeta.saldo_pagar:.2f}, Límite ${tarjeta.limite_credito}, Interés {tarjeta.intereses*100}%")


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tarjetas = []

    def agregar_tarjeta(self, tarjeta):
        self.tarjetas.append(tarjeta)
        return self

    def hacer_compra(self, monto, tarjeta_index=0):
        if tarjeta_index < len(self.tarjetas):
            self.tarjetas[tarjeta_index].compra(monto)
        else:
            print("Tarjeta no válida")
        return self

    def pagar_tarjeta(self, monto, tarjeta_index=0):
        if tarjeta_index < len(self.tarjetas):
            self.tarjetas[tarjeta_index].pago(monto)
        else:
            print("Tarjeta no válida")
        return self

    def mostrar_saldo_usuario(self):
        print(f"Usuario: {self.nombre}")
        for i, tarjeta in enumerate(self.tarjetas):
            print(
                f"  Tarjeta {i+1}: Saldo a Pagar: ${tarjeta.saldo_pagar:.2f}")
        return self


# Crear 3 tarjetas
tarjeta1 = TarjetaCredito(limite_credito=1000, intereses=0.05)
tarjeta2 = TarjetaCredito(limite_credito=2000, intereses=0.02)
tarjeta3 = TarjetaCredito(limite_credito=500, intereses=0.03)

# Crear usuarios
usuario1 = Usuario("Juan").agregar_tarjeta(tarjeta1)
usuario2 = Usuario("Ana").agregar_tarjeta(tarjeta2)
usuario3 = Usuario("Luis").agregar_tarjeta(tarjeta3)

# Operaciones encadenadas para tarjetas directamente
print("\n--- TARJETA 1 ---")
tarjeta1.compra(200).compra(100).pago(
    50).cobrar_interes().mostrar_info_tarjeta()

print("\n--- TARJETA 2 ---")
tarjeta2.compra(300).compra(400).compra(200).pago(
    100).pago(50).cobrar_interes().mostrar_info_tarjeta()

print("\n--- TARJETA 3 ---")
tarjeta3.compra(100).compra(150).compra(100).compra(
    100).compra(100).mostrar_info_tarjeta()

# Mostrar información del usuario
print("\n--- USUARIOS ---")
usuario1.mostrar_saldo_usuario()
usuario2.mostrar_saldo_usuario()
usuario3.mostrar_saldo_usuario()

# BONUS: Usuario con varias tarjetas
tarjeta_extra = TarjetaCredito(limite_credito=3000, intereses=0.01)
usuario1.agregar_tarjeta(tarjeta_extra)
usuario1.hacer_compra(500, tarjeta_index=1).pagar_tarjeta(200, tarjeta_index=1)
usuario1.mostrar_saldo_usuario()

# BONUS FINAL
TarjetaCredito.mostrar_todas_las_tarjetas()
