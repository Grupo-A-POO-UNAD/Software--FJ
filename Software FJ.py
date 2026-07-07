# ============================================================================
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA - UNAD
# Curso: Programacion
# Fase 4 - Proyecto Integrador
#
# Sistema Integral de Gestion de Clientes, Servicios y Reservas
# Empresa: Software FJ
# ============================================================================

# ============================================================================
# INTEGRANTES DEL EQUIPO
#
# Yesid Leonardo Gomez Ramos
# - Herencia
# - Polimorfismo
# - Servicios
#
# Karen Stefanny Gil Bohorquez
# - Clase Cliente
# - Encapsulamiento
# - Validacion de datos
#
# Daniel Garzon
# - Excepciones
# - Logs
# - Integracion del proyecto
# ============================================================================

from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# ============================================================================
# EXCEPCIONES PERSONALIZADAS
# ============================================================================

class GestionError(Exception):
    """Clase base de excepciones."""
    pass


class ServicioError(GestionError):
    pass


class ParametrosInvalidosError(ServicioError):
    pass


class ClienteError(GestionError):
    pass


class ReservaError(GestionError):
    pass
# ============================================================================
# REGISTRO DE LOGS
# ============================================================================

def registrar_log(mensaje):

    try:

        with open("software_fj.log", "a", encoding="utf-8") as archivo:

            fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            archivo.write(f"[{fecha}] {mensaje}\n")

    except Exception as e:

        print("No fue posible escribir el archivo log.", e)
# ============================================================================
# CLASE ABSTRACTA ENTIDAD
# (Karen + Integracion)
# ============================================================================

class Entidad(ABC):

    def __init__(self, id):

        self._id = id

    @property
    def id(self):

        return self._id

    @abstractmethod
    def mostrar_datos(self):
        pass
# ============================================================================
# CLASE CLIENTE
# ============================================================================

class Cliente(Entidad):

    def __init__(self, id, nombre, cedula, correo, telefono):

        super().__init__(id)

        self.nombre = nombre
        self.cedula = cedula
        self.correo = correo
        self.telefono = telefono

        self.validar_datos()

    # ----------------------------

    def validar_datos(self):

        if self.nombre.strip() == "":

            raise ClienteError("Nombre invalido.")

        if len(self.nombre) < 3:

            raise ClienteError(
                "El nombre debe tener minimo tres caracteres."
            )

        if not self.cedula.isdigit():

            raise ClienteError(
                "La cedula solo debe contener numeros."
            )

        if "@" not in self.correo:

            raise ClienteError(
                "Correo invalido."
            )

        if not self.telefono.isdigit():

            raise ClienteError(
                "Telefono invalido."
            )

        if len(self.telefono) != 10:

            raise ClienteError(
                "Telefono debe tener diez digitos."
            )

    # ----------------------------

    def mostrar_datos(self):

        return (
            f"Cliente: {self.nombre}\n"
            f"Cedula: {self.cedula}\n"
            f"Correo: {self.correo}\n"
            f"Telefono: {self.telefono}"
        )

    def __str__(self):

        return f"{self.nombre} ({self.cedula})"
# ============================================================================
# CLASE ABSTRACTA SERVICIO
# (Yesid + Integracion)
# ============================================================================

class Servicio(Entidad, ABC):

    def __init__(self, id, nombre):

        super().__init__(id)

        if not nombre.strip():
            raise ParametrosInvalidosError(
                "El nombre del servicio no puede estar vacio."
            )

        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self, descuento=0):
        pass

    @abstractmethod
    def descripcion(self):
        pass

    def calcular_costo_con_impuesto(self, impuesto=0.19):

        return self.calcular_costo() * (1 + impuesto)

    def mostrar_datos(self):

        return self.descripcion()
# ============================================================================
# RESERVA DE SALA
# ============================================================================

