from turnosPorEspecialista import TurnosPorEspecialista
class HorarioDeAtencion():
    turnosPorEspecialista = []

    def __init__(self, diaSemana, horaInicio, horaFin, turnosPorEspecialista=[]):
        self.DiaSemana = diaSemana
        self.HoraInicio = horaInicio
        self.HoraFin = horaFin
        self.turnosPorEspecialista = turnosPorEspecialista

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
    
    def get_turnosPorEspecialista(self):
        return self.turnosPorEspecialista

    def set_turnosPorEspecialista(self, turnosPorEspecialista):
        self.turnosPorEspecialista = turnosPorEspecialista
    
    def __str__(self):
        #return '{} ({})'.format(self.DiaSemana, self.HoraInicio, self.HoraFin)
        return ('El horario de atencion es:' + str(self.DiaSemana) + ' de ' + str(self.HoraInicio) + ' a '+ str(self.HoraFin) + ' hs' + ' turnos: ' + str(self.turnosPorEspecialista) + "\n")

    def añadir_turno(self, t):
        if not isinstance(t, TurnosPorEspecialista):
            raise Exception('añadir_turno: turno debe ser de la clase TrunoPorEspecialista')

        if t in self.turnosPorEspecialista : 
            indice = self.turnosPorEspecialista.index(t)
        else: 
            self.turnosPorEspecialista.append(t)
    
    def mostrar_turnos(self):
        for t in self.turnosPorEspecialista:
           print(t)  # Print toma por defecto str(t)

# try:
#     h1 = HorarioDeAtencion("lunes", "8", "12")
#     turno1 = TurnosPorEspecialista("01/01/2022", '8', '8:30')
#     turno2 = TurnosPorEspecialista("01/01/2022", '8:30', '9')
    
#     h1.añadir_turno(turno1)
#     h1.añadir_turno(turno2)
#     print(h1)
#     h1.mostrar_turnos()
# except Exception as e:
#     print(e)