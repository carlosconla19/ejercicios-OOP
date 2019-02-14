class Fecha():
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    def get_info(self):
        fecha = (self.dia, "/",self.mes, "/", self.año)
        return fecha

    def get_comprobar(self):
        if (1 <= self.dia <= 31) and (1 <= self.mes <= 12) and (self.año >= 0):
            return "Fecha correcta"
        else:
            return "Fecha incorrecta"

    def get_dia(self):
        dia_mas = self.dia +1

        if dia_mas > 31:
            mes_mas = self.mes +1
            if mes_mas > 12:
                return (1, "/", 1, "/", self.año +1 )
            else:
                return (1, "/", mes_mas, "/", self.año)
        else:
            return (dia_mas, "/", self.mes, "/", self.año)





hoy  = Fecha(31,12,2020)
print(hoy.get_dia())
