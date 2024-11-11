class Empleado:
    def calcular_salario(self):
        return 0

class EmpleadoPorHora(Empleado):
    def __init__(self, tarifa_hora, horas_trabajadas):
        self.tarifa_hora = tarifa_hora
        self.horas_trabajadas = horas_trabajadas
    def calcular_salario(self):
        return self.tarifa_hora * self.horas_trabajadas
    
class EmpleadoFijo(Empleado):
    def __init__(self, salario_mensual):
        self.salario_mensual = salario_mensual
        
    def calcular_salario(self):
        return self.salario_mensual
    

empleados = [
    EmpleadoPorHora(10, 150),
    EmpleadoFijo(3000)
]
for empleado in empleados:
    print("Salario", empleado.calcular_salario())