"""
Module: calc_potencia
Author: Thulio Henrique
Description:
    Provides utility functions for computing and reporting complex, active,
    reactive, and apparent power in three-phase electrical systems. The module
    handles per-phase power as well as total system power, supporting both
    balanced and unbalanced loads.

    Power is computed using the standard complex power relation:
        S = V * conj(I)

    For each phase (A, B, C), the following quantities are calculated:
        - Complex power (S)
        - Active power (P = Re{S})
        - Reactive power (Q = Im{S})
        - Apparent power (|S|)

    Total system power is obtained by summing the phase complex powers.

Functions:
    calculaPotencia(tensoes, correntes):
        Computes the complex, active, reactive, and apparent power per phase
        and for the entire circuit. Returns a dictionary with all quantities.

    imprimePotencia(resultados):
        Prints formatted power results to stdout, including:
            - Per-phase S, P, Q, |S|
            - Total S, P, Q, |S|
            - Power factor and classification (lagging/leading/in-phase)

Parameters:
    tensoes (tuple[complex]):
        Tuple containing phase voltages (Va, Vb, Vc).

    correntes (tuple[complex]):
        Tuple containing phase currents (Ia, Ib, Ic).

Returns (from calculaPotencia):
    dict:
        {
            "S_fases": { "A": Sa, "B": Sb, "C": Sc },
            "P_fases": { ... },
            "Q_fases": { ... },
            "S_aparente_fases": { ... },
            "S_total": complex,
            "P_total": float,
            "Q_total": float,
            "S_aparente_total": float,
            "fp": float,          # power factor
            "tipo_fp": str        # "lagging", "leading", or "in-phase"
        }

Usage Example:
    from calc_potencia import calculaPotencia, imprimePotencia

    resultados = calculaPotencia(tensoes, correntes)
    imprimePotencia(resultados)

Notes:
    - All values use the standard sign convention of power systems.
    - The module is independent and can be reused in any three-phase analysis.
    - Complex arithmetic is handled using NumPy for numerical stability.
"""

import numpy as np


# Função que calcula a potência em cada fase, potência total e fator de potência do circuito
def calculaPotencia(tensoes, correntes):

    # Dicionário que armazena a potência complexa em cada fase
    S_fases = {
        "A": tensoes[0] * np.conj(correntes[0]),
        "B": tensoes[1] * np.conj(correntes[1]),
        "C": tensoes[2] * np.conj(correntes[2]),
    }

    # P (ativa), Q (reativa) e |S| (aparente) por fase
    P_fases = {fase: np.real(S) for fase, S in S_fases.items()} # Extrai a parte real e armazena a potência ativa em cada fase
    Q_fases = {fase: np.imag(S) for fase, S in S_fases.items()} # Extrai a parte imaginária e armazena a potência reativa em cada fase
    S_aparente_fases = {fase: np.abs(S) for fase, S in S_fases.items()} # Calcula o módulo da potência complexa e armazena a potência aparente em cada fase

    # Soma as potências para chegar no valor total do circuito
    S_total = sum(S_fases.values())
    P_total = np.real(S_total)
    Q_total = np.imag(S_total)
    S_aparente_total = np.abs(S_total)

    # Calcula o fator de potência total do circuito e indica o tipo
    fp = P_total / S_aparente_total
    if Q_total > 0:
        tipo_fp = "atrasado (indutivo)."
    elif Q_total < 0:
        tipo_fp = "adiantado (capacitivo)."
    else:
        tipo_fp = "em fase."

    # Dicionário que armazena os valores das potências já calculadas
    resultados = {
        "S_fases": S_fases,
        "P_fases": P_fases,
        "Q_fases": Q_fases,
        "S_aparente_fases": S_aparente_fases,
        "S_total": S_total,
        "P_total": P_total,
        "Q_total": Q_total,
        "S_aparente_total": S_aparente_total,
        "fp": fp,
        "tipo_fp": tipo_fp,
    }

    return resultados

# Função que imprime as potências por fase e total
def imprimePotencia(resultados):

    print("Potências:\n")
    print("Fase A:")
    print(f"    Sa = {resultados['S_fases']['A']:.2f}")
    print(f"    Pa = {resultados['P_fases']['A']:.2f}W")
    print(f"    Qa = {resultados['Q_fases']['A']:.2f}var")
    print(f"   |Sa| = {resultados['S_aparente_fases']['A']:.2f}VA\n")

    print("Fase B:")
    print(f"    Sb = {resultados['S_fases']['B']:.2f}")
    print(f"    Pb = {resultados['P_fases']['B']:.2f}W")
    print(f"    Qb = {resultados['Q_fases']['B']:.2f}var")
    print(f"   |Sb| = {resultados['S_aparente_fases']['B']:.2f}VA\n")

    print("Fase C:")
    print(f"    Sc = {resultados['S_fases']['C']:.2f}")
    print(f"    Pc = {resultados['P_fases']['C']:.2f}W")
    print(f"    Qc = {resultados['Q_fases']['C']:.2f}var")
    print(f"   |Sc| = {resultados['S_aparente_fases']['C']:.2f}VA\n")

    print("Total:")
    print(f"    S = {resultados['S_total']:.2f}")
    print(f"    P = {resultados['P_total']:.2f}W")
    print(f"    Q = {resultados['Q_total']:.2f}var")
    print(f"   |S| = {resultados['S_aparente_total']:.2f}VA\n")

    print("Fator de Potência:")
    print(f"    fp = {resultados['fp']:.2f}")
    print(f"    Tipo: {resultados['tipo_fp']}\n")
