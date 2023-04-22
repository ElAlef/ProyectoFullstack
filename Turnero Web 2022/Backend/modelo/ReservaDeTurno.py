from paciente import Paciente
from obrasocial import ObraSocial
from turnosPorEspecialista import TurnosPorEspecialista
from especialista import Especialista
from HorarioDeAtencion import HorarioDeAtencion

class ReservaDeTurno():
    TurnoPorEspecialista = []
    paciente = []
    
    def __init__(self, paciente =[], turnoPorEspecialista = []):
        #self.id_reserva = id(ReservaDeTurno())
        #self.Fecha = fecha
        #self.Hora = hora
        self.Paciente = paciente
        self.TurnoPorEspecialista = turnoPorEspecialista
    
    #def get_id_reserva(self):
     #   return self.id_reserva

    #def set_id_reserva(self):
     #   self.id_reserva = id(ReservaDeTurno())

    # def get_Fecha(self):
    #     return self.Fecha

    # def set_Fecha(self, fecha):
    #     self.Fecha = fecha
    
    # def get_Hora(self):
    #     return self.Hora

    # def set_Hora(self, hora):
    #     self.Hora = hora
    
    def get_Paciente(self):
        return self.Paciente

    def set_Paciente(self, paciente):
        self.Paciente = paciente
    
    def get_TurnoPorEspecialista(self):
        return self.TurnoPorEspecialista

    def set_TurnoPorEspecialista(self, turnoPorEspecialista):
        self.TurnoPorEspecialista = turnoPorEspecialista
    
    def añadir_turnoPorEspecialista(self, tue):
        if not isinstance(tue, TurnosPorEspecialista):
            raise Exception('añadir_turnoPorEspecialista: turnoPorEspecialista debe ser de la clase TurnosPorEspecialista')

        if tue in self.TurnoPorEspecialista : 
            indice = self.TurnoPorEspecialista.index(tue)
        else: 
            self.TurnoPorEspecialista.append(tue)
    
    def mostrar_turnoPorEspecialista(self):
        for tue in self.TurnoPorEspecialista:
           print(tue)
    
    def añadir_paciente(self, p):
        if not isinstance(p, Paciente):
            raise Exception('añadir_paciente: paciente debe ser de la clase paciente')

        if p in self.Paciente : 
            indice = self.Paciente.index(p)
        else: 
            self.Paciente.append(p)
    
    def mostrar_paciente(self):
        for p in self.Paciente:
           print(p)
    
    def __str__(self):
        return "reserva de turno fecha " + str(self.TurnoPorEspecialista) + "paciente: " + str(self.Paciente) + "\n"
        
try:
    h3 = HorarioDeAtencion("lunes", "8", "12")
    especialista3 = Especialista("5695", 'nora', 'lopez', "33222121", "332545", 'vdvd@nfnf', 'pediatra', [])
    turno3 = TurnosPorEspecialista("01/01/2022", '8:30', '9')
    especialista3.añadir_horario(h3)
    h3.añadir_turno(turno3)
    #print(h3)
    #h3.mostrar_turnos()
    paciente3 = Paciente("123", 'juan', 'perez', "33222111", "322545", 'vdvd@nfnf', "1", [])
    os3 = ObraSocial("APROSS", "FAMILIAR")
    paciente3.añadir_obrasocial(os3)
    #print(paciente3)
    #paciente3.mostrar_obrasocial()
    reserva3 = ReservaDeTurno([], [])
    reserva3.añadir_paciente(paciente3)
    reserva3.añadir_turnoPorEspecialista(turno3)
    print(reserva3)
    reserva3.mostrar_paciente()
    reserva3.mostrar_turnoPorEspecialista()

except Exception as e:
    print(e)