# =========================================================================
# INTEGRANTES DEL EQUIPO DE TRABAJO:
# 1. Yesid Leonardo Gómez Ramos (Encargado: Herencia, Polimorfismo y Excepciones)
# Grupo: 213023A_2202
# =========================================================================

from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import messagebox

# -------------------------------------------------------------------------
# EXCEPCIONES PERSONALIZADAS
# -------------------------------------------------------------------------
class ServicioError(Exception):
    """Clase base para errores en los servicios de Software FJ."""
    pass

class ParametrosInvalidosError(ServicioError):
    """Se lanza cuando los parámetros numéricos o de entrada son incorrectos."""
    pass


# -------------------------------------------------------------------------
# CLASE ABSTRACTA BASE (Abstracción)
# -------------------------------------------------------------------------
class Servicio(ABC):

    def __init__(self, nombre):
        if not nombre:
            raise ParametrosInvalidosError("El nombre del servicio no puede estar vacío.")
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self, descuento=0.0):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# -------------------------------------------------------------------------
# CLASES HIJAS (Herencia y Polimorfismo)
# -------------------------------------------------------------------------

class ReservaSala(Servicio):

    def __init__(self, nombre, horas):
        super().__init__(nombre)
        if not isinstance(horas, (int, float)) or horas <= 0:
            raise ParametrosInvalidosError(f"Las horas de la sala '{nombre}' deben ser mayores a cero.")
        self.horas = horas

    def calcular_costo(self, descuento=0.0):
        try:
            if descuento < 0.0 or descuento > 1.0:
                raise ParametrosInvalidosError("El descuento debe estar entre 0.0 y 1.0")
            costo_base = self.horas * 50000
            costo_final = costo_base - (costo_base * descuento)
        except ParametrosInvalidosError as e:
            raise ServicioError("Error interno al calcular costo de Sala") from e  # Encadenamiento
        else:
            return int(costo_final)
        finally:
            pass  # Bloque final

    def descripcion(self):
        return f"Reserva de sala: {self.nombre} ({self.horas} horas)"


class AlquilerEquipo(Servicio):

    def __init__(self, nombre, dias):
        super().__init__(nombre)
        if not isinstance(dias, (int, float)) or dias <= 0:
            raise ParametrosInvalidosError(f"Los días para '{nombre}' deben ser mayores a cero.")
        self.dias = dias

    def calcular_costo(self, descuento=0.0):
        try:
            if descuento < 0.0 or descuento > 1.0:
                raise ParametrosInvalidosError("El descuento debe estar entre 0.0 y 1.0")
            costo_base = self.dias * 30000
            costo_final = costo_base - (costo_base * descuento)
        except ParametrosInvalidosError as e:
            raise ServicioError("Error interno al calcular costo de Equipo") from e
        else:
            return int(costo_final)

    def descripcion(self):
        return f"Alquiler de equipo: {self.nombre} ({self.dias} días)"


class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, horas):
        super().__init__(nombre)
        if not isinstance(horas, (int, float)) or horas <= 0:
            raise ParametrosInvalidosError(f"Las horas de asesoría para '{nombre}' deben ser mayores a cero.")
        self.horas = horas

    def calcular_costo(self, descuento=0.0):
        try:
            if descuento < 0.0 or descuento > 1.0:
                raise ParametrosInvalidosError("El descuento debe estar entre 0.0 y 1.0")
            costo_base = self.horas * 80000
            costo_final = costo_base - (costo_base * descuento)
        except ParametrosInvalidosError as e:
            raise ServicioError("Error interno al calcular costo de Asesoría") from e
        else:
            return int(costo_final)

    def descripcion(self):
        return f"Asesoría especializada: {self.nombre} ({self.horas} horas)"


# -------------------------------------------------------------------------
# INTERFAZ GRÁFICA (Tkinter)
# -------------------------------------------------------------------------

def mostrar_servicios():
    texto = "--- OPERACIONES EXITOSAS ---\n"
    
    # 1. Simulación de Casos Válidos (Polimorfismo en acción)
    servicios_validos = [
        ReservaSala("Sala de reuniones", 2),
        AlquilerEquipo("VideoBeam", 3),
        AsesoriaEspecializada("Python Avanzado", 4)
    ]
    
    for servicio in servicios_validos:
        texto += servicio.descripcion()
        texto += f"\nCosto: ${servicio.calcular_costo()}\n"
        texto += "-" * 30 + "\n"

    # 2. Simulación de Casos Inválidos (Prueba de Estabilidad ante Errores Graves)
    texto += "\n--- PRUEBA DE ERRORES CONTROLADOS ---\n"
    
    # Intento 1: Crear servicio con horas negativas
    try:
        texto += "Intentando registrar Sala con horas inválidas (-2)...\n"
        sala_error = ReservaSala("Sala de Juntas", -2)
    except ParametrosInvalidosError as e:
        # El programa no se cae, captura el error y continúa de forma secuencial
        texto += f"⚠️ Excepción controlada: {e}\n"
        texto += "-" * 30 + "\n"

    # Intento 2: Calcular costo con un descuento dañado (ej: 150%)
    try:
        texto += "Intentando aplicar descuento inválido (1.5)...\n"
        equipo = AlquilerEquipo("Laptop", 2)
        costo = equipo.calcular_costo(descuento=1.5)
    except ServicioError as e:
        texto += f"⚠️ Excepción controlada: {e} (Origen: {e.__cause__})\n"
        texto += "-" * 30 + "\n"

    # Muestra todo el reporte unificado en la ventana gráfica
    messagebox.showinfo("Reporte de Operaciones - Software FJ", texto)


def obtener_servicios():
    """Función puente que puede usarse"""
    return [
        ReservaSala("Sala de reuniones", 2),
        AlquilerEquipo("VideoBeam", 3),
        AsesoriaEspecializada("Python", 4)
    ]


# --- Construcción de la Ventana Principal ---
ventana = tk.Tk()
ventana.title("Módulo de Servicios - Software FJ")
ventana.geometry("350x180")

# Etiqueta de inforción
lbl_info = tk.Label(ventana, text="Fase de Validación Secuencial\nHerencia, Polimorfismo y Excepciones", font=("Arial", 9, "italic"))
lbl_info.pack(pady=15)

# Flujo avanzado de validación
boton = tk.Button(
    ventana,
    text="Ejecutar Simulación de Operaciones",
    command=mostrar_servicios,
    bg="#0e79e4",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5
)
boton.pack(pady=10)

if __name__ == "__main__":
    ventana.mainloop()
