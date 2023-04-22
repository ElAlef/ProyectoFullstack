class ObraSocial():

    def __init__(self, nombre, plan):
        self.Nombre = nombre
        self.Plan = plan
      
    def get_Nombre(self):
        return self.Nombre

    def set_Nombre(self, nombre):
        self.Nombre = nombre

    def get_Plan(self):
        return self.Plan

    def set_Plan(self, plan):
        self.Plan = plan
    
    def __str__(self):
        return 'Obra Social:' + str(self.Nombre) + ' Plan: ' + str(self.Plan) + "\n"