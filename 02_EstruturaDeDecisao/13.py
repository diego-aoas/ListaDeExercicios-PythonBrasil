"""
Faça um Programa que leia um número e exiba o dia
correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.
"""

dia = input("Digite um número: ")

if dia == '1':
    print("O dia da semana correspondente é Domingo")
if dia == '2':
    print("O dia da semana correspondente é Segunda-feira")
elif dia == '3':
    print("O dia da semana correspondente é Terça-feira")
elif dia == '4':
    print("O dia da semana correspondente é Quarta-feira")
elif dia == '5':
    print("O dia da semana correspondente é Quinta-feira")
elif dia == '6':
    print("O dia da semana correspondente é Sexta-feira")
elif dia == '7':
    print("O dia da semana correspondente é Sábado")
else:
    print("Valor incorreto...")