def consultar_clientes(cursor):
    """Consulta todos los clientes en la base de datos."""
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    print(clientes)
    print("✓ Consulta de clientes realizada correctamente.")

    return clientes 
