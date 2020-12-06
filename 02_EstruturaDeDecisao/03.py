"""
Faça um Programa que verifique se uma letra
digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

letra = input("Digite uma letra: ")

if letra == 'M' or letra == 'm':
    print("Masculino!")
elif letra == 'F' or letra == 'f':
    print("Feminino!")
else:
    print("Sexo inválido...")