"""
Module: calc_corrente
Author: Thulio Henrique
Description:
    Provides functions for computing phase currents in a Y-connected (star) 
    three-phase circuit, supporting both 3-wire (isolated neutral) and 
    4-wire (grounded/connected neutral) systems. The functions return the 
    phase currents Ia, Ib, and Ic based on line impedances, load impedances, 
    neutral impedance, and the appropriate neutral quantity (neutral current 
    or neutral displacement voltage).

    This module operates using methods from the Circuito class:
        - circuito.calcula_I_n()    → neutral current (4-wire)
        - circuito.calcula_V_nl_n() → neutral displacement voltage (3-wire)

    Depending on the system configuration:
        - For 3-wire systems, phase current includes compensation via V_nl_n.
        - For 4-wire systems, phase current includes compensation via I_n * Zn.

Functions:
    correnteFaseA(circuito):
        Computes phase current in phase A.
    correnteFaseB(circuito):
        Computes phase current in phase B.
    correnteFaseC(circuito):
        Computes phase current in phase C.

Parameters:
    circuito (Circuito):
        An instance containing:
            - Phase source voltages (va, vb, vc)
            - Line impedances (za_linha, zb_linha, zc_linha)
            - Load impedances (za_carga, zb_carga, zc_carga)
            - Neutral impedance (zn)
            - Number of wires (3 or 4)
            - Methods for neutral current/displacement voltage

Returns:
    complex or str:
        Returns the computed complex phase current. If the total impedance 
        for a phase is zero, a string message is returned indicating the 
        condition.

Computation Summary:
    Impedance per phase:
        Z_total = Z_linha + Z_carga

    - For 3-wire systems:
        Ia = Va / Z_total − V_nl_n / Z_total
    - For 4-wire systems:
        Ia = Va / Z_total − I_n * Zn / Z_total

Usage Example:
    from calc_corrente import correnteFaseA
    Ia = correnteFaseA(circuito)

Notes:
    - This module computes *phase currents* only. For line currents in 
      Δ-connected loads, use calc_corrente_linha_carga.
    - For power and voltage calculations, refer to calc_potencia and 
      calc_tensao_carga.
"""

# Funções que calculam a corrente de fase em um circuito estrela levando em consideração se a configuração é estrela aterrado ou isolado
def correnteFaseA(circuito):
    impedancia_total_a = circuito.za_linha + circuito.za_carga
    I_n = circuito.calcula_I_n()
    V_nl_n = circuito.calcula_V_nl_n()

    if impedancia_total_a == 0:
        return "Impedância total na fase A é nula"

    elif circuito.fios == 3:
        return circuito.va / impedancia_total_a - V_nl_n / impedancia_total_a
    else:
        return circuito.va / impedancia_total_a - I_n * circuito.zn / impedancia_total_a


def correnteFaseB(circuito):
    impedancia_total_b = circuito.zb_linha + circuito.zb_carga
    I_n = circuito.calcula_I_n()
    V_nl_n = circuito.calcula_V_nl_n()

    if impedancia_total_b == 0:
        return "Impedância total na fase B é nula"

    elif circuito.fios == 3:
        return circuito.vb / impedancia_total_b - V_nl_n / impedancia_total_b
    else:
        return circuito.vb / impedancia_total_b - I_n * circuito.zn / impedancia_total_b


def correnteFaseC(circuito):
    impedancia_total_c = circuito.zc_linha + circuito.zc_carga
    I_n = circuito.calcula_I_n()
    V_nl_n = circuito.calcula_V_nl_n()

    if impedancia_total_c == 0:
        return "Impedância total na fase C é nula"

    elif circuito.fios == 3:
        return circuito.vc / impedancia_total_c - V_nl_n / impedancia_total_c
    else:
        return circuito.vc / impedancia_total_c - I_n * circuito.zn / impedancia_total_c
