import Especialista
class Administrador:
    especialista = Especialista()
    
    def __init__(self, contraseña, nombre, apellido, nroDNI, cargo, telefono, email, especialista):
        self.Contraseña = contraseña
        self.Nombre = nombre
        self.Apellido = apellido
        self.NroDNI = nroDNI
        self.Cargo = cargo
        self.Telefono = telefono
        self.Email = email
        self.Especialista = especialista

    def get_Contraseña(self):
        return self.Contraseña

    def set_Contraseña(self, contraseña):
        self.Contraseña= contraseña

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

    def get_Cargo(self):
        return self.Cargo

    def set_Cargo(self, cargo):
        self.Cargo = cargo
    
    def get_Telefono(self):
        return self.Telefono

    def set_Telefono(self, telefono):
        self.Telefono = telefono

    def get_Email(self):
        return self.Email

    def set_Email(self, email):
        self.Email = email
    
    def get_Especialista(self):
        return self.Especialista

    def set_Especialista(self, especialista):
        self.Especialista = especialista
    
    def ingresar_especialista(self, especialista):
        if not isinstance(especialista, Especialista):
            raise Exception('ingresar_especialista: especialista debe ser de la clase Especialista')
        if especialista in self.especialistas:
            indice = self.especialistas.index(especialista)
        else:
            self.especialistas.append(especialista)
