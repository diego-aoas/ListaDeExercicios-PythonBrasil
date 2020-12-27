"""
Faça um programa que pergunte o preço de três produtos
e informe qual produto você deve comprar, sabendo que a
decisão é sempre pelo mais barato.
"""

produto_1 = float(input("Informe o preço do produto 1: "))
produto_2 = float(input("Informe o preço do produto 2: "))
produto_3 = float(input("Informe o preço do produto 3: "))

if produto_1 < produto_2 and produto_1 < produto_3:
    print("Compre o produto 1 é o mais barato!")
elif produto_2 < produto_1 and produto_2 < produto_3:
    print("Compre o produto 2 é o mais barato!")
else:
    print("Compre o produto 3 é o mais barato!")
