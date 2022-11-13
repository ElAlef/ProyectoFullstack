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