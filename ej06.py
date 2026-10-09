# Definición de la clase CuentaCorriente
class CuentaCorriente:
    # Constructor que inicia con el titular y un saldo inicial
    def __init__(self, cliente, saldo_inicial=0.0):
        self.cliente = cliente  # Nombre del titular de la cuenta
        self.saldo = saldo_inicial  # Saldo disponible actual

    # Método para acreditar dinero a la cuenta
    def acreditar(self, monto):
        if monto > 0:  # Valida que el monto ingresado sea positivo
            self.saldo += monto  # Suma el monto al saldo actual
            print(f"[ACREDITACIÓN] Se acreditaron {monto:,.0f} Gs. correctamente.")
        else:
            print("[ERROR] El monto a acreditar debe ser mayor a cero.")

    # Método para registrar consumo en la cuenta
    def registrar_consumo(self, monto):
        if monto <= 0:  # Valida que el monto consumido sea positivo
            print("[ERROR] El monto del consumo debe ser mayor a cero.")
        elif monto > self.saldo:  # Controla que no gaste más de lo que tiene
            print(f"[RECHAZADO] Saldo insuficiente ({self.saldo:,.0f} Gs.) para realizar el consumo de {monto:,.0f} Gs.")
        else:
            self.saldo -= monto  # Descuenta el monto consumido del saldo
            print(f"[CONSUMO] Consumo de {monto:,.0f} Gs. registrado con éxito.")

    # Representación en texto del estado de la cuenta
    def __str__(self):
        return f"Cuenta Corriente | Cliente: {self.cliente} | Saldo Actual: {self.saldo:,.0f} Gs."


# Bloque de ejecución principal
if __name__ == "__main__":
    # Creación de la cuenta corriente
    cuenta = CuentaCorriente("María Celeste", 100000)
    print(cuenta)

    # Carga de saldo adicional
    cuenta.acreditar(150000)
    print(cuenta)

    # Intento de compra exitosa
    cuenta.registrar_consumo(200000)
    print(cuenta)

    # Intento de compra rechazada por falta de fondos
    cuenta.registrar_consumo(80000)
    print(cuenta)