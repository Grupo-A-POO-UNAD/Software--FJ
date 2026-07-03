
# INTEGRANTES DEL EQUIPO DE TRABAJO (Paso # 5):
# Encargada: Karen Stefanny Gil Bohórquez
# Grupo: 213023A_2202

from abc import ABC, abstractmethod

class entidad(ABC):
    def __init__(self, id):
        self._id = id

    @property
    def id(self):
        return self._id

    @abstractmethod
    def mostrar_datos(self):
        pass