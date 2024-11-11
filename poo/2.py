class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo=0):
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"deposito {cantidad} hecho. Saldo actual {self.__saldo}")
        else:
            print("cantidad invalida para depositar")
            
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"retiro de {cantidad} hecho. Saldo actual {self.__saldo}")
        else:
            print("cantidad invalida para retirar")

    def get_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria("12345678", 1000)
cuenta.depositar(500)
cuenta.retirar(200)
print("saldo final", cuenta.get_saldo())