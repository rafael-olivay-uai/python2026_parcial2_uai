"""Bóvedas del Banco Mágico (paradigma orientado a objetos)."""
import csv


class Boveda:
    def __init__(self, propietario, galeones=0):
        self.propietario = propietario
        self._galeones = galeones

    @property
    def galeones(self):
        return self._galeones

    @galeones.setter
    def galeones(self, cantidad):
        if cantidad < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._galeones = cantidad

    def extraer(self, cantidad):
        if cantidad > self._galeones:
            raise ValueError("Saldo insuficiente")
        self._galeones -= cantidad

    def __str__(self):
        return f"Bóveda de {self.propietario}: {self._galeones} galeones"

    def __add__(self, other):
        return Boveda("Bóveda Combinada", self._galeones + other._galeones)


def cargar_bovedas(nombre_archivo):
    """Lee un CSV (propietario, galeones) y devuelve una lista de Bovedas."""
    bovedas = []
    try:
        with open(nombre_archivo, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                bovedas.append(Boveda(fila["propietario"], int(fila["galeones"])))
    except FileNotFoundError:
        print(f"No se encontró el archivo {nombre_archivo}")
    return bovedas


if __name__ == "__main__":
    bovedas = cargar_bovedas("bovedas.csv")
    for boveda in bovedas:
        print(boveda)
