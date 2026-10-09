# Definición de la clase Empleado
class Empleado:
    # Constructor que recibe nombre, cargo y el salario mensual
    def __init__(self, nombre, cargo, salario_mensual):
        self.nombre = nombre  # Guarda el nombre del empleado
        self.cargo = cargo  # Guarda el cargo del empleado
        self.salario_mensual = salario_mensual  # Guarda el salario mensual en Gs.

    # Método para calcular el salario anual incluyendo el aguinaldo (13 meses)
    def calcular_salario_anual(self, incluir_aguinaldo=True):
        meses = 13 if incluir_aguinaldo else 12  # Si incluye aguinaldo suma 13 meses
        return self.salario_mensual * meses  # Retorna el total cobrado al año

    # Método que muestra la información legible del empleado
    def __str__(self):
        # Muestra el nombre, cargo, salario mensual y el salario anual con aguinaldo
        return f"Empleado: {self.nombre} | Cargo: {self.cargo} | Salario Mensual: {self.salario_mensual:,.0f} Gs. | Salario Anual (con aguinaldo): {self.calcular_salario_anual():,.0f} Gs."


# Bloque de ejecución principal
if __name__ == "__main__":
    # Creación de un objeto de tipo Empleado
    emp1 = Empleado("Óscar Campuzano", "Técnico Electromecánico", 3500000)

    # Impresión de la información del empleado
    print(emp1)