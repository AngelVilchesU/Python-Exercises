"""
Ejercicio: Conectar en una bd mysql, hacer una consulta y mostrar info por consola
"""

import mysql.connector
# Variables
class Conexion:
    def conectar(self):
        con = mysql.connector.connect(
            host = 'localhost',
            user= 'root',
            password= 'mysql',
            database = 'sakila'
        )
        return con

class Actor(Conexion):
    def consultaActor(self):
        con = self.conectar()
        sql = "SELECT first_name FROM actor;"
        cursor = con.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        cursor.close()
        con.close()
        return registros

    def imprimir(self):
        datos = self.consultaActor()
        for fila in datos:
            print(fila)
consulta = Actor()

# Proceso
consulta.imprimir()

# Resultado


# ¿Cómo mejorar la lógica?

