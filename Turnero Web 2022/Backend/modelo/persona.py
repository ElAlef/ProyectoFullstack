class Persona:
    
    def __init__(self,contraseña, nombre, apellido, nroDNI, telefono, email):
        self.Contraseña = contraseña
        self.Nombre = nombre
        self.Apellido = apellido
        self.NroDNI = nroDNI
        self.Telefono = telefono
        self.Email = email

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
    
    def get_Telefono(self):
        return self.Telefono

    def set_Telefono(self, telefono):
        self.Telefono = telefono

    def get_Email(self):
        return self.Email

    def set_Email(self, email):
        self.Email = email

    def __str__(self):
        return "contraseña o matricula: " + self.Contraseña + " nombre: " + self.Nombre + " apellido: " + self.Apellido + " dni: " + self.NroDNI + " telefono: " + self.Telefono + " email: " + self.Email + "m.\n"

