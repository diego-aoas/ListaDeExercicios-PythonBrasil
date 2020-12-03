"""
Faça um Programa que calcule a área de um quadrado,
em seguida mostre o dobro desta área para o usuário.
"""

import math

quadrado = float(input("Insira o tamanho do lado do quadrado: "))

area = math.pow(quadrado, 2) * 2

print(f"O dobro da área do quadrado calculado é {area}.")
