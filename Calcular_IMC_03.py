"""
* Criar variáveis para nome (str), idade (int)
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento de uma pessoa (baseado na idade e no ano atual)
* Obter o imc da pessoa com 2  casas decimais (no peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""""

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
ano_atual = int(input('Digite o ano atual: '))

ano_nasc = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, é nascido em {ano_nasc} e seu imc é {imc:.2f}')
