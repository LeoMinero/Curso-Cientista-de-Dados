# Calcular IMC

nome = 'Leonardo'
idade = 36
altura = 1.66
peso = 72
ano_atual = 2023
ano_nasc = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg')
print(f'O imc de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {ano_nasc}\n')

print(f'{nome} tem {idade} anos, {altura} de altura, pesa {peso}kg, é nascido em {ano_nasc} e seu imc é {imc:.2f}\n')
