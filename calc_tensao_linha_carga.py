"""
Module: calc_tensao_linha_carga
Author: Thulio Henrique
Description:
    Provides functions for computing line-to-line voltages at the load in
    three-phase systems. These voltages are derived directly from the 
    phase-to-neutral voltages previously calculated by calc_tensao_carga.

    For a star-connected (Y) load, the phase load voltages Va', Vb', Vc'
    are combined to obtain the corresponding line voltages:

        V_ab = Va' − Vb'
        V_bc = Vb' − Vc'
        V_ca = Vc' − Va'

    These functions return the complex line voltages across each pair of
    load terminals.

Functions:
    tensaoLinhaZab(circuito):
        Computes line-to-line voltage Vab at the load.

    tensaoLinhaZbc(circuito):
        Computes line-to-line voltage Vbc at the load.

    tensaoLinhaZca(circuito):
        Computes line-to-line voltage Vca at the load.

Parameters:
    circuito (Circuito):
        An instance containing all voltages, impedances, and computed phase
        currents required to determine phase-to-neutral voltages at the load.

Returns:
    complex:
        The line-to-line voltage for the respective phase pair.

Usage Example:
    from calc_tensao_linha_carga import tensaoLinhaZab
    Vab = tensaoLinhaZab(circuito)

Notes:
    - These calculations assume the load voltages come from functions in 
      calc_tensao_carga.
    - Applicable for Y-connected loads. For Δ-connected systems, the load
      phase voltages correspond directly to the line voltages.
"""

from calc_tensao_carga import tensaoCargaZa, tensaoCargaZb, tensaoCargaZc


# Calcula as tensões fase-fase na carga utilizando Va'n' - Vb'n'...
def tensaoLinhaZab(circuito):
    return tensaoCargaZa(circuito) - tensaoCargaZb(circuito)


def tensaoLinhaZbc(circuito):
    return tensaoCargaZb(circuito) - tensaoCargaZc(circuito)


def tensaoLinhaZca(circuito):
    return tensaoCargaZc(circuito) - tensaoCargaZa(circuito)
