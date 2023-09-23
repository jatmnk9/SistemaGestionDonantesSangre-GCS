import sqlite3 as sql
import os
from modelo.Credencial import Credencial
from modelo.OperacionDonante import OperacionDonante
from modelo.OperacionCredencial import OperacionCredencial
from modelo.OperacionCita import OperacionCita

def conectar_bd():  
    # Establecer conexión con la base de datos
    conn = sql.connect("SGDS-VABD01.db")
    return conn

def eliminar_usuario(id):
    conn = sql.connect("modelo/SGDS-VABD01.db")
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM Credencial WHERE idCredencial = ?", (id,))
        conn.commit()
    except sql.Error as e:
        print("Error al eliminar datos de la tabla Credencial:", str(e))
        conn.rollback()
        conn.close()
        return False

    try:
        cursor.execute("DELETE FROM Donante WHERE idDonante = ?", (id,))
        conn.commit()
    except sql.Error as e:
        print("Error al eliminar datos de la tabla Donante:", str(e))
        conn.rollback()
        conn.close()
        return False

    try:
        cursor.execute("DELETE FROM Cita WHERE idDonante = ?", (id,))
        conn.commit()
    except sql.Error as e:
        print("Error al eliminar datos de la tabla Cita:", str(e))
        conn.rollback()
        conn.close()
        return False

    conn.close()
    return True

def buscar_usuario(user, password):
    conn = sql.connect("modelo/SGDS-VABD01.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT * FROM Credencial WHERE user = ? AND password = ?",
            (user, password),
        )

        usuario = cursor.fetchone()

        return usuario
    except sql.Error as e:
        print("Error al buscar usuario:", str(e))

    return None

def usuarioDatos(nombre):
    conn = sql.connect("modelo/SGDS-VABD01.db")    
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT dni, telefono, direccion, fechaNacimiento FROM Paciente WHERE nombre = ?",
            (nombre,),
        )

        usuario = cursor.fetchone()

        return usuario
    except sql.Error as e:
        print("Error al buscar usuario:", str(e))

    return None

def usuarioDonaciones(nombre):
    conn = sql.connect("modelo/SGDS-VABD01.db")    
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT ultimaDonacion FROM Paciente WHERE nombre = ?",
            (nombre,),
        )

        usuario = cursor.fetchone()

        return usuario
    except sql.Error as e:
        print("Error al buscar usuario:", str(e))

    return None

def usuarioBeneficios(nombre):
    conn = sql.connect("modelo/SGDS-VABD01.db")    
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT beneficioActivo FROM Paciente WHERE nombre = ?",
            (nombre,),
        )

        usuario = cursor.fetchone()

        return usuario
    except sql.Error as e:
        print("Error al buscar usuario:", str(e))

    return None

def registrar_credencial(credencial):
    conn = conectar_bd()
    cursor = conn.cursor()
    instruccion = "INSERT INTO Credencial VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(instruccion, (
        credencial.get_idCredencial(),
        credencial.get_fechaDeCreacion(),
        credencial.get_fechaDeExpiracion(),
        credencial.get_estado(),
        credencial.get_tipoDeUsuario(),
        credencial.get_username(),
        credencial.get_password()
    ))
    conn.commit()
    conn.close()


def registrar_donante(donante):
    conn = conectar_bd()
    cursor = conn.cursor()

    try:
        instruccion = "INSERT INTO Donante VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(
            instruccion,
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


def buscar_donante(dni):
    conn = sql.connect("modelo/SGDS-VABD01.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT idDonante FROM Donante WHERE dni = ?",
            (dni),
        )

        resultado = cursor.fetchone()

        if resultado:
            id_donante = resultado[0]
            return id_donante
    except sql.Error as e:
        print("Error al buscar usuario:", str(e))

    return None


def buscar_hospital(hospital):
    conn = sql.connect("modelo/SGDS-VABD01.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT idHospital FROM Hospital WHERE nombreDeHospital = ?",
            (hospital),
        )

        resultado = cursor.fetchone()

        if resultado:
            id_hospital = resultado[0]
            return id_hospital
    except sql.Error as e:
        print("Error al buscar usuario:", str(e))

    return None

def registrar_cita(cita):
    conn = conectar_bd()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO Cita (idCita, fecha, idDonante, idHospital, estado) VALUES (?, ?, ?, ?, ?)",
            (cita.idCita, cita.fecha, cita.idDonante, cita.idHospital, cita.estado),
        )

        conn.commit()
        print("Cita registrada exitosamente.")
    except sql.Error as e:
        print("Error al registrar la cita:", str(e))

    conn.close()
