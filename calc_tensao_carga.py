"""
Module: calc_tensao_carga
Author: Thulio Henrique
Description:
    Provides functions to compute the phase voltages at the load terminals
    in a three-phase system, specifically for Y-connected (star) loads.
    Each function multiplies the corresponding phase current by the
    respective phase load impedance (Za, Zb, Zc), applying Ohm’s Law:

        V_phase = I_phase * Z_phase

    These functions are used by circuit analysis routines to determine
    phase-to-neutral voltages at the load for both balanced and unbalanced
    configurations.

Functions:
    tensaoCargaZa(circuito):
        Computes the phase-to-neutral voltage of phase A at the load.

    tensaoCargaZb(circuito):
        Computes the phase-to-neutral voltage of phase B at the load.

    tensaoCargaZc(circuito):
        Computes the phase-to-neutral voltage of phase C at the load.

Parameters:
    circuito (Circuito):
        An instance containing:
            - Phase currents (computed via correnteFaseA/B/C)
            - Load impedances za_carga, zb_carga, zc_carga
            - System details such as source voltages and line impedances

Returns:
    complex:
        The computed phase-to-neutral load voltage for the corresponding phase.

Usage Example:
    from calc_tensao_carga import tensaoCargaZa
    Va_load = tensaoCargaZa(circuito)

Notes:
    - These functions assume a star-connected load. For line voltages in Δ
      configurations, refer to calc_tensao_linha_carga.
    - Currents are computed using utilities from calc_corrente.
"""

from calc_corrente import correnteFaseA, correnteFaseB, correnteFaseC


# Funções que calculam as tensões fase-neutro na carga utilizando Ia * Za...
def tensaoCargaZa(circuito):
    return correnteFaseA(circuito) * circuito.za_carga


def tensaoCargaZb(circuito):
    return correnteFaseB(circuito) * circuito.zb_carga


def tensaoCargaZc(circuito):
    return correnteFaseC(circuito) * circuito.zc_carga
