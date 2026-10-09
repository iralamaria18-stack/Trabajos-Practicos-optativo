# Definición de la clase Producto para un almacén
class Producto:
    # Constructor que inicializa el nombre, precio y cantidad en stock
    def __init__(self, nombre, precio_unitario, stock):
        self.nombre = nombre  # Asigna el nombre del producto
        self.precio_unitario = precio_unitario  # Asigna el precio unitario en Guaraníes
        self.stock = stock  # Asigna las unidades disponibles en stock

    # Método que calcula y retorna el valor total del producto en stock
    def calcular_valor_total_stock(self):
        return self.precio_unitario * self.stock  # Multiplica el precio por la cantidad

    # Método especial que devuelve el producto representado en texto
    def __str__(self):
        # Muestra el nombre, precio formateado con puntos de miles y el stock actual
        return f"Producto: {self.nombre} | Precio: {self.precio_unitario:,.0f} Gs. | Stock: {self.stock} unidades | Total Stock: {self.calcular_valor_total_stock():,.0f} Gs."


# Bloque de ejecución principal
if __name__ == "__main__":
    # Creación del primer producto (almacén)
    prod1 = Producto("Yerba Mate 500g", 18000, 25)
    # Creación del segundo producto
    prod2 = Producto("Leche Entera 1L", 7500, 40)

    # Imprime la descripción completa del primer producto
    print(prod1)
    # Imprime la descripción completa del segundo producto
    print(prod2)