# test_triangulo.py

import pytest
from triangulo import tipo_triangulo  # Importa la función desde triangulo.py

# Pruebas por Tablas de Decisión
@pytest.mark.parametrize("a, b, c, esperado", [
    (3, 3, 3, "Equilátero"),   # CP1 - Todos los lados iguales (Triángulo equilátero válido)
    (0, 0, 0, "Error: Los lados deben ser mayores que 0"),    # CP2 - Todos los lados iguales = 0
    (-1, -1, -1, "Error: Los lados deben ser mayores que 0"),     # CP3 - Todos los lados iguales < 0
    (3.5, 3.5, 3.5, "Error: Los lados deben ser números enteros"),   # CP4 - Todos los lados iguales (Triángulo equilátero válido)
    (3, 3, 4, "Isósceles"),    # CP5 - Permutación 1 de Isósceles
    (3, 4, 3, "Isósceles"),    # CP6 - Permutación 2 de Isósceles
    (4, 3, 3, "Isósceles"),    # CP7 - Permutación 3 de Isósceles
    (6, 2, 2, "No es un triángulo"), # CP7extra - Isósceles donde a > b + c
    (2, 3, 4, "Escaleno"),  # CP8 - Triangulo escaleno valido
    (3, 2, 1, "No es un triángulo"),  # CP9.1 - Escaleno donde a = b + c
    (4, 2, 1, "No es un triángulo"),  # CP9.2 - Escaleno donde a > b + c
    (2, 3, 1, "No es un triángulo"),  # CP10.1 - Escaleno donde b = a + c
    (2, 4, 1, "No es un triángulo"),  # CP10.2 - Escaleno donde b > b + c
    (1, 2, 3, "No es un triángulo"),  # CP11.1 - Escaleno donde c = b + a
    (1, 2, 4, "No es un triángulo"),  # CP11.2 - Escaleno donde c > b + a
])
def test_tablas_decision(a, b, c, esperado):
    assert tipo_triangulo(a, b, c) == esperado

# Pruebas de Valores Límite
@pytest.mark.parametrize("a, b, c, esperado", [
    ('', 1, 1, "Error: Los lados deben ser números enteros"),  # CP 12 - a = string vacia
    (1, '@', 2, "Error: Los lados deben ser números enteros"),  # CP 13 - b = '@'
    (2, 3, 'a', "Error: Los lados deben ser números enteros"),  # CP 14 - c = 'a'
    (0, 3, 3, "Error: Los lados deben ser mayores que 0"),  # CP 15 - a = 0
    (3, 0, 3, "Error: Los lados deben ser mayores que 0"),  # CP 16 - b = 0
    (3, 3, 0, "Error: Los lados deben ser mayores que 0"),  # CP 17 - c = 0
    (4, 2, 2, "No es un triángulo"),  # CP18 -  a = b + c
    (2, 4, 2, "No es un triángulo"),  # CP19 -  b = a + c
    (2, 2, 4, "No es un triángulo"),  # CP20 -  c = a + b
    (3, 3, 3, "Equilátero"),  # CP21 -  Equilatero
    (9, 11, 11, "Isósceles"),  # CP22 -  Isósceles
    (5, 6, 7, "Escaleno"),  # CP23 -  Escaleno

    
])
def test_valores_limite(a, b, c, esperado):
    assert tipo_triangulo(a, b, c) == esperado