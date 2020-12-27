"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

vogais = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

letra = input("Digite uma letra: ")

if letra in vogais:
    print("É vogal!")
else:
    print("É consoante...")
