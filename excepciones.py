"""
==========================================================
Archivo: excepciones.py
Participante encargado: Daniel Garzon
Grupo:213023_55
==========================================================
"""

# ==========================================================
# EXCEPCIÓN BASE DEL SISTEMA
# ==========================================================

class GestionError(Exception):
    """
    Clase base para todas las excepciones del sistema.

    Todas las excepciones personalizadas heredarán de esta clase,
    permitiendo capturar cualquier error del sistema mediante
    una única excepción general cuando sea necesario.
    """

    def __init__(self, mensaje="Ha ocurrido un error en el sistema."):
        super().__init__(mensaje)


# ==========================================================
# EXCEPCIONES RELACIONADAS CON CLIENTES
# ==========================================================

class ClienteInvalidoError(GestionError):
    """
    Se produce cuando la información del cliente
    no cumple con las validaciones requeridas.
    """

    def __init__(self, mensaje="Los datos del cliente son inválidos."):
        super().__init__(mensaje)


# ==========================================================
# EXCEPCIONES RELACIONADAS CON SERVICIOS
# ==========================================================

class ServicioError(GestionError):
    """
    Clase base para errores relacionados con los servicios.
    """

    def __init__(self, mensaje="Ha ocurrido un error con el servicio."):
        super().__init__(mensaje)


class ServicioNoDisponibleError(ServicioError):
    """
    Se genera cuando el servicio solicitado
    no se encuentra disponible.
    """

    def __init__(self, mensaje="El servicio solicitado no está disponible."):
        super().__init__(mensaje)


class PrecioInvalidoError(ServicioError):
    """
    Se genera cuando el precio del servicio
    es incorrecto.
    """

    def __init__(self, mensaje="El precio del servicio es inválido."):
        super().__init__(mensaje)


# ==========================================================
# EXCEPCIONES RELACIONADAS CON RESERVAS
# ==========================================================

class ReservaError(GestionError):
    """
    Clase base para errores relacionados con las reservas.
    """

    def __init__(self, mensaje="Ha ocurrido un error en la reserva."):
        super().__init__(mensaje)


class ReservaInvalidaError(ReservaError):
    """
    Se produce cuando una reserva
    contiene información incorrecta.
    """

    def __init__(self, mensaje="La reserva es inválida."):
        super().__init__(mensaje)


class DuracionInvalidaError(ReservaError):
    """
    Se produce cuando la duración de la reserva
    no cumple con los requisitos establecidos.
    """

    def __init__(self, mensaje="La duración de la reserva es inválida."):
        super().__init__(mensaje)


class EstadoReservaError(ReservaError):
    """
    Se produce cuando el estado actual de una reserva
    no permite realizar una determinada operación.
    """

    def __init__(self, mensaje="El estado de la reserva no permite realizar esta operación."):
        super().__init__(mensaje)