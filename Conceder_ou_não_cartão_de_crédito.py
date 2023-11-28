"""
Algorítmo para conceder liberação de aquisição de cartão de crédito
com idade mínima de 22 anos e score mínimo de 600 pontos.
"""

nome = input('Qual nome do cliente? ')
idade = int(input('Qual a idade do cliente? '))
score = int(input('Qual o score do cliente? '))
idade_min = 22
score_min = score

if idade_min >= 22 and score_min >= 600:
    print(f'{nome} PODE adquirir um cartão de crédito!! ')
else:
    print(f'No momento {nome} NÃO PODE adquirir um cartão de crédito!! ')
