# app/encuesta.py

from typing import List, Optional
from app.pregunta import Pregunta
from app.grupo import Grupo
from app.participante import Participante
from app.informe import Informe
import csv

class Encuesta:
    def __init__(self, titulo: str, fechaCreacion: str = ""):
        self.titulo = titulo               # Almacena el título de la encuesta
        self.fechaCreacion = fechaCreacion  # Almacena la fecha de creación
        self.preguntas: List[Pregunta] = []  # Lista para almacenar las preguntas
        self.grupo: Optional[Grupo] = None  # Grupo al que se aplica la encuesta
        self.informes: List[Informe] = []   # Lista para almacenar informes generados

    def agregar_pregunta(self, pregunta: Pregunta) -> None:
        self.preguntas.append(pregunta)  # Agrega una pregunta a la lista de preguntas

    def aplicar_a_grupo(self, grupo: Grupo) -> None:
        self.grupo = grupo  # Asigna un grupo a la encuesta

    def cargar_participantes(self, csv_file: str) -> List[Participante]:
        participantes = []
        try:
            with open(csv_file, mode='r', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Asegurarse de que cada campo esté presente y manejar valores faltantes
                    nombre = row.get('nombre', '').strip()
                    correo = row.get('correo', '').strip()
                    edad_str = row.get('edad')
                    genero = row.get('genero', '').strip()
                    ubicacion = row.get('ubicacion', '').strip()

                    # Convertir edad a int solo si tiene un valor válido
                    edad = int(edad_str) if edad_str and edad_str.isdigit() else None

                    # Verificar que los campos obligatorios no estén vacíos
                    if nombre and correo and edad is not None and genero:
                        participante = Participante(
                            nombre=nombre,
                            correo=correo,
                            edad=edad,
                            genero=genero,
                            ubicacion=ubicacion
                        )
                        participantes.append(participante)
                        print(f"Participante agregado: {participante.nombre}")  # Mensaje de depuración
                    else:
                        print(f"Advertencia: Datos incompletos en la fila {row}")  # Mensaje de advertencia
            return participantes
        except Exception as e:
            print(f"Error al cargar participantes: {e}")
            return []

    def generar_informe(self) -> Informe:
        tasa_respuesta = 0.0  # Aquí podrías calcular la tasa de respuesta real
        resultados = {}       # Datos de resultados de la encuesta

        informe = Informe(titulo_encuesta=self.titulo, tasa_respuesta=tasa_respuesta, resultados=resultados)
        informe.calcular_estadisticas()
        self.informes.append(informe)
        return informe