class ReservaSala(Servicio):

    def __init__(self, id, nombre, horas):

        super().__init__(id, nombre)

        if horas <= 0:

            raise ParametrosInvalidosError(
                "Las horas deben ser mayores que cero."
            )

        self.horas = horas

    def calcular_costo(self, descuento=0):

        try:

            if descuento < 0 or descuento > 1:

                raise ParametrosInvalidosError(
                    "Descuento invalido."
                )

            costo = self.horas * 50000

            return int(costo - costo * descuento)

        except ParametrosInvalidosError as e:

            registrar_log(f"[ERROR SALA] {e}")

            raise ServicioError(
                "Error al calcular costo."
            )

        finally:

            print(f"Servicio procesado: {self.nombre}")

    def descripcion(self):

        return (
            f"Sala: {self.nombre}\n"
            f"Horas: {self.horas}"
        )
# ============================================================================
# ALQUILER DE EQUIPO
# ============================================================================

class AlquilerEquipo(Servicio):

    def __init__(self, id, nombre, dias):

        super().__init__(id, nombre)

        if dias <= 0:

            raise ParametrosInvalidosError(
                "Los dias deben ser mayores que cero."
            )

        self.dias = dias

    def calcular_costo(self, descuento=0):

        try:

            if descuento < 0 or descuento > 1:

                raise ParametrosInvalidosError(
                    "Descuento invalido."
                )

            costo = self.dias * 30000

            return int(costo - costo * descuento)

        except ParametrosInvalidosError as e:

            registrar_log(f"[ERROR EQUIPO] {e}")

            raise ServicioError(
                "Error al calcular costo."
            )

        finally:

            print(f"Servicio procesado: {self.nombre}")

    def descripcion(self):

        return (
            f"Equipo: {self.nombre}\n"
            f"Dias: {self.dias}"
        )
# ============================================================================
# ASESORIA ESPECIALIZADA
# ============================================================================

class AsesoriaEspecializada(Servicio):

    def __init__(self, id, nombre, horas):

        super().__init__(id, nombre)

        if horas <= 0:

            raise ParametrosInvalidosError(
                "Las horas deben ser mayores que cero."
            )

        self.horas = horas

    def calcular_costo(self, descuento=0):

        try:

            if descuento < 0 or descuento > 1:

                raise ParametrosInvalidosError(
                    "Descuento invalido."
                )

            costo = self.horas * 80000

            return int(costo - costo * descuento)

        except ParametrosInvalidosError as e:

            registrar_log(f"[ERROR ASESORIA] {e}")

            raise ServicioError(
                "Error al calcular costo."
            )

        finally:

            print(f"Servicio procesado: {self.nombre}")

    def descripcion(self):

        return (
            f"Asesoria: {self.nombre}\n"
            f"Horas: {self.horas}"
        )
# ============================================================================
# CLASE RESERVA
# (Integracion del proyecto)
# ============================================================================

class Reserva:

    def __init__(self, cliente, servicio):

        if not isinstance(cliente, Cliente):

            raise ReservaError("Debe seleccionar un cliente valido.")

        if not isinstance(servicio, Servicio):

            raise ReservaError("Debe seleccionar un servicio valido.")

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Confirmada"

    def mostrar_datos(self):

        return (
            f"Cliente : {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Estado  : {self.estado}"
        )

    def cancelar(self):

        self.estado = "Cancelada"
# ============================================================================
# LISTAS
# ============================================================================

clientes = []
servicios = []
reservas = []
from tkinter.scrolledtext import ScrolledText

