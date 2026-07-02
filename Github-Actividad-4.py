# =========================================================================
# INTEGRANTES DEL EQUIPO DE TRABAJO (Paso # 5):
# 1. [Yesid Leonardo Gómez Ramos]
# 2. [Nombre del Estudiante 2]
# Grupo: 213023A_2202
# =========================================================================

from abc import ABC, abstractmethod

# -------------------------
# Clase abstracta (Padre)
# -------------------------
class Servicio(ABC):

    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# -------------------------
# Clase hija 1
# -------------------------
class ReservaSala(Servicio):

    def __init__(self, nombre, horas):
        super().__init__(nombre)
        self.horas = horas

    def calcular_costo(self):
        return self.horas * 50000

    def descripcion(self):
        return f"Reserva de sala: {self.nombre}"


# -------------------------
# Clase hija 2
# -------------------------
class AlquilerEquipo(Servicio):

    def __init__(self, nombre, dias):
        super().__init__(nombre)
        self.dias = dias

    def calcular_costo(self):
        return self.dias * 30000

    def descripcion(self):
        return f"Alquiler de equipo: {self.nombre}"


# -------------------------
# Clase hija 3
# -------------------------
class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, horas):
        super().__init__(nombre)
        self.horas = horas

    def calcular_costo(self):
        return self.horas * 80000

    def descripcion(self):
        return f"Asesoría especializada: {self.nombre}"


# -------------------------
# Programa principal
# -------------------------
servicios = [
    ReservaSala("Sala de reuniones", 2),
    AlquilerEquipo("VideoBeam", 3),
    AsesoriaEspecializada("Python", 4)
]

print("=== SERVICIOS DISPONIBLES ===\n")

for servicio in servicios:
    print(servicio.descripcion())
    print(f"Costo: ${servicio.calcular_costo()}")
    print("-" * 30)