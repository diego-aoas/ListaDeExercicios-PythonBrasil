"""
Faça um Programa que pergunte quanto você ganha por hora
e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""

salario_mes = 0
ganho_hora = float(input("Quanto você ganhar por hora? "))
horas_trabalhada = float(input("Qual o número de horas trabalhada por mês? "))

salario_mes = ganho_hora * horas_trabalhada

print(f"O seu salário total no mês é de R$ {salario_mes}.")