def simular_diez_operaciones():

    clientes.clear()
    servicios.clear()
    reservas.clear()

    reporte = "========== SOFTWARE FJ ==========\n\n"

    # =====================================================
    # REGISTRO DE CLIENTE
    # =====================================================

    try:

        cliente = Cliente(
            1,
            "Daniel Garzon",
            "123456789",
            "daniel@email.com",
            "3001234567"
        )

        clientes.append(cliente)

        reporte += "===== CLIENTE REGISTRADO =====\n"
        reporte += cliente.mostrar_datos()
        reporte += "\n\n"

    except Exception as e:

        reporte += f"Error al registrar cliente: {e}\n\n"

    # =====================================================
    # REGISTRO DE SERVICIOS
    # =====================================================

    try:

        sala = ReservaSala(
            1,
            "Sala Audiovisual",
            4
        )

        servicios.append(sala)

    except Exception as e:

        reporte += f"Error: {e}\n"

    try:

        equipo = AlquilerEquipo(
            2,
            "VideoBeam Epson",
            3
        )

        servicios.append(equipo)

    except Exception as e:

        reporte += f"Error: {e}\n"

    try:

        asesoria = AsesoriaEspecializada(
            3,
            "Arquitectura Python",
            5
        )

        servicios.append(asesoria)

    except Exception as e:

        reporte += f"Error: {e}\n"

    # =====================================================
    # RESERVA
    # =====================================================

    try:

        reserva = Reserva(cliente, sala)

        reservas.append(reserva)

        reporte += "===== RESERVA =====\n"
        reporte += reserva.mostrar_datos()
        reporte += "\n\n"

    except Exception as e:

        reporte += f"Error al crear reserva: {e}\n\n"

    # =====================================================
    # SERVICIOS
    # =====================================================

    reporte += "===== SERVICIOS REGISTRADOS =====\n\n"

    contador = 1

    for servicio in servicios:

        try:

            costo = servicio.calcular_costo(0.10)

            reporte += f"Servicio {contador}\n"
            reporte += servicio.descripcion() + "\n"
            reporte += f"Costo con descuento: ${costo}\n"
            reporte += "-" * 35 + "\n"

            contador += 1

        except Exception as e:

            reporte += f"Error: {e}\n"

    # =====================================================
    # EXCEPCIONES
    # =====================================================

    reporte += "\n===== PRUEBA DE EXCEPCIONES =====\n"

    try:

        ReservaSala(
            4,
            "Sala Premium",
            0
        )

    except Exception as e:

        registrar_log(str(e))

        reporte += "✓ Horas invalidas detectadas.\n"

    try:

        Cliente(
            2,
            "",
            "ABC",
            "correo",
            "123"
        )

    except Exception as e:

        registrar_log(str(e))

        reporte += "✓ Cliente invalido detectado.\n"

    # =====================================================
    # RESUMEN
    # =====================================================

    reporte += "\n=====================================\n"
    reporte += "RESUMEN DEL SISTEMA\n"
    reporte += "=====================================\n\n"

    reporte += f"Clientes registrados : {len(clientes)}\n"
    reporte += f"Servicios registrados: {len(servicios)}\n"
    reporte += f"Reservas registradas : {len(reservas)}\n"

    return reporte
# ============================================================================
# FUNCIONES
# ============================================================================

def mostrar_servicios():

    reporte = simular_diez_operaciones()

    cuadro_texto.config(state="normal")
    cuadro_texto.delete("1.0", tk.END)
    cuadro_texto.insert(tk.END, reporte)
    cuadro_texto.config(state="disabled")


# ============================================================================
# INTERFAZ GRAFICA
# ============================================================================

ventana = tk.Tk()

ventana.title("Software FJ")
ventana.geometry("650x500")
ventana.resizable(False, False)

# ============================================
# TITULO
# ============================================

titulo = tk.Label(
    ventana,
    text="Sistema Integral de Gestion de Clientes, Servicios y Reservas",
    font=("Arial", 14, "bold")
)

titulo.pack(pady=10)

# ============================================
# SUBTITULO
# ============================================

subtitulo = tk.Label(
    ventana,
    text="Clientes - Servicios - Reservas",
    font=("Arial", 10)
)

subtitulo.pack()

# ============================================
# DESCRIPCION DEL PROYECTO
# ============================================

descripcion = tk.Label(
    ventana,
    text=(
        "Proyecto desarrollado utilizando\n"
        "Programacion Orientada a Objetos\n\n"
        "Herencia | Polimorfismo | Encapsulamiento\n"
        "Excepciones | Registro de Logs"
    ),
    font=("Arial",10),
    justify="center"
)

descripcion.pack(pady=10)

# ============================================
# BOTON
# ============================================

boton = tk.Button(
    ventana,
    text="Ejecutar Simulacion",
    command=mostrar_servicios,
    bg="#1E88E5",
    fg="white",
    font=("Arial",10,"bold"),
    width=25
)

boton.pack(pady=10)

# ============================================
# AREA DE RESULTADOS
# ============================================

cuadro_texto = ScrolledText(
    ventana,
    width=75,
    height=18,
    font=("Consolas",10)
)

cuadro_texto.pack(padx=15, pady=10)

cuadro_texto.config(state="disabled")

if __name__ == "__main__":
    ventana.mainloop()