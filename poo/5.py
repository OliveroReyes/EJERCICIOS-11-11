from abc import ABC, abstractmethod

# Clase abstracta Producto
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

    # Métodos getters
    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    # Métodos setters
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @precio.setter
    def precio(self, precio):
        self._precio = precio

# Clase concreta ProductoElectrónico
class ProductoElectrónico(Producto):
    def __init__(self, nombre, precio, garantia):
        super().__init__(nombre, precio)
        self._garantia = garantia

    def calcular_precio(self):
        # Supongamos un impuesto del 10% para productos electrónicos
        return self._precio * 1.10

    def mostrar_detalles(self):
        return f"Electrónico: {self._nombre}, Precio: ${self._precio:.2f}, Garantía: {self._garantia} años"

# Clase concreta ProductoRopa
class ProductoRopa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    def calcular_precio(self):
        # Supongamos un impuesto del 5% para productos de ropa
        return self._precio * 1.05

    def mostrar_detalles(self):
        return f"Ropa: {self._nombre}, Precio: ${self._precio:.2f}, Talla: {self._talla}"

# Menú interactivo
def menu():
    productos = []
    while True:
        print("\n--- Sistema de Gestión de Tienda ---")
        print("1. Agregar Producto Electrónico")
        print("2. Agregar Producto de Ropa")
        print("3. Ver Productos")
        print("4. Calcular Precio Total")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto electrónico: ")
            precio = float(input("Ingrese el precio: "))
            garantia = int(input("Ingrese la garantía (en años): "))
            producto = ProductoElectrónico(nombre, precio, garantia)
            productos.append(producto)
            print("Producto electrónico agregado correctamente.")
        
        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto de ropa: ")
            precio = float(input("Ingrese el precio: "))
            talla = input("Ingrese la talla: ")
            producto = ProductoRopa(nombre, precio, talla)
            productos.append(producto)
            print("Producto de ropa agregado correctamente.")
        
        elif opcion == "3":
            if not productos:
                print("No hay productos en la tienda.")
            else:
                for idx, producto in enumerate(productos, start=1):
                    print(f"{idx}. {producto.mostrar_detalles()}")
        
        elif opcion == "4":
            if not productos:
                print("No hay productos para calcular el precio total.")
            else:
                total = sum(producto.calcular_precio() for producto in productos)
                print(f"El precio total de todos los productos es: ${total:.2f}")
        
        elif opcion == "5":
            print("¡Gracias por usar el sistema!")
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
