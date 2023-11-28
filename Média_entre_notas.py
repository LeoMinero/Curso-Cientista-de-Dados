# Média entre notas usando while com o resultado da variável média

N1 = float(input("Digite o valor de N1: "))
N2 = float(input("Digite o valor de N2: "))
N3 = float(input("Digite o valor de N3: "))
media = (N1 + N2 + N3) / 3
print(f'O valor das médias entre as notas é: {media:.2f}')

while (media >= 7):
    print('Parabéns, você foi aprovado!!')
else:
    print('Você foi reprovado!! Não desista!! Tente outra vez!!')
