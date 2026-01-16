def borrar_clientes(cursor, cliente_nombre):
    """Borra un clientes específico de la base de datos."""
    cursor.execute("DELETE FROM clientes WHERE nombre = ?", (cliente_nombre,))
    print(f"✓ Cliente con Nombre {cliente_nombre} eliminado correctamente.")
    
    return cursor.rowcount