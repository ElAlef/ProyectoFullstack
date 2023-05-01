
class TurnosPorEspecialista():

    def __init__(self, fecha, horaDesde, horaHasta):
        self.Fecha = fecha
        self.HoraDesde = horaDesde
        self.HoraHasta = horaHasta
      
    def get_Fecha(self):
        return self.Fecha

    def set_Fecha(self, fecha):
        self.Fecha = fecha

    def get_HoraDesde(self):
        return self.HoraDesde

    def set_HoraDesde(self, horaDesde):
        self.HoraDesde = horaDesde

    def get_HoraHasta(self):
        return self.HoraHasta

    def set_HoraHasta(self, horaHasta):
        self.HoraHasta = horaHasta
    
    
    def __str__(self):
        
        return ('turno:' + str(self.Fecha) + ' de ' + str(self.HoraDesde) + ' a '+ str(self.HoraHasta) + ' hs' + "\n")

