"""
==========================================================
Archivo: logger_config.py
Participante encargado:Daniel Garzon 
Grupo:213023_55
==========================================================
"""

import logging
import os

# ==========================================================
# RUTA DEL ARCHIVO DE LOGS
# ==========================================================

# Obtiene la carpeta donde se encuentra este archivo.
RUTA_ACTUAL = os.path.dirname(os.path.abspath(__file__))

# Crea la ruta completa del archivo logs.txt.
ARCHIVO_LOG = os.path.join(RUTA_ACTUAL, "logs.txt")


# ==========================================================
# CONFIGURACIÓN DEL LOGGER
# ==========================================================

logging.basicConfig(
    filename=ARCHIVO_LOG,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger("SoftwareFJ")


# ==========================================================
# FUNCIONES AUXILIARES
# ==========================================================

def registrar_info(mensaje):
    """
    Registra un evento informativo.
    """
    logger.info(mensaje)


def registrar_advertencia(mensaje):
    """
    Registra una advertencia del sistema.
    """
    logger.warning(mensaje)


def registrar_error(mensaje):
    """
    Registra un error del sistema.
    """
    logger.error(mensaje)


def registrar_excepcion(excepcion):
    """
    Registra una excepción incluyendo
    toda la información del traceback.
    """
    logger.exception(excepcion)