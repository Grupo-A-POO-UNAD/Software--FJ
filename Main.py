
# INTEGRANTES DEL EQUIPO DE TRABAJO (Paso # 5):
# 1. [Yesid Leonardo Gómez Ramos]
# 2. [Karen Stefanny Gil Bohórquez]
# Grupo: 213023A_2202

from cliente import Cliente

class Cliente (Entidad):
    def __init__(self, id, nombre, correo, telefono):
        super().__init__(id)
        self._nombre = nombre
        self._correo = correo
        self._telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        self._correo = valor

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        self._telefono = valor

    def mostrar_datos(self):
        return f"Cliente {self.id}: {self.nombre}, {self.correo}, {self.telefono}"