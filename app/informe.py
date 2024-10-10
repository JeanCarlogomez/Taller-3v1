# app/informe.py

class Informe:
    def __init__(self, titulo_encuesta: str, tasa_respuesta: float = 0.0, resultados: dict = None):
        self.titulo_encuesta = titulo_encuesta
        self.tasa_respuesta = tasa_respuesta
        self.resultados = resultados if resultados else {}

    def calcular_estadisticas(self) -> None:
        # Aquí puedes implementar lógica para calcular estadísticas y almacenar en `resultados`
        pass
