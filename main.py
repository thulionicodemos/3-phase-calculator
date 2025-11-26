"""
Module: main
Author: Thulio Henrique
Description:
    Entry-point script for running the three-phase circuit analysis in a
    command-line environment. This script provides a simple text-based menu
    that allows the user to choose among:
        1. Y-connected (star) balanced or unbalanced circuit
        2. Δ-connected (delta) balanced circuit
        3. Δ-connected (delta) unbalanced circuit

    The script constructs a Circuito object with predefined electrical
    parameters (source voltages, impedances, load values) and dispatches the
    computation to the appropriate analysis module:
        - calc_circuito_eq_desesq_Y       (Y circuits)
        - calc_circuito_eq_DD             (Balanced Δ)
        - calc_circuito_deseq_D           (Unbalanced Δ)

    Results are printed directly to stdout using the formatting functions
    present in the calculation modules.

Main Function:
    main():
        Displays an interactive console menu, captures user input, constructs
        the Circuito instance, and executes the analysis based on the selected
        circuit topology.

Workflow Summary:
    1. Display circuit options (Y, Δ balanced, Δ unbalanced)
    2. Validate user input
    3. Initialize source voltages (Va, Vb, Vc) with 120° separation
    4. Construct Circuito object with:
           - 3-wire configuration
           - Line impedances
           - Load impedances
           - Phase-to-neutral voltages
    5. Call the appropriate computation function
    6. Print results to the terminal

Parameters:
    None (user input is collected interactively via console prompts)

Outputs:
    Printed results showing:
        - Circuit configuration
        - Phase voltages
        - Currents (line and/or phase)
        - Powers (complex, active, reactive)
        - Additional analysis depending on circuit type

Usage Example:
    python main.py

Notes:
    - This script is intended for console-based usage only.
    - For graphical operation, refer to the Streamlit interface implemented
      in painel.py.
    - Impedances and voltages inside this script are predefined for testing
      and demonstration purposes.
"""

from calc_circuito_eq_desesq_Y import calcula_Y
from calc_circuito_eq_DD import calcula_D_equilibrado
from calc_circuito_deseq_D import calcula_D_deseq
import convert as cv
from circuito_trifasico import Circuito


def main():

    # Menu para escolher o tipo de circuito
    print("Escolha o tipo de circuito:")
    print("1 - Circuito Y (estrela) equilibrado ou desequilibrado")
    print("2 - Circuito Δ (triângulo) equilibrado")
    print("3 - Circuito Δ (triângulo) desequilibrado")

    # Loop que roda o menu infinitamente até que uma opção válida seja escolhida
    while True:
        try:
            escolha = int(input("Digite o número da opção (1, 2 ou 3): "))
            if escolha in [1, 2, 3]:
                break
            else:
                print("Opção inválida. Escolha 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    ### Dados do circuito
    # Entrar com a tensão de fase-neutro da fonte
    Va = Vb = Vc = 127
    angulo_Va = 10
    angulo_Vb = angulo_Va - 120
    angulo_Vc = angulo_Va + 120

    circuito = Circuito(
        fios=3,
        va=cv.polar_to_rect(Va, angulo_Va),
        vb=cv.polar_to_rect(Vb, angulo_Vb),
        vc=cv.polar_to_rect(Vc, angulo_Vc),
        za_linha=(0.2 + 0.3j) * 0.8,
        zb_linha=(0.2 + 0.3j) * 0.8,
        zc_linha=(0.2 + 0.3j) * 0.8,
        za_carga=15 + 7j,
        zb_carga=20 + 10j,
        zc_carga=18 + 8j,
        zn=0,
    )
    ###################################################
    print(circuito)

    # Chamada da função de acordo com o tipo de circuito selecionado
    if escolha == 1:
        calcula_Y(circuito)
    elif escolha == 2:
        calcula_D_equilibrado(circuito)
    elif escolha == 3:
        calcula_D_deseq(circuito)


if __name__ == "__main__":
    main()
