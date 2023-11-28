# Exiba na saída o valor maior que ou valor menor que dependendo de quem vem primeiro na escolha do usuário.

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'O primeiro valor = {primeiro_valor} é maior do que o segundo valor = {segundo_valor}')
else:
    print(f'O segundo valor = {segundo_valor} é maior que o primeiro valor = {primeiro_valor}')

"""""""""
primeiro_valor1 = int(primeiro_valor)
segundo_valor2 = int(segundo_valor)

if primeiro_valor1 > segundo_valor2:
    print(f'O primeiro valor = {primeiro_valor1} é maior do que o segundo valor = {segundo_valor2}')
else:
    print(f'O segundo valor = {segundo_valor2} é maior que o primeiro valor = {primeiro_valor1}')
"""""""""