"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

numero_1 = float(input("Digite o primeira número: "))
numero_2 = float(input("Digite o segundo número: "))
numero_3 = float(input("Digite o terceiro número: "))

maior = None
menor = None

if numero_1 > numero_2 and numero_1 > numero_3:
    maior = numero_1
elif numero_2 > numero_1 and numero_2 > numero_3:
    maior = numero_2
else:
    maior = numero_3

if numero_1 < numero_2 and numero_1 < numero_3:
    menor = numero_1
elif numero_2 < numero_1 and numero_2 < numero_3:
    menor = numero_2
else:
    menor = numero_3

print(
    f"O {maior} é o maior número entre {numero_1}, {numero_2} e {numero_3} e o {menor} é o menor número entre {numero_1}, {numero_2} e {numero_3}.")
