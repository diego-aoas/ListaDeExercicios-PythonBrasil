""""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme
e mostre a temperatura em graus Celsius.

    C = 5 * ((F-32) / 9).
"""

celsius = 0
fahrenheit = float(input("Informe a temperatura em Fahrenheit a ser convertida: "))

celsius = round(5 * ((fahrenheit - 32) / 9), 2)

print(f"A temperatura {fahrenheit}F em Celsius é {celsius}.")
