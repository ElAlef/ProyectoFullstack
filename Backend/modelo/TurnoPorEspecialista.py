import Especialista
import ReservaDeTurno
class TurnosPorEspecialista(Especialista):
    atencion = ReservaDeTurno()
    def __init__(self, fecha, horaDesde, horaHasta, atencion):
        self.Fecha = fecha
        self.HoraDesde = horaDesde
        self.HoraHasta = horaHasta
        self.Atencion = atencion

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

    def get_Atencion(self):
        return self.Atencion

    def set_Atencion(self, atencion):
        self.Atencion = atencion