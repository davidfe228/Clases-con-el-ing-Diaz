def dividir(x, y):
    """Función que divide dos números y devuelve el resultado."""

    if y == 0:
        raise ValueError("No se puede dividir por cero.")

    resultado = x / y   #esta línea realiza la división de x entre y
    
    return resultado
