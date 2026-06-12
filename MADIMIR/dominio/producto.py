class Producto:

    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar(self):
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria
        }