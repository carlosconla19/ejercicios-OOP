class Libro():
    def __init__(self, prestamo, devolucion, info):
        self.prestamo = prestamo
        self.devolucion = devolucion
        self.info = info
    def get_prestamo(self):
        return self.prestamo
    def get_devolucion(self):
        return self.devolucion
    def get_info(self):
        return self.info
blancanieves = Libro()
