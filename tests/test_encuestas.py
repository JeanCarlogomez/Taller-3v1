import pytest
from app import encuesta, pregunta, respuesta, usuario, grupo

# Pruebas para la clase Encuesta
def test_crear_encuesta():
    encuesta = encuesta(titulo="Encuesta de Satisfacción", fechaCreacion="2024-10-03")
    assert encuesta.titulo == "Encuesta de Satisfacción"

def test_agregar_pregunta():
    encuesta = encuesta(titulo="Encuesta de Satisfacción")
    pregunta1 = pregunta(texto="¿Cómo calificaría el servicio?")
    pregunta2 = pregunta(texto="¿Recomendaría el servicio?")
    pregunta3 = pregunta(texto="¿Cómo mejoraría el servicio?")
    encuesta.agregar_pregunta(pregunta1)
    encuesta.agregar_pregunta(pregunta2)
    encuesta.agregar_pregunta(pregunta3)
    assert len(encuesta.preguntas) == 3

# Pruebas para la clase Pregunta
def test_crear_pregunta():
    pregunta = pregunta(texto="¿Cuál es su edad?")
    assert pregunta.texto == "¿Cuál es su edad?"

# Pruebas para la clase Respuesta
def test_crear_respuesta():
    usuario = usuario(nombre="Juan Pérez", email="juan@example.com")
    pregunta = pregunta(texto="¿Cómo calificaría el servicio?")
    respuesta = respuesta(pregunta, usuario, "Excelente")
    assert respuesta.valor == "Excelente"

# Pruebas para la clase Usuario
def test_crear_usuario():
    usuario = usuario(nombre="Ana García", email="ana@example.com")
    assert usuario.nombre == "Ana García"

# Pruebas para la clase Grupo
def test_crear_grupo():
    grupo = grupo(nombre="Clientes VIP", criterios={"edad": ">= 30"})
    assert grupo.nombre == "Clientes VIP"

# Pruebas para la integración entre clases
def test_encuesta_con_grupo():
    encuesta = encuesta(titulo="Encuesta de Satisfacción")
    grupo = grupo(nombre="Clientes VIP")
    encuesta.aplicar_a_grupo(grupo)
    assert encuesta.grupo == grupo

# ... Agregar más pruebas según sea necesario
