nome = 'Leonardo'
print(nome[3])
print(nome[-2])
print('n' in nome)
print('m' in nome)
print('Leo' in nome)
print(10 * '-')

print(nome[3])
print(nome[-2])
print('n' not in nome)
print('m' not in nome)
print('Leo' not in nome)

'''
Isso é apenas um comentário
Isso é apenas um comentário
Isso é apenas um comentário
'''

idade = input('Digite sua idade: ')
print(f'Sua idade é {idade: <1} anos.')

nota = input('Digite a nota final do aluno: ')
frequencia = input('Digite a frequência do aluno: ')

nota1 = float(nota)
frequencia1 = int(frequencia)
if nota1 >= 7 and frequencia1 > 70:
    print('Aprovado!!')
else:
    print('Reprovado')

# Novo if
if nota1 >= 7 or frequencia1 > 70:
    print('Aprovado!!')
else:
    print('Reprovado')

# If e elif
if nota1 <= 4:
    print('Reprovado!!')
elif nota1 > 4 and nota1 <= 6:
    print('Exame final')
else:
    print('Aprovado')
