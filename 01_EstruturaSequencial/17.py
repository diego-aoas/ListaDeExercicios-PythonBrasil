"""
Faça um Programa para uma loja de tintas. O programa deverá pedir
o tamanho em metros quadrados da área a ser pintada. Considere que
a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas
e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta
seja menor. Acrescente 10% de folga e sempre arredonde os valores
para cima, isto é, considere latas cheias.
"""
import math

area = float(input("Forneça a área em M²: "))

rendimento = math.ceil(area / 6)

lata_18l = math.ceil(rendimento / 18)

lata_3l = math.ceil(rendimento / 3.6)

total_lata18 = lata_18l * 80
total_lata3 = lata_3l * 25

rendimento_10pce = math.ceil(rendimento + (rendimento * 0.10))
latao = 0
latinha = 0


while rendimento_10pce >= 0:
    if rendimento_10pce >= 18 and rendimento_10pce > 4:
        latao += 1
        rendimento_10pce -= 18
    else:
        rendimento_10pce < 4
        latinha += 1
        rendimento_10pce -= 3.6

latas_distribuida = latao * 80 + latinha * 25

print(f"Para a área de {area}M² serão necessárias {lata_18l} latas de 18 litros totalizando R$ {total_lata18}.")
print(f"Para a área de {area}M² serão necessárias {lata_3l} latas de 3,6 litros totalizando R$ {total_lata3}.")
print(f"Para a área de {area}M² (considerando 10% de folga no rendimento) serão necessárias {latao}"
      f" latas de 18 litros e {latinha} de 3,6 litros, totalizando R$ {latas_distribuida}.")