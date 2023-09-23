import sqlite3 as sql
import os
from modelo.Sistema import Sistema



class OperacionDonante:
    def __init__(self):
        pass
    
    syst = Sistema("Activo")
    
    def registrar_donante(donante):
        conn = sql.connect("modelo/SGDS-VABD01.db")
        cursor = conn.cursor()

        try:
            instruction = "INSERT INTO Donante VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(
                instruction,
                (
                    donante.get_id_donante(),
                    donante.get_nombre(),
                    donante.get_fecha_nacimiento(),
                    donante.get_dni(),
                    donante.get_telefono(),
                    donante.get_direccion(),
                    donante.get_beneficio_activo(),
                    donante.get_grupo_sanguineo(),
                    donante.get_rh(),
                    donante.get_ultima_donacion(),
                    donante.get_id_hospitalUltimo(),
                ),
            )

            conn.commit()
            print("Donante registrado exitosamente.")
        except sql.Error as e:
            print("Error al registrar el donante:", str(e))

        conn.close()

    def buscar_donantes(self, donante, sistema):
        conn = sql.connect("modelo/SGDS-VABD01.db")
        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT * FROM Donante WHERE grupo_sanguineo = ? AND direccion LIKE ?",
                (donante.get_grupo_sanguineo(), f"%{donante.get_direccion()}%"),
            )

            donantes = cursor.fetchall()

            return donantes
        except sql.Error as e:
            print("Error al buscar donantes:", str(e))

        conn.close()
        return []

    def cambiar_datos(self, donante, sistema):
        conn = sql.connect("modelo/SGDS-VABD01.db")
        cursor = conn.cursor()
        try:
            cursor.execute(
                "UPDATE Donante SET nombre = ?, fecha_nacimiento = ?, dni = ?, telefono = ?, "
                "direccion = ? WHERE idDonante = ?",
                (
                    donante.get_nombre(),
                    donante.get_fecha_nacimiento(),
                    donante.get_dni(),
                    donante.get_telefono(),
                    donante.get_direccion(),
                    donante.get_id_donante()
                ),
            )

            conn.commit()
            print("Datos actualizados exitosamente.")
        except sql.Error as e:
            print("Error al actualizar los datos:", str(e))

        conn.close()

    def eliminar_donante(id):
        conn = sql.connect("modelo/SGDS-VABD01.db")
        cursor = conn.cursor()
        instruction = "DELETE FROM Donante where idDonante= ?"
        cursor.execute(instruction, (id,))
        conn.commit()
        conn.close()


    def ver_donantes(self, sistema):
        conn = sql.connect("modelo/SGDS-VABD01.db")
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM Donante")

            donantes = cursor.fetchall()

            if donantes:
                for donante in donantes:
                    print(f"ID: {donante[0]}, Nombre: {donante[1]}, Grupo Sanguíneo: {donante[7]}, RH: {donante[8]}")
            else:
                print("No se encontraron donantes en la base de datos.")
        except sql.Error as e:
            print("Error al obtener los donantes:", str(e))

        conn.close()
