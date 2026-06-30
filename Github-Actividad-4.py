# =========================================================================
# INTEGRANTES DEL EQUIPO DE TRABAJO (Paso # 5):
# 1. [Yesid Leonardo Gómez Ramos]
# 2. [Nombre del Estudiante 2]
# Grupo: 213023A_2202
# =========================================================================

from abc import ABC, abstractmethod

# --- EXCEPCIONES PERSONALIZADAS (Manejo avanzado) ---
class GestionError(Exception):
    """Clase base para excepciones del sistema."""
    pass

class ReservaInvalidaError(GestionError):
    """Se lanza cuando una reserva no cumple con los requisitos."""
    pass

# --- CLASES BASE Y ABSTRACCIÓN ---
class Entidad(ABC):
    def __init__(self, id_entidad, nombre):
        self._id_entidad = id_entidad  # Encapsulamiento (Atributo protegido)
        self._nombre = nombre

    @property
    def id_entidad(self):
        return self._id_entidad

    @property
    def nombre(self):
        return self._nombre

    @abstractmethod
    def obtener_detalles(self):
        """Método abstracto para obligar al polimorfismo."""
        pass

# --- CLASES DERIVADAS (Herencia y Polimorfismo) ---
class Cliente(Entidad):
    def __init__(self, id_entidad, nombre, email):
        super().__init__(id_entidad, nombre)
        self.__email = email  # Atributo privado

    @property
    def email(self):
        return self.__email

    def obtener_detalles(self):
        return f"Cliente: {self.nombre} (ID: {self.id_entidad}) - Email: {self.__email}"

class Servicio(Entidad):
    def __init__(self, id_entidad, nombre, precio):
        super().__init__(id_entidad, nombre)
        self.__precio = precio

    @property
    def precio(self):
        return self.__precio

    def obtener_detalles(self):
        return f"Servicio: {self.nombre} - Precio: ${self.__precio:,}"

# --- SISTEMA DE RESERVAS ---
class Reserva:
    def __init__(self, id_reserva, cliente, servicio, fecha):
        self.__id_reserva = id_reserva
        self.__cliente = cliente
        self.__servicio = servicio
        self.__fecha = fecha

    def registrar(self):
        if not self.__cliente or not self.__servicio:
            raise ReservaInvalidaError("La reserva debe contener un Cliente y un Servicio válidos.")
        return f"Reserva {self.__id_reserva} confirmada para {self.__cliente.nombre} - {self.__servicio.nombre} el {self.__fecha}"