"""
Supondo que a população de um país A seja da ordem
de 80000 habitantes com uma taxa anual de crescimento
de 3% e que a população de B seja 200000 habitantes
com uma taxa de crescimento de 1.5%. Faça um programa
que calcule e escreva o número de anos necessários para
que a população do país A ultrapasse ou iguale a população
do país B, mantidas as taxas de crescimento
"""

ano = 0
populacao_a = 80000
taxa_a = 0.03
populacao_b = 200000
taxa_b = 0.015

while populacao_a <= populacao_b:
    populacao_a += populacao_a * taxa_a
    populacao_b += populacao_b * taxa_b
    ano += 1

print(f"Em {ano} anos a População de A será maior que B!")
