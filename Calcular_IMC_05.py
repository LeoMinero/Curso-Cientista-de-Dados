# Calcular IMC

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
ano_atual = int(input('Digite o ano atual: '))

ano_nasc = ano_atual - idade
imc = peso / (altura ** 2)

print(f'\n{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg')
print(f'O imc de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {ano_nasc}\n')

print(f'{nome} tem {idade} anos, {altura} de altura, pesa {peso}kg, é nascido em {ano_nasc} e'
  f'seu imc é {imc:.2f}\n')
