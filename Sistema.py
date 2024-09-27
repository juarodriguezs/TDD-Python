class Sistema:
    def __init__(self):
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        identificadores = map(lambda c: c.identificador, self.cuentas)
        if cuenta.identificador in identificadores:
            raise ValueError(f"Ya existe una cuenta con el identificador {cuenta.identificador}")
        self.cuentas.append(cuenta)
