# Definición de la clase Habitacion para la administración de un hotel
class Habitacion:
    # Constructor con número, tipo, tarifa nocturna y estado de ocupación
    def __init__(self, numero, tipo, tarifa_por_noche):
        self.numero = numero  # Número de la habitación
        self.tipo = tipo  # Ej: 'Simple', 'Doble', 'Suite'
        self.tarifa_por_noche = tarifa_por_noche  # Precio por noche en Gs.
        self.ocupada = False  # Estado inicial: libre (False)

    # Método para ocupar la habitación
    def ocupar(self):
        if self.ocupada:  # Validación de estado previo
            print(f"[ERROR] La habitación {self.numero} ya se encuentra ocupada.")
        else:
            self.ocupada = True  # Modifica el estado a ocupada
            print(f"[HOTEL] Habitación {self.numero} ({self.tipo}) ha sido OCUPADA.")

    # Método para liberar la habitación al terminar la estadía
    def liberar(self):
        if not self.ocupada:  # Validación de estado previo
            print(f"[ERROR] La habitación {self.numero} ya está libre.")
        else:
            self.ocupada = False  # Cambia el estado a libre
            print(f"[HOTEL] Habitación {self.numero} ha sido LIBERADA con éxito.")

    # Método para calcular el costo total según las noches reservadas
    def calcular_costo_estadia(self, noches):
        if noches <= 0:  # Valida que la cantidad de noches sea coherente
            print("[ERROR] La cantidad de noches debe ser mayor a cero.")
            return 0
        return self.tarifa_por_noche * noches  # Multiplica noches por la tarifa

    # Método de representación textual del estado de la habitación
    def __str__(self):
        estado_str = "Ocupada" if self.ocupada else "Libre"
        return f"Habitación Nº: {self.numero} | Tipo: {self.tipo} | Tarifa/Noche: {self.tarifa_por_noche:,.0f} Gs. | Estado: [{estado_str}]"


# Bloque de ejecución principal
if __name__ == "__main__":
    # Instanciación de una habitación tipo Suite
    hab = Habitacion(numero=302, tipo="Suite Matrimonial", tarifa_por_noche=350000)
    print(hab)

    # Intento de ocupación
    hab.ocupar()
    print(hab)

    # Reintento fallido de ocupación
    hab.ocupar()

    # Cálculo de liquidación de estadía por 3 noches
    noches_estadia = 3
    costo_total = hab.calcular_costo_estadia(noches_estadia)
    print(f"\nCosto total de la estadía por {noches_estadia} noches: {costo_total:,.0f} Gs.")

    # Checkout / Liberación de la habitación
    hab.liberar()
    print(hab)