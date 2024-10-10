from app.participante import Participante

class Grupo:
    def __init__(self, nombre: str, criterios: dict = None):
        self.nombre = nombre
        self.criterios = criterios if criterios else {}
        self.participantes = []

    def agregar_participante(self, participante: Participante) -> None:
        self.participantes.append(participante)
