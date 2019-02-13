class Alumno():
    def __init__(self,nombre,  numero_matricula, not1, not2, not3):
        self.nombre = nombre
        self.numero_matricula = numero_matricula
        self.not1 = not1
        self.not2 = not2
        self.not3 = not3
        self.media = not1 + not2 + not3

    def evaluacion(self):


        if (self.media / 3) >= 4.8:
                   return self.nombre, self.numero_matricula, "Aprobado"
        else:
            return ("suspenso")
