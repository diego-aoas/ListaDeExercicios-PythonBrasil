"""
Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do Imposto de Renda, que depende
do salário bruto (conforme tabela abaixo) e 3% para o
Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas
não é descontado (é a empresa que deposita). O Salário Líquido
corresponde ao Salário Bruto menos os descontos. O programa
deverá pedir ao usuário o valor da sua hora e a quantidade de
horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo. No
exemplo o valor da hora é 5 e a quantidade de hora é 220.

            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00
            (-) INSS ( 10%)                 : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00
"""

salario_hora = float(input("Qual o seu salário/hora: "))
horas_trabalhadas = float(input("Quantidades de horas trabalhada no mês: "))

salario_bruto = horas_trabalhadas * salario_hora
sindicato = salario_bruto * 0.03
fgts = salario_bruto * 0.11
inss = salario_bruto * 0.1

if salario_bruto <= 900.0:
    ir = 0
elif salario_bruto > 900.0 and salario_bruto <= 1500.0:
    ir = salario_bruto * 0.05
elif salario_bruto > 1500.0 and salario_bruto <= 2500.0:
    ir = salario_bruto * 0.1
else:
    ir = salario_bruto * 0.2

descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos

print(f"O salário bruto: R$ {salario_bruto}\n"
      f"(-) IR:          R$ {ir}\n"
      f"(-) INSS:        R$ {inss}\n"
      f"(-) Sindicato:   RS {sindicato}\n"
      f"FGTS:            R$ {fgts}\n"
      f"Total Descontos: R$ {descontos}\n"
      f"Salário Liquido: R$ {salario_liquido}")
