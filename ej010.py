# Importación de la clase Producto creada para reuso (o redefinida aquí para que sea autónomo)
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio unitario en Guaraníes


# Clase Item que relaciona un Producto con la cantidad comprada
class Item:
    # Constructor del ítem
    def __init__(self, producto, cantidad):
        self.producto = producto  # Objeto de clase Producto
        self.cantidad = cantidad  # Cantidad seleccionada

    # Método que calcula el subtotal del ítem
    def calcular_subtotal(self):
        return self.producto.precio * self.cantidad  # Multiplica precio por cantidad

    # Representación en texto del ítem en la lista de compras
    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad} un. @ {self.producto.precio:,.0f} Gs. c/u = Subtotal: {self.calcular_subtotal():,.0f} Gs."


# Clase Carrito que reúne los Ítems agregados por el cliente
class Carrito:
    # Constructor que inicializa el carrito vacío
    def __init__(self):
        self.items = []  # Lista interna para guardar los ítems

    # Método para agregar un producto indicando la cantidad
    def agregar_item(self, producto, cantidad):
        item = Item(producto, cantidad)  # Crea la instancia del ítem
        self.items.append(item)  # Agrega el ítem al carrito
        print(f"Agregado al carrito: {producto.nombre} (x{cantidad})")

    # Método para calcular el costo total general del carrito
    def calcular_total(self):
        return sum(item.calcular_subtotal() for item in self.items)  # Suma los subtotales

    # Método especial que genera el detalle de la compra en formato legible
    def __str__(self):
        res = "=== DETALLE DEL CARRITO DE COMPRAS ===\n"
        for item in self.items:  # Recorre y lista cada ítem
            res += f"- {item}\n"
        res += f"--------------------------------------\n"
        res += f"TOTAL A PAGAR: {self.calcular_total():,.0f} Gs."  # Muestra el total formateado
        return res


# Bloque de ejecución principal
if __name__ == "__main__":
    # Definición de productos de la tienda
    p1 = Producto("Mouse Inalámbrico", 120000)
    p2 = Producto("Teclado Mecánico", 350000)

    # Creación del carrito de compras
    carrito = Carrito()

    # Adición de ítems al carrito
    carrito.agregar_item(p1, 2)
    carrito.agregar_item(p2, 1)

    # Muestra el ticket final detallado
    print("\n" + str(carrito))