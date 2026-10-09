# Definición de la clase LineaTelefonica
class LineaTelefonica:
    # Constructor que inicializa los GB incluidos y el acumulador de consumo
    def __init__(self, numero, gb_incluidos):
        self.numero = numero  # Número telefónico de la línea
        self.gb_incluidos = gb_incluidos  # Paquete de GB contrados
        self.gb_consumidos = 0.0  # Acumulador inicializado en 0 GB

    # Método que registra consumos de megas o gigas
    def registrar_consumo(self, gb):
        if gb <= 0:  # Valida que el consumo informado sea mayor a cero
            print("[ERROR] El consumo debe ser un valor positivo.")
            return

        disponible = self.obtener_gb_disponibles()  # Consulta los GB restantes
        if disponible == 0:  # Verifica si el saldo ya está completamente agotado
            print(f"[PAQUETE AGOTADO] No podés navegar. Se agotaron los {self.gb_incluidos} GB del plan.")
        elif gb > disponible:  # Si el consumo solicitado supera el saldo actual
            print(f"[AVISO DE LÍMITE] Consumo de {gb:.2f} GB excede el saldo. Se consumieron {disponible:.2f} GB y el paquete se AGOTÓ.")
            self.gb_consumidos = self.gb_incluidos  # Se consume el saldo restante por completo
        else:
            self.gb_consumidos += gb  # Suma el consumo normal
            print(f"[CONSUMO] Consumo registrado: {gb:.2f} GB.")

    # Método que devuelve la cantidad de GB disponibles para usar
    def obtener_gb_disponibles(self):
        return max(0.0, self.gb_incluidos - self.gb_consumidos)  # Evita valores negativos

    # Método de representación gráfica del estado del plan
    def __str__(self):
        return f"Línea: {self.numero} | Plan: {self.gb_incluidos} GB | Consumido: {self.gb_consumidos:.2f} GB | Disponible: {self.obtener_gb_disponibles():.2f} GB"


# Bloque de ejecución principal
if __name__ == "__main__":
    # Creación de la línea con un plan de 10 GB
    linea = LineaTelefonica("0981-987654", gb_incluidos=10.0)
    print(linea)

    # Consumos progresivos de datos
    linea.registrar_consumo(3.5)
    print(linea)

    linea.registrar_consumo(6.0)
    print(linea)

    # Consumo que agota el límite máximo permitido
    linea.registrar_consumo(2.0)
    print(linea)