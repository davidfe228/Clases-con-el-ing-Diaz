def insertar_cliente(cursor, nombre,cedula, telefono, email ):
    """Inserta un nuevo cliente en la base de datos."""
    cursor.execute(
        "INSERT INTO clientes (nombre, cedula, numero, correo) VALUES (?, ?, ?, ?)", (nombre, cedula, telefono, email))
    print(f"✓ Cliente {nombre} insertado correctamente.")
    
    return cursor.lastrowid

    