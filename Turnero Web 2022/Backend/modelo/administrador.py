from persona import Persona

class Administrador(Persona):
    
    def __init__(self, contraseña, nombre, apellido, nroDNI, telefono, email, cargoAdministrativo):
        Persona.__init__(self,contraseña, nombre, apellido, nroDNI, telefono, email)
        self.CargoAdministrativo = cargoAdministrativo
    
    def get_CargoAdministrativo(self):
        return self.CargoAdministrativo

    def set_CargoAdministrativo(self, cargoAdministrativo):
        self.CargoAdministrativo = cargoAdministrativo
    
    def __str__(self):
        return Persona.__str__(self) + "cargo administrativo: " + self.CargoAdministrativo + " administrador/s.\n"
        

# administrador1 = Administrador("222", 'jose', 'lopez', "33222121", "332545", 'vdvd@nfnf', 'encargado')
# print(administrador1)
