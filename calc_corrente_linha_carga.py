"""
Module: calc_corrente_linha_carga
Author: Thulio Henrique
Description:
    Provides functions to compute line currents in a Δ-connected (Delta) load
    for a three-phase power system. In a Delta configuration, line currents
    differ from branch (phase) currents because each line carries the algebraic
    sum of two phase currents.

    This module imports the phase-current functions from calc_corrente and uses
    them to compute the line currents Ia, Ib, and Ic based on the relationships:

        Ia = I_ab − I_ca
        Ib = I_bc − I_ab
        Ic = I_ca − I_bc

    These expressions apply to both balanced and unbalanced Delta loads.

Functions:
    correnteLinhaA(circuito):
        Computes the line current in phase A.

    correnteLinhaB(circuito):
        Computes the line current in phase B.

    correnteLinhaC(circuito):
        Computes the line current in phase C.

Parameters:
    circuito (Circuito):
        An instance containing all source voltages, impedances, and system
        configuration required to compute the phase currents:
            - Phase source voltages (va, vb, vc)
            - Load impedances (za_carga, zb_carga, zc_carga)
            - Line impedances (za_linha, zb_linha, zc_linha)
            - Number of wires (3 or 4)
            - Neutral data (if applicable)

Returns:
    complex:
        The line current for each respective phase, expressed as:
            Ia = Iab − Ica
            Ib = Ibc − Iab
            Ic = Ica − Ibc

        Each output is a complex number representing magnitude and angle.

Usage Example:
    from calc_corrente_linha_carga import correnteLinhaA
    Ia = correnteLinhaA(circuito)

Notes:
    - Line currents are different from phase currents in Delta circuits.
    - For Y-connected line currents, use the phase-current functions from
      calc_corrente directly.
    - For power calculations, use calc_potencia.
"""

from calc_corrente import correnteFaseA as correnteFaseAB, correnteFaseB as correnteFaseBC, correnteFaseC as correnteFaseCA


# Funções que calculam a corrente de linha em um circuito triângulo
def correnteLinhaA(circuito):
    return correnteFaseAB(circuito) - correnteFaseCA(circuito)


def correnteLinhaB(circuito):
    return correnteFaseBC(circuito) - correnteFaseAB(circuito)


def correnteLinhaC(circuito):
    return correnteFaseCA(circuito) - correnteFaseBC(circuito)
