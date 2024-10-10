# app/encuesta.py

from typing import List, Optional
from app.pregunta import Pregunta
from app.grupo import Grupo
from app.participante import Participante
from app.informe import Informe
import csv

class Encuesta:
    def __init__(self, titulo: str, fechaCreacion: str = ""):
        self.titulo = titulo
        self.fechaCreacion = fechaCreacion
        self.preguntas = []
        self.grupo = None
        self.informes = []

    def agregar_pregunta(self, pregunta: Pregunta) -> None:
        self.preguntas.append(pregunta)

    def aplicar_a_grupo(self, grupo: Grupo) -> None:
        self.grupo = grupo

    def cargar_participantes(self, csv_file: str) -> List[Participante]:
        participantes = []
        try:
            with open(csv_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    participante = Participante(
                        nombre=row.get('nombre'),
                        correo=row.get('correo'),
                        edad=int(row.get('edad')),
                        genero=row.get('genero'),
                        ubicacion=row.get('ubicacion', '')
                    )
                    participantes.append(participante)
            return participantes
        except Exception as e:
            print(f"Error al cargar participantes: {e}")
            return []

    def generar_informe(self) -> Informe:
        # Calcula aquí la tasa de respuesta u otros datos y pasa solo los datos necesarios
        tasa_respuesta = 0.0  # Aquí podrías calcular la tasa de respuesta real
        resultados = {}       # Datos de resultados de la encuesta

        informe = Informe(titulo_encuesta=self.titulo, tasa_respuesta=tasa_respuesta, resultados=resultados)
        informe.calcular_estadisticas()
        self.informes.append(informe)
        return informe
