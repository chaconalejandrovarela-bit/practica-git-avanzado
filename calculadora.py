# ============================================
# CALCULADORA - Funciones adicionales
# Agreguen estas funciones a su calculadora.py,
# una por una, con su propio commit para cada una
# ============================================

# Calculadora

def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b


def potenciar(a, b):
    return a ** b


def factorial(n):
    if n < 0:
        return "Error: el factorial no existe para números negativos"

    resultado = 1

    for i in range(1, n + 1):
        resultado *= i

    return resultado

def potencia(base, exponente):
    return base ** exponente
