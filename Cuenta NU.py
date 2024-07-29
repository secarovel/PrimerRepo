class CuentaAhorros:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.tasa_anual = 0.13
        self.tasa_diaria = (1 + self.tasa_anual) ** (1 / 365) - 1

    def ingresar_dinero(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Ingresado: ${cantidad:.2f}. Saldo actual: ${self.saldo:.2f}")
        else:
            print("La cantidad a ingresar debe ser positiva.")

    def capitalizar_diariamente(self, dias):
        for dia in range(1, dias + 1):
            intereses = self.saldo * self.tasa_diaria
            self.saldo += intereses
            print(f"Día {dia}: Intereses: ${intereses:.2f}. Saldo actual: ${self.saldo:.2f}")

# Ejemplo de uso
cuenta = CuentaAhorros(0)  # Crear una cuenta con un saldo inicial de $1000
cuenta.ingresar_dinero(2000000000)   # Ingresar $500
cuenta.capitalizar_diariamente(365)  # Capitalizar diariamente durante 30 días
