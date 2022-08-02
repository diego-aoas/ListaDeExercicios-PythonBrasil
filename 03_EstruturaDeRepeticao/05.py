"""
Altere o programa anterior permitindo ao usuário informar as
populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
"""

ano = 0
populacao_a = int(input("Informe a população de A: "))
taxa_a = float(input("Informe a taxa de crescimento da população de A: ")) / 100
populacao_b = int(input("Informe a população de B: "))
taxa_b = float(input("Informe a taxa de crescimento da população de B: ")) / 100

if populacao_a < populacao_b:
    if taxa_a > taxa_b:
        while populacao_a <= populacao_b:
            populacao_a += populacao_a * taxa_a
            populacao_b += populacao_b * taxa_b
            ano += 1

print(f"Em {ano} anos a População de A será maior que B!")
