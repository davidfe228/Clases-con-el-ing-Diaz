import sqlite3


def conectar_base_datos(nombre_bd="datos.db"):
    """Crea una conexión a la base de datos SQLite."""
    try:
        conexion = sqlite3.connect(nombre_bd)
        cursor = conexion.cursor()
        print(f"✓ Conexión establecida a {nombre_bd}")
        return conexion, cursor
    except sqlite3.Error as error:
        print(f"✗ Error al conectar: {error}")
        return None, None