# Definición de la clase Vehiculo para una agencia automotriz
class Vehiculo:
    # Constructor que inicializa los datos comerciales del vehículo
    def __init__(self, marca, modelo, anio, precio):
        self.marca = marca  # Guarda la marca del vehículo
        self.modelo = modelo  # Guarda el modelo
        self.anio = anio  # Guarda el año de fabricación
        self.precio = precio  # Guarda el precio en Guaraníes

    # Método que devuelve la descripción comercial lista para ser publicada
    def obtener_descripcion_comercial(self):
        return f"{self.marca} {self.modelo} {self.anio} - {self.precio:,.0f} Gs."  # Formatea con f-strings

    # Método especial para mostrar el objeto en formato legible
    def __str__(self):
        return self.obtener_descripcion_comercial()  # Retorna la descripción comercial


# Bloque de ejecución principal
if __name__ == "__main__":
    # Creación del primer vehículo de la agencia
    v1 = Vehiculo("Toyota", "Corolla", 2020, 95000000)
    # Creación del segundo vehículo
    v2 = Vehiculo("Hyundai", "HB20", 2022, 78000000)

    # Impresión de las ofertas de vehículos
    print("Oferta 1:", v1)
    print("Oferta 2:", v2)