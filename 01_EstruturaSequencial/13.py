"""
Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

    a. Para homens: (72.7*h) - 58
    b. Para mulheres: (62.1*h) - 44.7
"""

h = float(input("Insira sua altura (em metros): "))

peso_homem = round((72.7 * h) - 58,2)
peso_mulher = round((62.1 * h) - 44.7, 2)

print(f"Para homens a altura de {h}m o peso ideal é de {peso_homem}kg.")
print(f"Para mulheres a altura de {h}m o peso ideal é de {peso_mulher}kg")
