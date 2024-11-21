from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    @abstractmethod
    def calcular_precio(self):
        pass

    @abstractmethod
    def mostrar_detalles(self):
        pass

class ProductoElectronico(Producto):
    def calcular_precio(self):
        return self._precio * 1.21  # Suponiendo un IVA del 21%

    def mostrar_detalles(self):
        print(f"Producto Electrónico: {self._nombre}, Precio con IVA: {self.calcular_precio()}")

class ProductoRopa(Producto):
    def calcular_precio(self):
        return self._precio * 1.15  # Suponiendo un IVA del 15%

    def mostrar_detalles(self):
        print(f"Producto de Ropa: {self._nombre}, Precio con IVA: {self.calcular_precio()}")

# Función para el menú
def menu_tienda():
    productos = []
    while True:
        print("\n1. Agregar producto electrónico")
        print("2. Agregar producto de ropa")
        print("3. Calcular precio total")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            nombre = input("Nombre del producto electrónico: ")
            precio = float(input("Precio: "))
            productos.append(ProductoElectronico(nombre, precio))
        elif opcion == "2":
            nombre = input("Nombre del producto de ropa: ")
            precio = float(input("Precio: "))
            productos.append(ProductoRopa(nombre, precio))
        elif opcion == "3":
            total = sum([producto.calcular_precio() for producto in productos])
            print(f"Precio total de todos los productos: {total}")
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el menú
menu_tienda()