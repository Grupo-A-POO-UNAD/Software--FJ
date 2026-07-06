
#INTEGRANTES DEL EQUIPO DE TRABAJO (Paso # 5):
# 2. [Karen Stefanny Gil Bohórquez]
# Grupo: 213023A_2202

from entidad import Entidad

class cliente(Entidad):
    """
    Clase que representa un cliente del sistema.
    Hereda de la clase abstracta Entidad.
    """

    def __init__(self, nombre, cedula, correo, telefono):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__correo = correo
        self.__telefono = telefono

        # Se validan los datos al crear el objeto
        self.validar_datos()

    # PROPIEDADES (ENCAPSULAMIENTO)

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        self.validar_datos()

    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, nueva_cedula):
        self.__cedula = nueva_cedula
        self.validar_datos()

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, nuevo_correo):
        self.__correo = nuevo_correo
        self.validar_datos()

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):
        self.__telefono = nuevo_telefono
        self.validar_datos()

    # MÉTODOS OBLIGATORIOS

    def validar_datos(self):
        """
        Valida la información del cliente.
        """

        # Validar nombre
        if not self.__nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if len(self.__nombre) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres.")

        # Validar cédula
        if not self.__cedula.isdigit():
            raise ValueError("La cédula solo debe contener números.")

        # Validar correo
        if "@" not in self.__correo or "." not in self.__correo:
            raise ValueError("El correo electrónico no es válido.")

        # Validar teléfono
        if not self.__telefono.isdigit():
            raise ValueError("El teléfono solo debe contener números.")

        if len(self.__telefono) != 10:
            raise ValueError("El teléfono debe tener exactamente 10 dígitos.")

    def mostrar_datos(self):
        """
        Muestra la información del cliente.
        """
        print("========== CLIENTE ==========")
        print(f"Nombre   : {self.__nombre}")
        print(f"Cédula   : {self.__cedula}")
        print(f"Correo   : {self.__correo}")
        print(f"Teléfono : {self.__telefono}")
        print("=============================")

    def __str__(self):
        """
        Representación en texto del objeto.
        """
        return (
            f"Cliente(Nombre='{self.__nombre}', "
            f"Cédula='{self.__cedula}', "
            f"Correo='{self.__correo}', "
            f"Teléfono='{self.__telefono}')"
        )
