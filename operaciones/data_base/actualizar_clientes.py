def actualizar_clientes(cursor, cliente_id, nuevo_nombre, nueva_cedula ):
    """Actualiza los datos de un cliente en la base de datos."""    
    cursor.execute(
        "UPDATE clientes SET nombre = ?, cedula = ? WHERE id = ?",
        (nuevo_nombre, nueva_cedula, cliente_id)
    )
    print(f"✓ Cliente con ID {cliente_id} actualizado correctamente.")
    
    return cursor.rowcount