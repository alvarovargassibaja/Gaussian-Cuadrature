"""Cálculo de integrales por el método de Cuadratura Gaussiana.

Este módulo permite al usuario realizar una aproximación de integrales mediante el método de Cuadratura Gaussiana.

Este módulo contiene las siguientes funciones:

-`gaussxw(N)` - Retorna una tupla con los valores de los puntos de colocación y los pesos.
-`gaussxwab(a, b, x, w)` - Retorna los puntos de colocación y los pesos escalados al intervalo de integración de interés.
-`legendre(x)` - Retorna la evaluación de la integral para cada punto de colocación.
"""

import numpy as np

def gaussxw(N):
  """Cálculo de puntos de colocación y pesos utilizando el método de cuadratura Gaussiana.
  
  Examples:
    >>> gaussxw(2)
    (array([0.57735027, 0.57735027]), array([1., 1.]))

  Args:
    N (int): Número de divisiones.

  Returns:
    (float): Retorna una tupla con los puntos de colocación y pesos.

  """
  a = np.linspace(3, 4 * (N - 1), N) / ((4 * N) + 2)
  x = np.cos(np.pi * a + 1 / (8 * N * N * np.tan(a)))

  epsilon = 1e-15
  delta = 1.0
  while delta > epsilon:
    p0 = np.ones(N, dtype = float)
    p1 = np.copy(x)
    for k in range(1, N):
      p0, p1 = p1, ((2 * k + 1) * x * p1 - k * p0) / (k + 1)
      dp = (N + 1) * (p0 - x * p1) / (1 - x * x)
      dx = p1 / dp
      x -= dx
      delta = np.max(np.abs(dx))

  w = 2 * (N + 1) * (N + 1)/(N * N * (1 - x * x) * dp * dp)
  return x,w

#Escalado del intervalo.
def gaussxwab(a, b, x, w):
  """Escalado de los puntos de colocación y los pesos.
  
  Examples:
    >>> gaussxwab(1, 3, xw_N2[0], xw_N2[1])
    (array([2.57735027, 2.57735027]), array([1., 1.]))

  Args:
    a (int): Límite de integración inferior.
    b (int): Límite de integración superior.
    x (float): Arreglo de datos con los puntos de colocación.
    w (float): Arreglo de datos con los pesos.

  Returns:
    (float): Retorna los puntos de colocación y los pesos escalados.

  """
  return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

#Función que contiene la expresión a evaluar.
def legendre(x):
  """Expresión de evaluación por cuadratura Gaussiana.

  Examples:
    >>> legendre(

  Args:
    x (float): Arreglo de datos con los puntos de colocación.

  Returns:
    (float): Retorna la evaluación de la epresión para cierto punto de colocación.

  """
  return x**6 - x**2 * np.sin(2 * x)

#Se calculan los "x" y "w" para cada valor de N.
#Caso para $N=2$
"""
xw_N2 = gaussxw(2)

#Luego para $N=3$
xw_N3 = gaussxw(3)

#Y finalmente para $N=4$
xw_N4 = gaussxw(4)
"""
#Caso adicional para $N=7$
xw_N7 = gaussxw(7)

# Se calcula el escalado del intervalo de evaluación con los datos de "x" y "w" obtenidos anteriormente.
#El resultado de "x" y "w" son tuplas. Las expresiones xw_NX[0] y xw_NX[1] representan los valores de los puntos de locación ("x") y pesos ("w"), respectivamente.
"""
ab_N2 = gaussxwab(1, 3, xw_N2[0], xw_N2[1])

ab_N3 = gaussxwab(1, 3, xw_N3[0], xw_N3[1])

ab_N4 = gaussxwab(1, 3, xw_N4[0], xw_N4[1])
"""
ab_N7 = gaussxwab(1, 3, xw_N7[0], xw_N7[1])

# Aplicando la ecuación de Newton - Cotes.
# Las expresiones ab_NX[0] y ab_NX[1] representan los valores de los puntos de locación ("x") y pesos ("w") escalados, respectivamente.
"""
sum_N2 = np.sum(ab_N2[1] * legendre(ab_N2[0]))
print(sum_N2)

sum_N3 = np.sum(ab_N3[1] * legendre(ab_N3[0]))
print(sum_N3)

sum_N4 = np.sum(ab_N4[1] * legendre(ab_N4[0]))
print(sum_N4)
"""
sum_N7 = np.sum(ab_N7[1] * legendre(ab_N7[0]))
print(sum_N7)
