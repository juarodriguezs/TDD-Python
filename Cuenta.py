class Cuenta:
    def __init__(self, identificador: int, titular: str, tipo: str, saldo: int):
        self.identificador = identificador
        self.titular = titular
        self.tipo = tipo
        self.saldo = saldo

    def cargar_puntos(self, puntos: int):
        self.saldo += puntos
        return self.saldo

    def redimir_puntos(self, puntos: int):
        if puntos > self.saldo:
            raise ValueError(f"No tiene saldo suficiente para redimir {puntos} puntos. Saldo disponible: {self.saldo}")
        self.saldo -= puntos
        return self.saldo
