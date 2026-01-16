def consultar_clientes(cursor, id_cliente):
    """Consulta todos los clientes en la base de datos."""
    cursor.execute("SELECT * FROM clientes where id=?", (id_cliente,))
    clientes = cursor.fetchall()
    print(clientes)
    print("✓ Consulta de clientes realizada correctamente.")

    return clientes 
