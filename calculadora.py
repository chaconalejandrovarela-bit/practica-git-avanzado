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

def radicacion(a, b):
    if b == 0:
        return "Error: el índice no puede ser cero"
    if a < 0 and b % 2 == 0:
        return "Error: no existe raíz par de un número negativo"
    return a ** (1 / b)

def raiz_cuadrada(numero):
    if numero < 0:
        return "Error: no existe raiz de un numero negativo"
    return numero ** 0.5

def promedio(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)

def modulo(a, b):
    if b == 0:
        return "Error: no se puede calcular modulo con cero"
    return a % b

def valor_absoluto(numero):
    return abs(numero)
