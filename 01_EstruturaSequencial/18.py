"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e
a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
aproximado de download do arquivo usando este link (em minutos).
"""

tamanho = float(input("Forneça o tamanho do arquivo (em MB): "))
velocidade = float(input("Forneça a velocidade da internet (Mbps): "))

tempo_download = round ((tamanho / (velocidade / 8)) / 60, 2)

print(
    f"Um arquivo de {tamanho}MB, feito o download em uma conexão de {velocidade}Mbps será de {tempo_download} minutos")
