import HorarioEspecialista
import TurnoPorEspecialista
class Especialista:
    horarioDeAtencion = HorarioEspecialista()
    turnos = TurnoPorEspecialista()
    
    def __init__(self, nombre, apellido, nroDNI, nroMatricula, especialidad, telefono, email, horarioDeAtencion, turnos):
        self.Nombre = nombre
        self.Apellido = apellido
        self.NroDNI = nroDNI
        self.NroMatricula = nroMatricula
        self.Especialidad = especialidad
        self.Telefono = telefono
        self.Email = email
        self.HorarioDeAtencion = horarioDeAtencion
        self.Turnos = turnos

    def get_Nombre(self):
        return self.Nombre

    def set_Nombre(self, nombre):
        self.Nombre = nombre

    def get_Apellido(self):
        return self.Apellido

    def set_Apellido(self, apellido):
        self.Apellido = apellido

    def get_NroDNI(self):
        return self.NroDNI

    def set_NroDNI(self, nroDNI):
        self.NroDNI = nroDNI

    def get_NroMatricula(self):
        return self.NroMatricula

    def set_NroMatricula(self, nroMatricula):
        self.NroMatricula = nroMatricula

    def get_Especialidad(self):
        return self.Especialidad

    def set_Especialidad(self, especialidad):
        self.Especialidad = especialidad
    
    def get_Telefono(self):
        return self.Telefono

    def set_Telefono(self, telefono):
        self.Telefono = telefono

    def get_Email(self):
        return self.Email

    def set_Email(self, email):
        self.Email = email

    def get_HorarioDeAtencion(self):
        return self.HorarioDeAtencion

    def set_HorarioDeAtencion(self, horarioDeAtencion):
        self.HorarioDeAtencion = horarioDeAtencion

    def get_Turnos(self):
        return self.Turnos

    def set_Turnos(self, turnos):
        self.Turnos = turnos