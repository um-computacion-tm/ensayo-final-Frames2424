class Dispositivo:
    def __init__(self, id = None, nombre = None, marca = None, tipo = None, diccionario = None):
        self.id = id
        self.nombre = nombre
        self.marca = marca
        self.tipo = tipo

        if diccionario:
            self.id = diccionario.get("id")
            self.nombre = diccionario.get("nombre")
            self.marca = diccionario.get("marca")
            self.tipo = diccionario.get("tipo")
            