# triangulo.py

def tipo_triangulo(a, b, c):

    # Verifica que los parametros sean enteros
    if not all(isinstance(i, int) for i in [a, b, c]):
        return "Error: Los lados deben ser números enteros"
    
    # Verifica que los parametros mayor a 0
    if any(i <= 0 for i in [a, b, c]):
        return "Error: Los lados deben ser mayores que 0"

    # Verifica si los lados forman un triángulo
    if a >= b + c or b >= a + c or c >= a + b:
        return "No es un triángulo"
    
    # Determina el tipo de triángulo
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"