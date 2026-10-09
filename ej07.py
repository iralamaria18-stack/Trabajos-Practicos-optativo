# Definición de la clase ProductoStock
class ProductoStock:
    # Constructor que inicializa los valores y el límite mínimo para alertas
    def __init__(self, nombre, precio, stock_inicial, stock_minimo):
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio unitario
        self.stock = stock_inicial  # Stock físico actual
        self.stock_minimo = stock_minimo  # Límite mínimo para solicitar reposición

    # Método para reponer o ingresar mercadería al depósito
    def reponer_stock(self, cantidad):
        if cantidad > 0:  # Valida que la cantidad agregada sea positiva
            self.stock += cantidad  # Incrementa las unidades en stock
            print(f"[REPOSICIÓN] Se ingresaron {cantidad} unidades de {self.nombre}.")
        else:
            print("[ERROR] La cantidad a reponer debe ser positiva.")

    # Método para registrar la venta de productos
    def registrar_venta(self, cantidad):
        if cantidad <= 0:  # Valida que la cantidad a vender sea válida
            print("[ERROR] La cantidad a vender debe ser mayor a cero.")
        elif cantidad > self.stock:  # Controla que el stock no sea negativo
            print(f"[VENTA RECHAZADA] No hay suficiente stock de {self.nombre}. Stock actual: {self.stock}")
        else:
            self.stock -= cantidad  # Descuenta las unidades vendidas
            print(f"[VENTA] Venta realizada: {cantidad} unidades de {self.nombre}.")
            self._verificar_alerta_stock()  # Llama a la verificación interna de stock

    # Método auxiliar que verifica si el stock cayó por debajo del mínimo
    def _verificar_alerta_stock(self):
        if self.stock < self.stock_minimo:  # Evalúa la condición de alerta
            print(f"  --> ¡ALERTA REPOSICIÓN! El stock de '{self.nombre}' ({self.stock} un.) está por debajo del mínimo ({self.stock_minimo} un.).")

    # Método de representación de estado
    def __str__(self):
        return f"Producto: {self.nombre} | Stock Actual: {self.stock} un. | Mínimo Alerta: {self.stock_minimo} un."


# Bloque de ejecución principal
if __name__ == "__main__":
    # Creación del producto con stock inicial de 10 y mínimo de 5
    prod = ProductoStock("Aceite Vegetal 900ml", 12000, stock_inicial=10, stock_minimo=5)
    print(prod)

    # Venta que no activa la alerta todavía
    prod.registrar_venta(4)
    print(prod)

    # Venta que disminuye el stock por debajo del mínimo y dispara la alerta
    prod.registrar_venta(3)
    print(prod)

    # Reposición para reestablecer el nivel de inventario
    prod.reponer_stock(10)
    print(prod)