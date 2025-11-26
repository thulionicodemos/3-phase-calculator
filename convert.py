"""
Module: convert
Author: Thulio Henrique
Description:
    Provides utility functions for converting complex numbers between
    rectangular (a + jb) and polar (r∠θ) representations. These conversions
    are fundamental in electrical engineering, especially in three-phase
    analysis, where complex phasors represent voltages, currents, and
    impedances.

Functions:
    polar_to_rect(r, angulo):
        Converts a complex number from polar form (magnitude and angle in
        degrees) to rectangular form using Euler's identity:
            z = r * (cos θ + j sin θ) = r * e^(jθ)

    rect_to_polar(Z):
        Converts a complex number from rectangular form to polar form,
        returning:
            - magnitude r = |Z|
            - angle θ in degrees using numpy.angle()

Parameters:
    r (float):
        Magnitude of the complex number in polar form.

    angulo (float):
        Angle of the complex number in degrees.

    Z (complex):
        Complex number in rectangular representation.

Returns:
    polar_to_rect → complex:
        The complex number in rectangular coordinates.

    rect_to_polar → tuple(float, float):
        (magnitude, angle_in_degrees)

Usage Example:
    from convert import polar_to_rect, rect_to_polar

    z = polar_to_rect(10, 30)   # 10∠30° → rectangular
    r, ang = rect_to_polar(z)   # back to polar form

Notes:
    - Internally uses NumPy for trigonometric and complex-number operations.
    - Angles are handled strictly in degrees for compatibility with the
      rest of the project.
"""

import numpy as np


# Converte um número na forma polar para forma retângular
def polar_to_rect(r, angulo):

    theta = np.deg2rad(angulo)
    # A linha abaixo utiliza a fórmula de Euler -> e^jθ = cosθ + jsenθ e multiplica pelo raio que retorna o numero complexo na forma retângular
    z = r * np.exp(1j * theta)

    return z


# Converte um número na forma retângular para forma polar
def rect_to_polar(Z):

    r = np.abs(Z)
    # Retorna o ângulo do número complexo e converte para graus
    angulo = np.angle(Z, deg=True)

    return r, angulo