class Participante:
    def __init__(self, nombre: str, correo: str, edad: int, genero: str, ubicacion: str = ""):
        self.nombre = nombre
        self.correo = correo
        self.edad = edad
        self.genero = genero
        self.ubicacion = ubicacion
