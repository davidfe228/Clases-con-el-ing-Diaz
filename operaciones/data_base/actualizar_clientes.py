def actualizar_clientes(cursor, cliente_nombre,  nueva_cedula ):
    """Actualiza los datos de un cliente en la base de datos."""    
    cursor.execute(
        "UPDATE clientes SET  cedula = ? WHERE nombre = ?",
        ( nueva_cedula, cliente_nombre)
    )
    print(f"✓ Cliente con nombre {cliente_nombre} actualizado correctamente.")
    
    return cursor.rowcount