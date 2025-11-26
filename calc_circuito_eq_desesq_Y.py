"""
Module: calc_circuito_eq_desesq_Y
Author: Thulio Henrique
Description:
    Implements the analysis of three-phase Y (star) connected loads, supporting
    both balanced and unbalanced configurations. The module computes:
        - Neutral displacement voltage (for 3-wire systems)
        - Neutral current (for 4-wire systems)
        - Phase currents
        - Phase voltages at the load
        - Line voltages
        - Complex power (S), active power (P), and reactive power (Q)

    The function prints formatted results using polar notation utilities and
    power-reporting functions, enabling capture within user interfaces such as
    Streamlit.

Main Function:
    calcula_Y(circuito):
        Executes the full computation for a Y-connected circuit. The function
        automatically detects whether the system is 3-wire or 4-wire based on
        circuito.fios and calculates either the neutral displacement voltage
        or the neutral current accordingly.

Parameters:
    circuito (Circuito):
        An instance of the Circuito class containing:
            - Phase-to-neutral source voltages
            - Load impedances (phase-by-phase)
            - Line impedances (if applicable)
            - Number of wires (3 or 4)
            - Utility methods to compute neutral quantities

Computational Steps:
    1. Computes neutral displacement voltage (3-wire) or neutral current (4-wire).
    2. Computes phase currents Ia, Ib, Ic using correnteFaseA/B/C.
    3. Computes phase load voltages Va', Vb', Vc' using tensaoCargaZa/Zb/Zc.
    4. Computes line voltages Vab, Vbc, Vca using tensaoLinhaZab/Zbc/Zca.
    5. Computes load power using calculaPotencia.
    6. Prints:
        - Neutral quantities (Vn'n or In)
        - Phase currents
        - Phase load voltages
        - Line voltages
        - Power summary (S, P, Q, pf)

Returns:
    None.   
    Outputs are printed directly to stdout for display or capture.

Usage Example:
    from calc_circuito_eq_desesq_Y import calcula_Y
    calcula_Y(circuito)

Notes:
    - This module handles BOTH balanced and unbalanced Y configurations.
    - For balanced Δ loads, use calc_circuito_eq_DD.
    - For unbalanced Δ loads, use calc_circuito_deseq_D.
"""

from calc_corrente import correnteFaseA, correnteFaseB, correnteFaseC
from calc_tensao_carga import tensaoCargaZa, tensaoCargaZb, tensaoCargaZc
from calc_tensao_linha_carga import tensaoLinhaZab, tensaoLinhaZbc, tensaoLinhaZca
from calc_potencia import calculaPotencia, imprimePotencia
from imprime_polar import imprimePolar as ip


# Função que calcula um circuito estrela seja ele equilibrado ou desequilibrado
def calcula_Y(circuito):

    print("Os resultados do circuito estrela são:\n")

    # Imprime os valores de tensão de deslocamento de neutro e corrente no neutro dependendo da configuração do circuito estrela
    if circuito.fios == 3:
        print(f"Vn'n = {ip(circuito.calcula_V_nl_n())}\n")
    else:
        print(f"In = {ip(circuito.calcula_I_n())}\n")

    # Cria uma tupla com os valores das correntes de fase
    correntes = (
        correnteFaseA(circuito),
        correnteFaseB(circuito),
        correnteFaseC(circuito),
    )
    # Cria uma tupla com os valores das tensões de fase na carga
    tensoes = (
        tensaoCargaZa(circuito),
        tensaoCargaZb(circuito),
        tensaoCargaZc(circuito),
    )
    # Chama a função que calcula as potências, passando as tuplas que contém as correntes e tensões e retorna um dicionário contendo as potências
    potencias = calculaPotencia(tensoes, correntes)

    print(f"Ia = {ip(correnteFaseA(circuito))}A")
    print(f"Ib = {ip(correnteFaseB(circuito))}A")
    print(f"Ic = {ip(correnteFaseC(circuito))}A\n")

    print(f"Va'n' = {ip(tensaoCargaZa(circuito))}V")
    print(f"Vb'n' = {ip(tensaoCargaZb(circuito))}V")
    print(f"Vc'n' = {ip(tensaoCargaZc(circuito))}V\n")

    print(f"Va'b' = {ip(tensaoLinhaZab(circuito))}V")
    print(f"Vb'c' = {ip(tensaoLinhaZbc(circuito))}V")
    print(f"Vc'a' = {ip(tensaoLinhaZca(circuito))}V\n")

    imprimePotencia(potencias)
