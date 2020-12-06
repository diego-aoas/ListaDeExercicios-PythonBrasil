"""
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que
a cobertura da tinta é de 1 litro para cada 3
metros quadrados e que a tinta é vendida em latas
de 18 litros, que custam R$ 80,00. Informe ao
usuário a quantidades de latas de tinta a serem
compradas e o preço total.
"""
import math

area = float(input("Informe a área a ser pintada: "))

rendimento = math.ceil(area / 3)

total_latas = math.ceil(rendimento / 18)
valor_total = 80 * total_latas

print(f"Serão necessárias {total_latas} latas e ficará o valor total de R$ {valor_total}.")
