class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

class Cuenta:
    def __init__(self, numero_cuenta, saldo, limitecre, tipocuenta):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.limite_credito = limitecre
        self.tipocuenta = tipocuenta

    def retirar_efectivo(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            return f"Retiro exitoso. Saldo restante: {self.saldo}"
        else:
            return "Saldo insuficiente."

    def ingresar_efectivo(self, cantidad):
        self.saldo += cantidad
        return f"Ingreso exitoso. Nuevo saldo: {self.saldo}"

    def pagar_factura(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            return f"Pago de factura exitoso. Saldo restante: {self.saldo}"
        else:
            return "Saldo insuficiente para pagar la factura."

    def transferir_fondos(self, cuenta_destino, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            cuenta_destino.saldo += cantidad
            return f"Transferencia exitosa. Nuevo saldo: {self.saldo}"
        else:
            return "Saldo insuficiente para realizar la transferencia."


class Cliente:
    def __init__(self, nombre, direccion, numero_cuenta, banco):
        self.nombre = nombre
        self.direccion = direccion
        self.numero_cuenta = numero_cuenta
        self.banco = banco
        self.banco.agregar_cuenta(self)

    def __str__(self):
        return f"Cliente: {self.nombre}, Número de cuenta: {self.numero_cuenta}, Banco: {self.banco.nombre}"

class Cajero:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def mostrar_menu(self, cliente):
        while True:
            print("\nMenu de opciones:")
            print("1. Retirar de efectivo")
            print("2. Ingreso de efectivo")
            print("3. Pago de factura")
            print("4. Transferencias")
            print("5. Salir")
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                print(cliente.cuenta.retirar_efectivo(cantidad))
            elif opcion == "2":
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                print(cliente.cuenta.ingresar_efectivo(cantidad))
            elif opcion == "3":
                cantidad = float(input("Ingrese la cantidad de la factura a pagar: "))
                print(cliente.cuenta.pagar_factura(cantidad))
            elif opcion == "4":
                cuenta_destino = input("Ingrese el número de cuenta destino: ")
                cantidad = float(input("Ingrese la cantidad a transferir: "))
                cuenta_destino_obj = next((cuenta for cuenta in cliente.banco.cuentas if cuenta.numero_cuenta == cuenta_destino), None)
                if cuenta_destino_obj:
                    print(cliente.cuenta.transferir_fondos(cuenta_destino_obj, cantidad))
                else:
                    print("Cuenta no valida.")
            elif opcion == "5":
                break
            else:
                print("Opción no válida. Intente Nuevamente.")

if __name__ == "__main__":
    banco1= Banco("Banco One")
    
    cliente1 = Cliente("Elian", "Estero Hondo", "001", banco1)
    cliente2 = Cliente("Alberto", "Santo Domingo", "002", banco1)

    cliente1.cuenta = Cuenta("001", 1000, 500, "Corriente")
    cliente2.cuenta = Cuenta("002", 2000, 1000, "Ahorro")
    cajero = Cajero("Cajer0", "2514")

    print(cliente1)
    print(cliente2)
    print("\nOperaciones:")
    cajero.mostrar_menu(cliente1)
    print("\nEstado de las cuentas después de las operaciones:")
    