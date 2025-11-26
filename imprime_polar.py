"""
Module: imprime_polar
Author: Thulio Henrique
Description:
    Utility module for formatting complex numbers in polar notation with
    fixed two-decimal precision. This function is used throughout the
    three-phase analysis system to produce clean, human-readable phasor
    representations for voltages, currents, and impedances.

Functions:
    imprimePolar(valor_retangular):
        Converts a complex number from rectangular form to polar form using
        rect_to_polar(), formats the magnitude and angle to two decimal
        places, and returns a string representation in the form:

            magnitude |_{angle}°

Parameters:
    valor_retangular (complex):
        Complex number in rectangular form to be converted and printed.

Returns:
    str:
        A formatted string containing:
            - magnitude (r) with 2 decimal places
            - angle in degrees (θ) with 2 decimal places, followed by the ° symbol

Usage Example:
    from imprime_polar import imprimePolar
    print(imprimePolar(3 + 4j))   # 5.00 |_{53.13}°

Notes:
    - This module depends on the rect_to_polar function from the convert module.
    - The formatting style is consistent across all analysis modules to ensure
      standardized output for the Streamlit interface and CLI tools.
"""

from convert import rect_to_polar


# Recebe um valor na forma retangular e imprime na forma polar com duas casas de precisão
def imprimePolar(valor_retangular):
    magnitude, angulo = rect_to_polar(valor_retangular)
    return f"{magnitude:.2f} |_{angulo:.2f}°"
