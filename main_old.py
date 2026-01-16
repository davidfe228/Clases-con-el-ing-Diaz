import sqlite3
from operaciones import suma, division
from operaciones.data_base.insertar_clientes import insertar_cliente
from operaciones.data_base.consulta_clientes import consultar_clientes
from operaciones.data_base.borrar_clientes import borrar_clientes
from operaciones.data_base.actualizar_clientes import actualizar_clientes    


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


def main():
    """Función principal del programa."""
    # Conectar a la base de datos SQLite
    conexion, cursor = conectar_base_datos()
    
    if conexion:
        try:
            borrar_clientes(cursor, "Cliente 8")
            conexion.commit()
            print("✓ Cambios guardados en la base de datos")
            actualizar_clientes(cursor, cliente_nombre = "Cliente 3" ,  nueva_cedula = 123456799)
            conexion.commit()
            # for i in range(1, 20):
            #     insertar_cliente(cursor, f"Cliente {i}", 1000568730 + i, 3128798760 + i, f"cliente{i}@gmail.com")
            # conexion.commit()
            # print("✓ Datos guardados en la base de datos")
            # clientes = consultar_clientes(cursor)
            # for cliente in clientes:
            #     print(cliente)  
            
        finally:
            conexion.close()
            print("✓ Conexión cerrada")

if __name__ == "__main__":
    main()
