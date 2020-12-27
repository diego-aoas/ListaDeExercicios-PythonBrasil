"""
Faça um Programa que leia três números e mostre o maior deles.
"""

numero_1 = float(input("Digite o primeira número: "))
numero_2 = float(input("Digite o segundo número: "))
numero_3 = float(input("Digite o terceiro número: "))

if numero_1 > numero_2 and numero_1 > numero_3:
    print(f"O número {numero_1} é maior que {numero_2} e {numero_3}.")
elif numero_2 > numero_1 and numero_2 > numero_3:
    print(f"O número {numero_2} é maior que {numero_1} e {numero_3}.")
else:
    print(f"O número {numero_3} é maior que {numero_1} e {numero_2}.")
