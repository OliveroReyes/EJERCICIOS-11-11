from abc import ABC, abstractmethod
class Estudiante(ABC):
    @abstractmethod
    def obtener_promedio(self):
        pass
    @abstractmethod
    def mostrar_informacion(self):
        pass

class EstudianteDeGrado(Estudiante):
    def __init__(self, nombre, notas):
        self.__nombre = nombre
        self.__notas = notas
        
    def obtener_promedio(self):
        return sum(self.__notas) / len(self.__notas)
    
    def mostrar_informacion(self):
         print(f"estudiante de grado {self.__nombre}, promedio {self.obtener_promedio()}")

class EstudianteDePosgrado(Estudiante):
    def __init__(self, nombre, tesis_calificada):
        self.__nombre = nombre
        self.__tesis_calificada = tesis_calificada

    def obtener_promedio(self):
        return "Completa la tesis" if self.__tesis_calificada else "Tesis pendiente"

    def mostrar_informacion(self):
        print(f"Estudiante de posgrado: {self.__nombre}, tesis {self.obtener_promedio()}")
        

estudiantes = [
    EstudianteDeGrado("Juan", [8.5, 9.0, 8.5]),
    EstudianteDePosgrado("Nancy", True)
]

for estudiante in estudiantes:
    estudiante.mostrar_informacion()