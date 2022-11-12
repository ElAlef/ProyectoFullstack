from persona import Persona
from HorarioDeAtencion import HorarioDeAtencion

class Especialista(Persona):
    horariosDeAtencion = []
    

    
    def __init__(self, contraseña, nombre, apellido, nroDNI, telefono, email, especialidad, horariosDeAtencion = []):
        Persona.__init__(self,contraseña, nombre, apellido, nroDNI, telefono, email)
        self.Especialidad = especialidad
        self.horariosDeAtencion = horariosDeAtencion #dentro de cada especialista va a haber varios horarios de atencion


    
    def get_Especialidad(self):
        return self.Especialidad

    def set_Especialidad(self, especialidad):
        self.Especialidad = especialidad
    
    def get_HorariosDeAtencion(self):
        return self.horariosDeAtencion

    def set_HorariosDeAtencion(self, horariosDeAtencion):
        self.horariosDeAtencion = horariosDeAtencion

    
    def __str__(self):
        return Persona.__str__(self) + "especialidad: " + self.Especialidad + " " + str(self.horariosDeAtencion) + "especialista/s.\n"
        
    def añadir_horario(self, h):
        if not isinstance(h, HorarioDeAtencion):
            raise Exception('añadir_horario: horario debe ser de la clase HorarioDeAtencion')

        if h in self.horariosDeAtencion : 
            indice = self.horariosDeAtencion.index(h)
        else: 
            self.horariosDeAtencion.append(h)
    
    def mostrar_horarios(self):
        for h in self.horariosDeAtencion:
           print(h)  # Print toma por defecto str(h)
# try:
#     h1 = HorarioDeAtencion("lunes", "8", "12")
#     especialista1 = Especialista("5695", 'nora', 'lopez', "33222121", "332545", 'vdvd@nfnf', 'pediatra', [])
#     #h1.DiaSemana = "lunes"
#     #h1.HoraInicio = "8"
#     #h1.HoraFin = "12"

#     #print(especialista1)
#     h2 = HorarioDeAtencion("jueves", "13", "16")
#     especialista1.añadir_horario(h2)
#     especialista1.añadir_horario(h1)
#     print(especialista1)
#     especialista1.mostrar_horarios()
    
#     #h2 = HorarioDeAtencion("martes", "9", "13")
#     #especialista1.añadir_horario(h2)
#     #print(especialista1)
# except Exception as e:
#     print(e)

