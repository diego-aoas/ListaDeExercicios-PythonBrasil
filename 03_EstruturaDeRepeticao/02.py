"""
Faça um programa que leia um nome de usuário
e a sua senha e não aceite a senha igual ao
nome do usuário, mostrando uma mensagem de
erro e voltando a pedir as informações.
"""

usuario = input("Insira o nome de usuário: ")
senha = input("Insira a senha de usuário: ")

while usuario == senha:
    print("ERRO!!! A senha de usuário não pode ser a mesma que o nome")
    usuario = input("Insira o nome de usuário: ")
    senha = input("Insira a senha de usuário: ")
