"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
numero_1 = float(input("Insira o número 1: "))
numero_2 = float(input("Insira o número 2: "))
numero_3 = float(input("Insira o número 3: "))

if numero_1 > numero_2 > numero_3:
    print(f"A sequência decrescente N1: {numero_1}, N2: {numero_2}, N3: {numero_3}.")
elif numero_1 > numero_3 > numero_2:
    print(f"A sequência decrescente N1: {numero_1}, N3: {numero_3}, N2: {numero_2}.")
elif numero_2 > numero_1 > numero_3:
    print(f"A sequência decrescente N2: {numero_2}, N1: {numero_1}, N3: {numero_3}.")
elif numero_2 > numero_3 > numero_1:
    print(f"A sequência decrescente N2: {numero_2}, N3: {numero_3}, N1: {numero_1}")
elif numero_3 > numero_1 > numero_2:
    print(f"A sequência decrescente N3: {numero_3}, N1: {numero_1}, N2: {numero_2}.")
else:
    print(f"A sequência decrescente N3: {numero_3}, N2: {numero_2}, N1: {numero_1}.")
