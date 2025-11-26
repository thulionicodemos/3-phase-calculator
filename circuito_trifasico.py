"""
Module: circuito_trifasico
Author: Thulio Henrique
Description:
    Defines the Circuito class, which centralizes all electrical parameters
    and computational utilities required to analyze three-phase power
    systems in Y (star) and Δ (delta) configurations. This class serves as
    the data structure and computation engine used throughout the entire
    application.

    The class stores:
        - Phase source voltages (va, vb, vc)
        - Line impedances (Za', Zb', Zc')
        - Load impedances (Za, Zb, Zc)
        - Neutral impedance (Zn)
        - Wire configuration (3-wire or 4-wire)

    The class also provides built-in electrical computation methods,
    including:
        - Neutral current for 4-wire Y systems
        - Neutral displacement voltage for 3-wire Y systems
        - Star ↔ Delta impedance conversion utilities

Class:
    Circuito(fios, va, vb, vc, za_linha, zb_linha, zc_linha,
             za_carga, zb_carga, zc_carga, zn)

Methods:
    __str__(self):
        Returns a formatted string describing all circuit parameters.

    calcula_I_n(self):
        Computes the neutral current (In) for grounded 4-wire star systems:
            In = (Ia + Ib + Ic) / (1 + Zn/Z_total_A + Zn/Z_total_B + Zn/Z_total_C)
        where each Z_total = Z_load + Z_line.

    calcula_V_nl_n(self):
        Computes the neutral displacement voltage for 3-wire isolated star
        systems:
            V_nl_n = (Va/Z_total_A + Vb/Z_total_B + Vc/Z_total_C) /
                     (1/Z_total_A + 1/Z_total_B + 1/Z_total_C)

    converteCargaYD(self):
        Converts star-connected load impedances (Za, Zb, Zc) into their
        equivalent delta-connected impedances using:
            Zab = (ZaZb + ZbZc + ZcZa) / Zc
            Zbc = (ZaZb + ZbZc + ZcZa) / Za
            Zca = (ZaZb + ZbZc + ZcZa) / Zb

    converteCargaDY(self):
        Converts delta-connected load impedances into their equivalent
        star-connected impedances:
            Za = (Zab * Zca) / (Zab + Zbc + Zca)
            Zb = (Zbc * Zab) / (Zab + Zbc + Zca)
            Zc = (Zca * Zbc) / (Zab + Zbc + Zca)

Parameters:
    fios (int):
        Number of wires (3 or 4). Determines whether neutral current or
        neutral displacement voltage is used.

    va, vb, vc (complex):
        Phase source voltages.

    za_linha, zb_linha, zc_linha (complex):
        Line impedances for phases A, B, and C.

    za_carga, zb_carga, zc_carga (complex):
        Load impedances for phases A, B, and C.

    zn (complex):
        Neutral impedance (used only in 4-wire star systems).

Returns:
    None.
    The class acts as a container and computation object used by all other
    analysis modules.

Usage Example:
    from circuito_trifasico import Circuito
    circ = Circuito(4, Va, Vb, Vc, Za_l, Zb_l, Zc_l, Za, Zb, Zc, Zn)
    In = circ.calcula_I_n()
"""

from imprime_polar import imprimePolar as ip


# Classe que irá armazenar os dados do circuito
class Circuito:
    # Construtor da classe
    def __init__(
        self,
        fios,
        va,
        vb,
        vc,
        za_linha,
        zb_linha,
        zc_linha,
        za_carga,
        zb_carga,
        zc_carga,
        zn,
    ):
        # Atributos da classe
        self.fios = int(fios)
        self.va = complex(va)
        self.vb = complex(vb)
        self.vc = complex(vc)
        self.za_linha = complex(za_linha)
        self.zb_linha = complex(zb_linha)
        self.zc_linha = complex(zc_linha)
        self.za_carga = complex(za_carga)
        self.zb_carga = complex(zb_carga)
        self.zc_carga = complex(zc_carga)
        self.zn = complex(zn)

    # Função que imprime os dados do circuito
    def __str__(self):
        return (
            f"Dados do Circuito Trifásico:\n"
            f"Quantidade de fios (3 ou 4): {self.fios}\n"
            f"Tensões: Va = {ip(self.va)}, Vb = {ip(self.vb)}, Vc = {ip(self.vc)}\n"
            f"Impedâncias de linha: Za' = {self.za_linha:.2f}, Zb' = {self.zb_linha:.2f}, Zc' = {self.zc_linha:.2f}\n"
            f"Cargas: Za = {self.za_carga:.2f}, Zb = {self.zb_carga:.2f}, Zc = {self.zc_carga:.2f}\n"
            f"Impedância do neutro: Zn = {self.zn:.2f}\n"
        )

    # Função que calcula a corrente no neutro (In) quando o circuito é estrela aterrado
    def calcula_I_n(self):

        I_n = (
            self.va / (self.za_carga + self.za_linha)
            + self.vb / (self.zb_carga + self.zb_linha)
            + self.vc / (self.zc_carga + self.zc_linha)
        ) / (
            1
            + self.zn / (self.za_carga + self.za_linha)
            + self.zn / (self.zb_carga + self.zb_linha)
            + self.zn / (self.zc_carga + self.zc_linha)
        )

        return I_n

    # Função que calcula a tensão de deslocamento de neutro (Vn'n) quando o circuito é estrela isolado
    def calcula_V_nl_n(self):

        V_nl_n = (
            self.va / (self.za_carga + self.za_linha)
            + self.vb / (self.zb_carga + self.zb_linha)
            + self.vc / (self.zc_carga + self.zc_linha)
        ) / (
            1 / (self.za_carga + self.za_linha)
            + 1 / (self.zb_carga + self.zb_linha)
            + 1 / (self.zc_carga + self.zc_linha)
        )

        return V_nl_n

    # Função para realizar a conversão da carga de estrela para triângulo
    def converteCargaYD(self):

        Z_ab = (
            self.za_carga * self.zb_carga
            + self.zb_carga * self.zc_carga
            + self.zc_carga * self.za_carga
        ) / self.zc_carga

        Z_bc = (
            self.za_carga * self.zb_carga
            + self.zb_carga * self.zc_carga
            + self.zc_carga * self.za_carga
        ) / self.za_carga

        Z_ca = (
            self.za_carga * self.zb_carga
            + self.zb_carga * self.zc_carga
            + self.zc_carga * self.za_carga
        ) / self.zb_carga

        self.za_carga = Z_ab
        self.zb_carga = Z_bc
        self.zc_carga = Z_ca

    # Função para realizar a conversão da carga de triângulo para estrela
    def converteCargaDY(self):

        Z_a = (
            self.za_carga
            * self.zc_carga
            / (self.za_carga + self.zb_carga + self.zc_carga)
        )

        Z_b = (
            self.zb_carga
            * self.za_carga
            / (self.za_carga + self.zb_carga + self.zc_carga)
        )

        Z_c = (
            self.zc_carga
            * self.zb_carga
            / (self.za_carga + self.zb_carga + self.zc_carga)
        )

        self.za_carga = Z_a
        self.zb_carga = Z_b
        self.zc_carga = Z_c
