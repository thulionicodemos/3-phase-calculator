"""
Module: painel
Author: Thulio Henrique
Description:
    Streamlit-based graphical interface for performing three-phase circuit
    analysis in Y (star) and Δ (delta) configurations. This interactive panel
    allows users to input phase voltages, line impedances, load impedances,
    and neutral impedance, and then compute:

        - Phase currents
        - Line currents
        - Phase and line voltages
        - Complex, active, and reactive power
        - Additional derived electrical quantities

    The UI is designed for educational and engineering purposes, providing
    fast and clear visualization of numerical results without requiring the
    user to write or edit Python code.

Main Features:
    • Input fields for:
        - Phase voltages in polar form (Va, Vb, Vc)
        - Line impedances Za', Zb', Zc'
        - Load impedances Za, Zb, Zc
        - Neutral impedance Zn
        - Circuit configuration: Y, Δ balanced, Δ unbalanced

    • A calculation button that:
        1. Builds a Circuito instance
        2. Calls the appropriate analysis function:
               - calcula_Y
               - calcula_D_equilibrado
               - calcula_D_deseq
        3. Captures printed results through stdout redirection
        4. Displays the results directly below the form

    • Automatically scrolls back to the top after calculation.

Functions:
    capturar_saida(func, *args, **kwargs):
        Utility function that redirects stdout to a string buffer in order to
        capture print-based output from the computational modules. This allows
        the results to be displayed cleanly in the Streamlit interface.

External Dependencies:
    - circuito_trifasico.Circuito
    - calc_circuito_eq_desesq_Y.calcula_Y
    - calc_circuito_eq_DD.calcula_D_equilibrado
    - calc_circuito_deseq_D.calcula_D_deseq
    - convert.polar_to_rect

Streamlit Structure:
    1. CSS setup for improved aesthetics
    2. Parameter input section:
         - Dropdown for circuit type
         - Number inputs arranged in columns for clarity
    3. Calculation trigger
    4. Results section rendered dynamically upon button press

Usage:
    Run the Streamlit app using:
        streamlit run painel.py

Notes:
    - This interface replaces the traditional console-based execution used
      in main.py, providing accessibility on desktop and mobile devices.
    - The panel can be deployed online via Streamlit Cloud or any compatible
      hosting service.
"""

import streamlit as st
import io
import contextlib

from circuito_trifasico import Circuito
from calc_circuito_eq_desesq_Y import calcula_Y
from calc_circuito_eq_DD import calcula_D_equilibrado
from calc_circuito_deseq_D import calcula_D_deseq
import convert as cv


# CSS
st.markdown(
    """
<style>
    h1, h2, h3 {
        color: #00AEEF !important;
    }
    hr { border: 1px solid #1B1F24; }
    input { border-radius: 5px !important; }
</style>
""",
    unsafe_allow_html=True,
)


# Função que captura prints das funções de cálculo
def capturar_saida(func, *args, **kwargs):
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        func(*args, **kwargs)
    return buffer.getvalue()


st.title("Calculadora de Circuitos Trifásicos")
st.title("<small><i>Three-Phase Circuit Calculator</i></small>", unsafe_allow_html=True)
st.markdown(
    "**Realiza os cálculos de corrente, tensão e potência em configurações Y e Δ.**"
)
st.caption("**Performs current, voltage, and power calculations in Y and Δ configurations.**")

# FORMULÁRIO DE PARÂMETROS
st.header("Parâmetros do Circuito")
st.caption("Circuit Parameters")

st.markdown("---")
st.subheader("Selecione o tipo de circuito")
st.caption("Select the circuit type")

tipo_circuito = st.selectbox(
    "",
    ["Y (estrela)", "Δ (triângulo) equilibrado", "Δ (triângulo) desequilibrado"],
)

# TENSÕES
st.markdown("---")
st.subheader("Tensões da Fonte — Forma Polar")
st.caption("Source Voltages — Polar Pattern")

st.markdown("**Va**")
col1, col2 = st.columns(2)
with col1:
    Va_mod = st.number_input("Módulo (V)", value=0.0, key="Va_mod")
with col2:
    Va_ang = st.number_input("Ângulo (°)", value=0.0, key="Va_ang")

st.markdown("**Vb**")
col1, col2 = st.columns(2)
with col1:
    Vb_mod = st.number_input("Módulo (V)", value=0.0, key="Vb_mod")
