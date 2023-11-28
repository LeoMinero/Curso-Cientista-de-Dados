"""
Faça um programa que peça para o usuário digitar um número inteiro e informe se o número
é par ou ímpar. Caso o usuário digite um número que não é inteiro, informe que não é um
número inteiro.
"""""
try:
    num = input('Digite um número inteiro: ')

    if not num.isdigit():
        print('Este não é um número inteiro')

    else:
        num = int(num)

    if num % 2 == 0:
        print('Este número é par!! ')

    else:
        print('Este número é ímpar!! ')

except:
    print('Tente outra vez!!')
