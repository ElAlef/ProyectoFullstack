from persona import Persona
from obrasocial import ObraSocial

class Paciente(Persona):
    obraSocial = []
    
    def __init__(self, contraseña, nombre, apellido, nroDNI, telefono, email, nroAfiliado, obraSocial):
        Persona.__init__(self,contraseña, nombre, apellido, nroDNI, telefono, email)
        self.NroAfiliado = nroAfiliado
        self.ObraSocial = obraSocial
    
    def get_NroAfiliado(self):
        return self.NroAfiliado

    def set_NroAfiliado(self, nroAfiliado):
        self.NroAfiliado = nroAfiliado

    def get_ObraSocial(self):
        return self.ObraSocial

    def set_ObraSocial(self, obraSocial):
        self.ObraSocial = obraSocial
    
    def __str__(self):
        return Persona.__str__(self) + "afiliado: " + self.NroAfiliado + " obra social: " + str(self.ObraSocial) + " paciente/s.\n"
    
    def añadir_obrasocial(self, os):
        if not isinstance(os, ObraSocial):
            raise Exception('añadir_obrasocial: obrasocial debe ser de la clase ObraSocial')

        if os in self.ObraSocial : 
            indice = self.ObraSocial.index(os)
        else: 
            self.ObraSocial.append(os)
    
    def mostrar_obrasocial(self):
        for os in self.ObraSocial:
           print(os)  
        

#paciente1 = Paciente("123", 'juan', 'perez', "33222111", "322545", 'vdvd@nfnf', "1", [])
#print(paciente1)
#os1 = ObraSocial("APROSS", "FAMILIAR")
#paciente1.añadir_obrasocial(os1)
#print(paciente1)
#paciente1.mostrar_obrasocial()