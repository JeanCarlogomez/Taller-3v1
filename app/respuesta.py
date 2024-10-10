from app.pregunta import Pregunta
from app.usuario import Usuario

class Respuesta:
    def __init__(self, pregunta: Pregunta, usuario: Usuario, valor: str):
        self.pregunta = pregunta
        self.usuario = usuario
        self.valor = valor
