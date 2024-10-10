# Sistema de Gestión de Encuestas

## Descripción
Este proyecto es un **Sistema de Gestión de Encuestas** desarrollado en Python, cuyo objetivo es facilitar la creación, gestión y análisis de encuestas para diferentes estudios, como la satisfacción de clientes, percepción de empleados sobre el ambiente laboral, y efectividad de campañas de marketing. El sistema se ejecuta desde la línea de comandos (CLI) utilizando **Git Bash** y la librería **Rich** para mejorar la visualización de datos en terminal.

## Características
- Creación de encuestas personalizables con preguntas y opciones predefinidas.
- Carga de participantes mediante archivos CSV con soporte para segmentación (edad, género, ubicación, etc.).
- Generación automática de informes de resultados, incluyendo estadísticas y tasas de respuesta.
- Almacenamiento de datos crudos de respuestas para análisis posterior.

## Información del Proyecto
- **Estudiante**: Jean Carlo Gomez Ortiz
- **Profesor**: Diego Fernando Marin
- **Curso**: Lenguaje de Programación Avanzada 1

## Instalación

1. **Clonar el repositorio**:
    Git Bash
   git clone https://github.com/JeanCarlogomez/Taller-3v1.git

2. **Crear y activar un entorno virtual**: 
    py -m venv venv
    source venv\scripts\activate

3. **Instalar las dependencias listadas en requirements.txt:**: 
    pip install -r requirements.md

## Requerimientos del Sistema
    Python 3.x
    Librerías: Rich (y otras que estén listadas en requirements.txt).

# Funcionamiento del Código
**Creación de Encuestas:**

La clase Encuesta permite crear nuevas encuestas con un título y una fecha de creación. Las encuestas pueden tener múltiples preguntas.
Manejo de Preguntas:

La clase Pregunta representa cada pregunta de la encuesta. Las preguntas pueden ser de diferentes tipos (ej. selección múltiple, texto).
Carga de Participantes:

El método cargar_participantes en la clase Encuesta permite cargar datos de participantes desde un archivo CSV. Cada participante se crea como una instancia de la clase Participante.
Gestión de Grupos:

La clase Grupo permite crear grupos de participantes basados en criterios específicos. Un grupo puede asignarse a una encuesta.
Registro de Respuestas:

Las respuestas de los participantes se pueden registrar, aunque esta funcionalidad se puede expandir en futuras versiones.
Generación de Informes:

La clase Informe genera un informe que incluye estadísticas de respuesta y resultados de la encuesta.
Ejecutar el Sistema:

Al ejecutar el archivo main.py, se crea una encuesta, se agregan preguntas, se carga un archivo CSV de participantes y se genera un informe.