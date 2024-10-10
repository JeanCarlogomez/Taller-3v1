# app/main.py

from app.encuesta import Encuesta
from app.pregunta import Pregunta
from app.grupo import Grupo

def main():
    # Crear una encuesta
    encuesta = Encuesta(titulo="Encuesta de Satisfacción", fechaCreacion="2024-10-10")
    print(f"Encuesta creada: {encuesta.titulo}, Fecha: {encuesta.fechaCreacion}")

    # Agregar preguntas a la encuesta
    pregunta1 = Pregunta(texto="¿Cómo calificaría el servicio?", tipo="selección múltiple")
    pregunta2 = Pregunta(texto="¿Recomendaría nuestro servicio a otros?", tipo="sí/no")
    encuesta.agregar_pregunta(pregunta1)
    encuesta.agregar_pregunta(pregunta2)
    print(f"Preguntas agregadas: {[p.texto for p in encuesta.preguntas]}")

    # Crear un grupo y asignarlo a la encuesta
    grupo = Grupo(nombre="Clientes VIP", criterios={"edad": ">= 30"})
    encuesta.aplicar_a_grupo(grupo)
    print(f"Grupo asignado a la encuesta: {grupo.nombre} con criterios {grupo.criterios}")

    # Cargar participantes desde el archivo CSV en la carpeta app
    participantes = encuesta.cargar_participantes("app/participantes.csv")
    for participante in participantes:
        grupo.agregar_participante(participante)
    print(f"Participantes en el grupo '{grupo.nombre}': {[p.nombre for p in grupo.participantes]}")

    # Generar un informe de la encuesta
    informe = encuesta.generar_informe()
    print("Informe generado de la encuesta.")
    print(f"Tasa de respuesta calculada en el informe: {informe.tasa_respuesta}")
    print(f"Resultados del informe: {informe.resultados}")

if __name__ == "__main__":
    main()