with col2:
    Vb_ang = st.number_input("Ângulo (°)", value=0.0, key="Vb_ang")

st.markdown("**Vc**")
col1, col2 = st.columns(2)
with col1:
    Vc_mod = st.number_input("Módulo (V)", value=0.0, key="Vc_mod")
with col2:
    Vc_ang = st.number_input("Ângulo (°)", value=0.0, key="Vc_ang")

# IMPEDÂNCIAS DE LINHA
st.markdown("---")
st.subheader("Impedâncias de Linha")
st.caption("Line Impedances")

st.markdown("**Za'**")
col1, col2 = st.columns(2)
with col1:
    Za_linha_real = st.number_input("Re(Za')", value=0.0, key="Za_linha_real")
with col2:
    Za_linha_imag = st.number_input("Im(Za')", value=0.0, key="Za_linha_imag")

st.markdown("**Zb'**")
col1, col2 = st.columns(2)
with col1:
    Zb_linha_real = st.number_input("Re(Zb')", value=0.0, key="Zb_linha_real")
with col2:
    Zb_linha_imag = st.number_input("Im(Zb')", value=0.0, key="Zb_linha_imag")

st.markdown("**Zc'**")
col1, col2 = st.columns(2)
with col1:
    Zc_linha_real = st.number_input("Re(Zc')", value=0.0, key="Zc_linha_real")
with col2:
    Zc_linha_imag = st.number_input("Im(Zc')", value=0.0, key="Zc_linha_imag")

# IMPEDÂNCIAS DA CARGA
st.markdown("---")
st.subheader("Impedâncias da Carga")
st.caption("Load Impedances")

st.markdown("**Za**")
col1, col2 = st.columns(2)
with col1:
    Za_real = st.number_input("Re(Za)", value=0.0, key="Za_real")
with col2:
    Za_imag = st.number_input("Im(Za)", value=0.0, key="Za_imag")

st.markdown("**Zb**")
col1, col2 = st.columns(2)
with col1:
    Zb_real = st.number_input("Re(Zb)", value=0.0, key="Zb_real")
with col2:
    Zb_imag = st.number_input("Im(Zb)", value=0.0, key="Zb_imag")

st.markdown("**Zc**")
col1, col2 = st.columns(2)
with col1:
    Zc_real = st.number_input("Re(Zc)", value=0.0, key="Zc_real")
with col2:
    Zc_imag = st.number_input("Im(Zc)", value=0.0, key="Zc_imag")

# IMPEDÂNCIA DO NEUTRO
st.markdown("---")
st.subheader("Impedância do Neutro")
st.caption("Neutral Impedance")

st.markdown("**Zn**")
col1, col2 = st.columns(2)
with col1:
    Zn_real = st.number_input("Re(Zn)", value=0.0, key="Zn_real")
with col2:
    Zn_imag = st.number_input("Im(Zn)", value=0.0, key="Zn_imag")

# BOTÃO PARA CALCULAR
st.markdown("---")
calcular = st.button("Calcular")

# RESULTADOS
if calcular:

    circuito = Circuito(
        fios=3,
        va=cv.polar_to_rect(Va_mod, Va_ang),
        vb=cv.polar_to_rect(Vb_mod, Vb_ang),
        vc=cv.polar_to_rect(Vc_mod, Vc_ang),
        za_linha=complex(Za_linha_real, Za_linha_imag),
        zb_linha=complex(Zb_linha_real, Zb_linha_imag),
        zc_linha=complex(Zc_linha_real, Zc_linha_imag),
        za_carga=complex(Za_real, Za_imag),
        zb_carga=complex(Zb_real, Zb_imag),
        zc_carga=complex(Zc_real, Zc_imag),
        zn=complex(Zn_real, Zn_imag),
    )

    if tipo_circuito == "Y (estrela)":
        saida = capturar_saida(calcula_Y, circuito)
    elif tipo_circuito == "Δ (triângulo) equilibrado":
        saida = capturar_saida(calcula_D_equilibrado, circuito)
    else:
        saida = capturar_saida(calcula_D_deseq, circuito)

    # Exibição dos resultados
    st.markdown("---")
    st.subheader("Resultados")
    st.caption("Results")
    st.text(saida)
