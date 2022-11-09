import Paciente
class ReservaDeTurno :
    paciente = Paciente()
    def __init__(self, paciente, fecha, hora, id_reserva):
        self.Paciente = paciente
        self.Fecha = fecha
        self.Hora = hora
        self.Id_Reserva = id_reserva
    
    def get_Paciente(self):
        return self.Paciente

    def set_Paciente(self, paciente):
        self.Paciente= paciente

    def get_Fecha(self):
        return self.Fecha

    def set_Fecha(self, fecha):
        self.Fecha = fecha

    def get_Hora(self):
        return self.Hora

    def set_Hora(self, hora):
        self.Hora = hora
    
    def get_Id_Reserva(self):
        return self.Id_Reserva

    def set_Id_Reserva(self, id_reserva):
        self.Id_Reserva = id_reserva
        