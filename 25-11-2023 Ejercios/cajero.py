class CajeroAutomatico:
    def __init__(self):
        self.saldo = 20000


    def depositar(self, monto): 
        self.saldo += monto
        print(f"Depósito exitoso. Saldo actual: {self.saldo}")

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro exitoso. Saldo actual: {self.saldo}")
        else:
            print("Fondos insuficientes.")

    def consultar_saldo(self):
        print(f"Saldo Disponible: {self.saldo}")



def main():
    cajero = CajeroAutomatico()

    while True:
        print("\n1. Depositar")
        print("2. Retirar")
        print("3. Consultar Saldo")
        print("4. Salir")

        opcion = input("Seleccione una opción : ")

        if opcion == "1":
            cajero.depositar(float(input("Ingrese el monto a depositar: ")))
        elif opcion == "2":
            cajero.retirar(float(input("Ingrese el monto que desea retirar: ")))
        elif opcion == "3":
            cajero.consultar_saldo()
        elif opcion == "4":
            print("Gracias por utilizar nuestros servicios. ")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
