"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
import math

raio = float(input("Insira o raio do círculo: "))

area = round(math.pi * math.pow(raio, 2), 2)

print(f"A área do círuculo é {area}.")
