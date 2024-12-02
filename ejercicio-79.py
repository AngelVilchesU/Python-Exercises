"""
Ejercicio: Representa una cuenta bancaria con deposito y retiro. debe haber titular y saldo

Lógica   : POO
"""

# Variables
class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def deposito(self, monto):
        self.saldo = self.saldo + monto
        print(f"Se ha depositado ha su cuenta un total de ${monto}")
        print(f"Monto actual: ${self.saldo}")

    def retiro(self, monto):
        self.saldo = self.saldo - monto
        print(f"Se ha retirado ha su cuenta un total de ${monto}")
        print(f"Monto actual: ${self.saldo}")

# Proceso
cuenta1 = Cuenta("ANGEL", 4000)

# Resultado
cuenta1.deposito(1000)
cuenta1.retiro(4000)


# ¿Cómo mejorar la lógica?

