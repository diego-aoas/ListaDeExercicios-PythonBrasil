"""
Faça um programa que lê as duas notas parciais obtidas
or um aluno numa disciplina ao longo de um semestre, e
calcule a sua média. A atribuição de conceitos obedece à
tabela abaixo:

      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0        A
      Entre 7.5 e 9.0         B
      Entre 6.0 e 7.5         C
      Entre 4.0 e 6.0         D
      Entre 4.0 e zero        E

O algoritmo deve mostrar na tela as notas,
a média, o conceito correspondente e a
mensagem “APROVADO” se o conceito for
A, B ou C ou “REPROVADO” se o conceito for D ou E
"""

nota1 = float(input("Digite Nota 1: "))
nota2 = float(input("Digite Nota 2: "))
conceito = None

media = (nota1 + nota2) / 2

if media >= 9.0 <= 10.0:
    conceito = 'A'
elif media >= 7.5 < 9.0:
    conceito = 'B'
elif media >= 6.0 < 7.5:
    conceito = 'C'
elif media >= 4.0 < 6.0:
    conceito = 'D'
else:
    conceito = 'E'

if conceito == 'A' == 'B' == 'C':
    print(f"Nota {nota1}, Nota {nota2} e a média: {media} = APROVADO")
else:
    print(f"Nota {nota1}, Nota {nota2} e a média: {media} = REPROVADO")
