# Definición de la clase Cliente para registrar sus datos personales
class Cliente:
    # Método constructor que inicializa los atributos del cliente
    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre  # Guarda el nombre del cliente
        self.cedula = cedula  # Guarda el número de cédula del cliente
        self.telefono = telefono  # Guarda el número de teléfono del cliente

    # Método especial que devuelve una representación legible del objeto en texto
    def __str__(self):
        # Retorna la ficha formateada usando f-strings
        return f"--- FICHA DE CLIENTE ---\nNombre: {self.nombre}\nCédula: {self.cedula}\nTeléfono: {self.telefono}\n"


# Bloque de ejecución principal
if __name__ == "__main__":
    # Creación del primer objeto Cliente con sus datos correspondientes
    cliente1 = Cliente("María Celeste", "4.567.890", "0981-123456")
    # Creación del segundo objeto Cliente con sus datos correspondientes
    cliente2 = Cliente("Facundo Campuzano", "5.123.456", "0971-654321")

    # Impresión de la ficha del primer cliente
    print(cliente1)
    # Impresión de la ficha del segundo cliente
    print(cliente2)