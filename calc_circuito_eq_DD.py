"""
Module: calc_circuito_eq_DD
Author: Thulio Henrique
Description:
    Provides the implementation for analyzing a balanced Delta (Δ) three-phase
    circuit. In a Δ-connected balanced load, all impedances are equal and the
    system exhibits symmetrical phase relationships. This module calculates
    phase currents, line currents, phase voltages, and both load and line
    complex powers.

    This module is part of a complete three-phase analysis toolkit that also
    includes unbalanced Δ and Y (star) configurations.

Main Function:
    calcula_D_equilibrado(circuito):
        Executes all computations for a balanced Δ load. Results are printed in
        formatted text, suitable for capture by a Streamlit interface or for
        direct use in console-based inspection.

Parameters:
    circuito (Circuito):
        An instance of the Circuito class containing:
            - Phase-to-neutral source voltages (va, vb, vc)
            - Line impedances (za_linha, zb_linha, zc_linha)
            - Load impedances (assumed equal for balanced Δ)
            - System metadata (e.g., number of wires)

Computational Steps:
    1. Computes phase (branch) currents I_ab, I_bc, I_ca using calc_corrente.
    2. Computes line currents I_a, I_b, I_c using calc_corrente_linha_carga.
    3. Computes phase voltages at the load (Va, Vb, Vc) using calc_tensao_carga.
    4. Computes complex power for the load and line (S, P, Q) using calculaPotencia.
    5. Prints:
        - Phase voltages
        - Branch currents
        - Line currents
        - Load powers
        - Line powers

Returns:
    None.   
    The function prints all results to stdout. For GUI usage (e.g., Streamlit),
    the output is typically captured using an I/O redirection utility.

Usage Example:
    from calc_circuito_eq_DD import calcula_D_equilibrado
    calcula_D_equilibrado(circuito)

Notes:
    - Designed specifically for balanced Δ circuits.
    - For unbalanced Δ circuits, use calc_circuito_deseq_D.
    - For Y (star) circuits, use calc_circuito_eq_desesq_Y.
"""

from calc_corrente import (
    correnteFaseA as Iab,
    correnteFaseB as Ibc,
    correnteFaseC as Ica,
)
from calc_corrente_linha_carga import (
    correnteLinhaA as Ia,
    correnteLinhaB as Ib,
    correnteLinhaC as Ic,
)
from calc_tensao_carga import (
    tensaoCargaZa as Va,
    tensaoCargaZb as Vb,
    tensaoCargaZc as Vc,
)
from calc_potencia import calculaPotencia, imprimePotencia
from imprime_polar import imprimePolar as ip


# Função que calcula um circuito triângulo equilibrado
def calcula_D_equilibrado(circuito):
    
    # Cria uma tupla com as correntes de fase na carga
    correntes_carga = (
        Iab(circuito),
        Ibc(circuito),
        Ica(circuito),
    )
    # Cria uma tupla com as correntes de linha
    correntes_linha = (
        Ia(circuito),
        Ib(circuito),
        Ic(circuito),
    )
    # Cria uma tupla com as tensões de fase na carga
    tensoes_carga = (
        Va(circuito),
        Vb(circuito),
        Vc(circuito),
    )
    
    # Chama a função que calcula as potências, passando as tuplas que contém as correntes e tensões e retorna um dicionário contendo as potências
    potencias_carga = calculaPotencia(tensoes_carga, correntes_carga)
    potencias_linha = calculaPotencia(tensoes_carga, correntes_linha)

    print("Os resultados do circuito triângulo equilibrado são:\n")

    # Imprimindo os resultados
    print("Como a configuração é triangulo, as tensões de linha e de fase são iguais.")
    print(f"Va'n' = {ip(Va(circuito))}")
    print(f"Vb'n' = {ip(Vb(circuito))}")
    print(f"Vc'n' = {ip(Vc(circuito))}\n")

    print(f"Ia'b' = {ip(Iab(circuito))}")
    print(f"Ib'c' = {ip(Ibc(circuito))}A")
    print(f"Ic'a' = {ip(Ica(circuito))}A\n")

    print(f"Ia = {ip(Ia(circuito))}")
    print(f"Ib = {ip(Ib(circuito))}")
    print(f"Ic = {ip(Ic(circuito))}\n")
    
    print("P carga")
    imprimePotencia(potencias_carga)

    print("P linha")
    imprimePotencia(potencias_linha)
