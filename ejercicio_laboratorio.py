class Laboratorio():
    def __init__(self, nombre, precio, componentes, porcentaje):
        self.nombre = nombre
        self.precio = precio
        self.componentes = componentes
        self.porcentaje = porcentaje
    def get_nombre(self):
        return self.nombre
    def get_precio(self):
        return self.precio
    def get_componentes(self):
        return self.componentes
    def get_porcentaje(self):
        return self.porcentaje

class Productos(Laboratorio):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.componentes= 0
        self.porcentaje = 0



class Medicamentos(Laboratorio):
    def __int__(self, nombre, precio, componentes, porcentaje):
        self.nombre = nombre
        self.precio = precio
        self.componentes = componentes
        self.porcentaje = porcentaje




lote_productos = []
dalsy = Medicamentos("Dalsy", 30, "acido....", 0.3)
lote_productos.append(dalsy)
paracetamol = Medicamentos("paracetamol", 20, "acido...", 0.2)
lote_productos.append(paracetamol)
ibuprofeno = Medicamentos("ibuprofeno", 25, "acido...", 0.2)
lote_productos.append(ibuprofeno)
pipeta = Productos("pipeta", 55.37)
lote_productos.append(pipeta)
regla = Productos("regla", 21.89)
lote_productos.append(regla)

print("El laboratorio tiene los siguientes productos: ")
for medicine in lote_productos:
    print("Tiene", medicine.get_nombre(), ", cuesta", medicine.get_precio(), "euros, contiene:", medicine.get_componentes(), "y con un porcentaje de :", medicine.get_porcentaje())







