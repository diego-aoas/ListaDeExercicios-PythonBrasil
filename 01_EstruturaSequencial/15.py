"""
Faça um Programa que pergunte quanto você ganha por hora
e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês, sabendo-se que são
descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
para o sindicato, faça um programa que nos dê:

    a. salário bruto.
    b. quanto pagou ao INSS.
    c. quanto pagou ao sindicato.
    d. o salário líquido.
    e. calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

    Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

valor_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhada = float(input("Quantas horas trabalhou no mês? "))

salario_bruto = valor_hora * horas_trabalhada
inss = salario_bruto * 8 / 100
sindicato = salario_bruto * 5 / 100
salario_liquido = salario_bruto - (inss + sindicato)

print(f"Seu salário bruto é de R$ {salario_bruto}")
print(f"Você pagou R$ {inss} de INSS.")
print(f"Você pagou R$ {sindicato} para o sindicato.")
print(f"Seu salário liquido é de R$ {salario_liquido}.")
