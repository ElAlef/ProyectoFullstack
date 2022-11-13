import mysql.connector

try:
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'turnero'
    )

    if connection.is_connected():
        print("LA CONEXION FUE EXITOSA")

except:
    print("NO SE PUDO CONECTAR A LA BASE DE DATOS")

finally:
    if connection.is_connected():
        connection.close(
            print("LA CONEXION FUE CERRADA")
        )

#PRIMERA OPERACIÓN DEL CRUD: CREATE/INSERT.
def insertarValor(self):
    if self.connection.is_connected():
        try:
            cursor = self.connection.cursor()
            sentenciaSQL = "INSERT INTO especialista VALUES(%s,%s,%s)"
            data = (idEspecialista,nombre,apellido,dni,nroMatricula,especialidad,telefono,email,horarioAtencion)

            cursor.execute(sentenciaSQL,data)
            self.connection.commit()
            self.connection.close()

        except:
            print("No se pudo conectar a la base de datos")

#SEGUNDA OPERACION DEL CRUD: READ/LEER
    def BuscarObjeto(self, nombre):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL= "SELECT * from especialista where nombre like '%AL%' "
               
                cursor.execute(sentenciaSQL)
                resultadoREAD = cursor.fetchall()
                self.conexion.close()
                return resultadoREAD

            except:
                print("No se pudo concectar a la base de datos")

#CUARTA OPERACION DEL CRUD: DELETE/ELIMINAR
    def EliminarObjeto(self,ID):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE from paciente where id = idPaciente"
                
                cursor.execute(sentenciaSQL)
                self.conexion.commit()                
                self.conexion.close()
            except:
                print("No se pudo concectar a la base de datos")