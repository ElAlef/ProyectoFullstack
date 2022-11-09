import Especialista
class HorarioEspecialista(Especialista):
    def __init__(self, diaSemana, horaInicio, horaFin):
        self.DiaSemana = diaSemana
        self.HoraInicio = horaInicio
        self.HoraFin = horaFin

    def get_DiaSemana(self):
        return self.DiaSemana

    def set_DiaSemana(self, diaSemana):
        self.DiaSemana = diaSemana

    def get_HoraInicio(self):
        return self.HoraInicio

    def set_HoraInicio(self, horaInicio):
        self.HoraInicio = horaInicio

    def get_HoraFin(self):
        return self.HoraFin

    def set_HoraFin(self, horaFin):
        self.HoraFin = horaFin

