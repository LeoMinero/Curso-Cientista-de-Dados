# Calcular IMC

nome = 'Leonardo'
idade = 36
altura = 1.66
peso = 72
imc = peso / (altura ** 2)
e_maior = idade > 18

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)

# Exercício
print(nome, 'tem', idade, 'anos de idade e seu imc é: %1.2f' % imc)
print(f'{nome} tem {idade} anos de idade e seu imc é: {imc:.2f}')
print('{} tem {} anos de idade e seu imc é: {:.2f}'. format(nome, idade, imc))
print('{0} tem {1} anos de idade e seu imc é: {2:.2f}'. format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu imc é: {im:.2f}'. format(n=nome, i=idade, im=imc))
