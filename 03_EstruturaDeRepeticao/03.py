"""
Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';
"""

nome = input("Insira o nome: ")
while len(nome) < 3:
    nome = input("Nome menor que 3 caracteres digite novamente: ")

idade = int(input("Insira a idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Idade menor que 0 ou maior que 150, digite novamente a idade: "))

salario = float(input("Insira o salário: "))
while salario <= 0:
    salario = float(input("Salário menor que 0, insira um novo: "))

sexo = input("Insira o sexo: ")
while sexo != 'f' and sexo != 'm':
    sexo = input("Sexo inválido, insira novo sexo: ")

estado_civil = input("Insira o estado cível: ")
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    estado_civil = input("Estado civil inválido, insira novamente: ")