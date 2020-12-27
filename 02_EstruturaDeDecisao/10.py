"""
Faça um Programa que pergunte em
que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino
ou N- Noturno. Imprima a mensagem
"Bom Dia!", "Boa Tarde!" ou
"Boa Noite!" ou "Valor Inválido!",
conforme o caso.
"""

letra = input("Digite 'M' - Matutino, 'V' - Vespertino, 'N' - Noturno: ")

if letra == 'M' or letra == 'm':
    print("Bom dia!!!")
elif letra == 'V' or letra == 'v':
    print("Boa Tarde!!!")
elif letra == 'N' or letra == 'n':
    print("Boa Noite!!!")
else:
    print("Valor Inválido!")
