"""
Module: calc_circuito_deseq_D
Author: Thulio Henrique
Description:
    Provides the implementation of the unbalanced Delta (Δ) three-phase
    circuit analysis. This module computes phase voltages, line currents,
    branch currents, load powers, line powers, and total source power for a
    Δ-connected load where impedances are not symmetrical between phases.

    The algorithm performs:
        - Conversion of load impedances to Δ configuration if needed
        - Calculation of phase voltages (Vab, Vbc, Vca)
        - Calculation of line currents using functions imported from calc_corrente
        - Computation of branch currents inside the unbalanced Δ load
        - Power calculation for the load and for the line impedances
        - Total complex, active, and reactive power (S, P, Q)
        - Power factor evaluation
        - Formatted printing of all intermediate results using imprime_polar
          and power printing utilities

Functions:
    calcula_D_deseq(circuito):
        Main function that receives a Circuito object and performs the full
        unbalanced Δ analysis. Results are printed to stdout so they can be
        captured by the Streamlit interface.

Parameters:
    circuito (Circuito):
        Object containing all source voltages, line impedances, load
        impedances, and system configuration.

Output:
    Prints all calculated quantities including:
        - Phase voltages
        - Line currents
        - Branch currents
        - Load powers (per phase and total)
        - Line powers
        - Source power (S, P, Q, |S|, power factor)

Usage Example:
    from calc_circuito_deseq_D import calcula_D_deseq
    calcula_D_deseq(circuito)

Notes:
    This module handles only Δ-connected unbalanced loads. For Y-connected or
    balanced Δ loads, use the corresponding modules:
        - calc_circuito_eq_desesq_Y.py
        - calc_circuito_eq_DD.py
"""

import numpy as np
from calc_corrente import (
    correnteFaseA as correnteLinhaA, 
    correnteFaseB as correnteLinhaB, 
    correnteFaseC as correnteLinhaC
    )
from imprime_polar import imprimePolar as ip
from calc_potencia import calculaPotencia, imprimePotencia


# Função que calcula um circuito triângulo desequilibrado
def calcula_D_deseq(circuito):

    # Salva as cargas do circuito antes da conversão
    zabOriginal = circuito.za_carga
    zbcOriginal = circuito.zb_carga
    zcaOriginal = circuito.zc_carga

    # Converte a carga em triângulo para estrela
    circuito.converteCargaDY()

    # Calcula as correntes de linha no circuito
    I_a = correnteLinhaA(circuito)
    I_b = correnteLinhaB(circuito)
    I_c = correnteLinhaC(circuito)

    # Calcula as tensões de fase na carga (Va'n'...)
    V_al = circuito.va - I_a * circuito.za_linha
    V_bl = circuito.vb - I_b * circuito.zb_linha
    V_cl = circuito.vc - I_c * circuito.zc_linha

    # Calcula as tensões fase-fase na carga (Va'b'...)
    V_albl = V_al - V_bl
    V_blcl = V_bl - V_cl
    V_clal = V_cl - V_al

    # Calcula as correntes de fase na carga
    I_ab = V_albl / zabOriginal
    I_bc = V_blcl / zbcOriginal
    I_ca = V_clal / zcaOriginal

    # Cria uma tupla com as correntes de fase na carga
    correntes_carga = (
        I_ab,
        I_bc,
        I_ca,
    )
    # Cria uma tupla com as tensões de fase na carga
    tensoes_carga = (
        V_albl,
        V_blcl,
        V_clal,
    )
    # Cria uma tupla com as correntes de linha
    correntes_linha = (
        I_a,
        I_b,
        I_c,
    )
    # Cria uma tupla com as tensões de perda na linha
    tensoes_linha = (
        I_a * circuito.za_linha,
        I_b * circuito.zb_linha,
        I_c * circuito.zc_linha,
    )

    # Chama a função que calcula as potências, passando as tuplas que contém as correntes e tensões e retorna um dicionário contendo as potências
    potencias_carga = calculaPotencia(tensoes_carga, correntes_carga)
    potencias_linha = calculaPotencia(tensoes_linha, correntes_linha)

    print("Os resultados do circuito Triângulo Desequilibrado são:\n")

    print(f"Ia = {ip(I_a)}")
    print(f"Ib = {ip(I_b)}")
    print(f"Ic = {ip(I_c)}\n")

    print(f"Iab = {ip(I_ab)}")
    print(f"Ibc = {ip(I_bc)}")
    print(f"Ica = {ip(I_ca)}\n")

    print(f"Va'b' = {ip(V_albl)}")
    print(f"Vb'c' = {ip(V_blcl)}")
    print(f"Vc'a' = {ip(V_clal)}\n")

    print("P carga")
    imprimePotencia(potencias_carga)

    print("P linha")
    imprimePotencia(potencias_linha)

    print(f"P fonte")
    print(f"    S = {(potencias_carga['S_total'] + potencias_linha['S_total']):.2f}")
    print(f"    P = {(potencias_carga['P_total'] + potencias_linha['P_total']):.2f}W")
    print(f"    Q = {(potencias_carga['Q_total'] + potencias_linha['Q_total']):.2f}VAr")
    print(f"   |S| = {np.abs((potencias_carga['S_total'] + potencias_linha['S_total'])):.2f}VA")
    print(f"   fp: {(
        (potencias_carga['P_total'] + potencias_linha['P_total']) / (
        (np.abs((potencias_carga['S_total'] + potencias_linha['S_total'])))
    )):.2f}\n"
    )
