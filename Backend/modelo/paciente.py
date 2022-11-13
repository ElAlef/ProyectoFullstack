from persona import Persona
from ObraSocial import ObraSocial


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
        

    def ingresarPaciente(self,idPaciente, nombre, apellido, DNI, nroAfiliado, telefono, email, Administrador_id_Administrador):
        import mysql.connector

        try:
            connection = mysql.connector.connect(host='localhost',
                                         database='turnero',
                                         user='vero',
                                         password='aguila13')

            mySql_insert_query = "INSERT INTO paciente (idPaciente, nombre, apellido, DNI, nroAfiliado, telefono, email, Administrador_id_Administrador) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "
            data = (idPaciente, nombre, apellido, DNI, nroAfiliado, telefono, email, Administrador_id_Administrador)

            cursor = connection.cursor()
            cursor.execute(mySql_insert_query, data)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into paciente table")
            cursor.close()

        except mysql.connector.Error as error:
          print("Failed to insert record into Laptop table {}".format(error))

        finally:
                if connection.is_connected():
                  connection.close()
                  print("MySQL connection is closed")

#CREATE si funciona:       
# try:
#      paciente1= Paciente("123", 'juan', 'perez', "33222111", "322545", 'vdvd@nfnf', "1", [])
#      paciente1.ingresarPaciente(456, 'juan', 'perez', 30222111, 10, 302545, 'vdvd@nfnf', 1)
# except Exception as e:
#         print(e)
    
    def modificarPaciente(self):
        import mysql.connector

        try:
            connection = mysql.connector.connect(host='localhost',
                                         database='turnero',
                                         user='vero',
                                         password='aguila13')

            mySql_insert_query = "UPDATE paciente SET nombre='pedro' WHERE nombre='juan'" 
    

            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            connection.commit()
            print(cursor.rowcount, "CAMBIO EXITOSO")
            cursor.close()

        except mysql.connector.Error as error:
          print("Failed to insert record into Laptop table {}".format(error))

        finally:
                if connection.is_connected():
                  connection.close()
                  print("MySQL connection is closed")

    def verPacientes(self):
        import mysql.connector

        try:
            connection = mysql.connector.connect(host='localhost',
                                         database='turnero',
                                         user='vero',
                                         password='aguila13')

            mySql_insert_query = "SELECT * from paciente "
            

            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            #resultadoREAD = cursor.fetchall()
            #return resultadoREAD
            rows=cursor.fetchall()
            for row in rows:
             print(row)

            cursor.close()
            

        except mysql.connector.Error as error:
          print("Failed to insert record into Laptop table {}".format(error))

        finally:
                if connection.is_connected():
                  connection.close()
                  print("MySQL connection is closed")


    def eliminarPaciente(self):
        import mysql.connector

        try:
            connection = mysql.connector.connect(host='localhost',
                                         database='turnero',
                                         user='vero',
                                         password='aguila13')

            mySql_insert_query = "DELETE FROM paciente WHERE idPaciente = '456' "
        

            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            connection.commit()
            print(cursor.rowcount, "Record deleted successfully into paciente table")
            cursor.close()

        except mysql.connector.Error as error:
          print("Failed to insert record into Laptop table {}".format(error))

        finally:
                if connection.is_connected():
                  connection.close()
                  print("MySQL connection is closed")
# DELETE si funciona:       
# #try:
#     paciente1= Paciente("123", 'juan', 'perez', "33222111", "322545", 'vdvd@nfnf', "1", [])
#     paciente1.eliminarPaciente()
# except Exception as e:
#         print(e)
#READ SI FUNCIONA:
#try:
#       paciente1= Paciente("123", 'juan', 'perez', "33222111", "322545", 'vdvd@nfnf', "1", [])
#       paciente1.verPacientes()
# except Exception as e:
#          print(e)
#UPDATE si funciona:
#try:
#       paciente1= Paciente("123", 'juan', 'perez', "33222111", "322545", 'vdvd@nfnf', "1", [])
#       paciente1.modificarPaciente()
# except Exception as e:
#          print(e)
        