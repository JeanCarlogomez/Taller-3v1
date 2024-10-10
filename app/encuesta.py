import pytest
from app.encuesta import Encuesta  # Clase con la primera letra en mayúsculas
from app.pregunta import Pregunta
from app.respuesta import Respuesta
from app.usuario import Usuario
from app.grupo import Grupo

# PRESENTE MUCHOS PROBLEMAS A LA HORA DE INTENTAR EJECUTAR ESTAS PRUEBAS

# Pruebas para la clase Encuesta
def test_crear_encuesta():
    e = Encuesta(titulo="Encuesta de Satisfacción", fechaCreacion="2024-10-03")
    assert e.titulo == "Encuesta de Satisfacción"

def test_agregar_pregunta():
    e = Encuesta(titulo="Encuesta de Satisfacción")
    pregunta1 = Pregunta(texto="¿Cómo calificaría el servicio?")
    pregunta2 = Pregunta(texto="¿Recomendaría el servicio?")
    pregunta3 = Pregunta(texto="¿Cómo mejoraría el servicio?")
    e.agregar_pregunta(pregunta1)
    e.agregar_pregunta(pregunta2)
    e.agregar_pregunta(pregunta3)
    assert len(e.preguntas) == 3

# Pruebas para la clase Pregunta
def test_crear_pregunta():
    p = Pregunta(texto="¿Cuál es su edad?")
    assert p.texto == "¿Cuál es su edad?"

# Pruebas para la clase Respuesta
def test_crear_respuesta():
    u = Usuario(nombre="Juan Pérez", email="juan@example.com")
    p = Pregunta(texto="¿Cómo calificaría el servicio?")
    r = Respuesta(p, u, "Excelente")
    assert r.valor == "Excelente"

# Pruebas para la clase Usuario
def test_crear_usuario():
    u = Usuario(nombre="Ana García", email="ana@example.com")
    assert u.nombre == "Ana García"

# Pruebas para la clase Grupo
def test_crear_grupo():
    g = Grupo(nombre="Clientes VIP", criterios={"edad": ">= 30"})
    assert g.nombre == "Clientes VIP"

# Pruebas para la integración entre Encuesta y Grupo
def test_encuesta_con_grupo():
    e = Encuesta(titulo="Encuesta de Satisfacción")
    g = Grupo(nombre="Clientes VIP")
    e.aplicar_a_grupo(g)
    assert e.grupo == g
