class CuentaBancaria:
    def __init__(self, n_cuenta, titular, saldo=0.0):
        self.n_cuenta = n_cuenta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito de ${monto} realizado. Nuevo saldo: ${self.saldo}")
        else:
            print("El monto a depositar debe ser mayor que cero.")

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de ${monto} realizado. Nuevo saldo: ${self.saldo}")
        else:
            print("Monto erroneo o saldo insuficiente, verifique la informacion.")

    def calcular_interes(self, tasa_interes):
        interes = self.saldo * (tasa_interes / 100)
        self.depositar(interes)
        print(f"El interés ha sido calculado y depositado. Su saldo es: ${self.saldo}")

    def imprimir_informacion(self):
        print(f"Número de cuenta: {self.n_cuenta}")
        print(f"Titular: {self.titular}")
        print(f"Saldo actual: ${self.saldo}")



cuenta = CuentaBancaria(n_cuenta="8092350815", titular="Elian Hernandez", saldo=1000.0)

cuenta.imprimir_informacion()

cuenta.depositar(1000.0)

cuenta.retirar(350.0)

cuenta.calcular_interes(2.5)

cuenta.imprimir_informacion()