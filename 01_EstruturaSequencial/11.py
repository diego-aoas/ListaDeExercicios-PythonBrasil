"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    a. o produto do dobro do primeiro com metade do segundo .
    b. a soma do triplo do primeiro com o terceiro.
    c. o terceiro elevado ao cubo.
"""
import math
numero1 = int(input("Insira o número 1: "))
numero2 = int(input("Insira o número 2: "))
numero3 = float(input("Insira o número 3: "))

print(f"O produto do dobro de {numero1} com metade de {numero2}: ", numero1 * 2 + numero2 / 2)
print(f"A soma do {numero1} com {numero3} é: ", numero1 * 3 + numero3)
print(f"{numero3} elevado ao cubo é: ", math.pow(numero3, 3))
