"""
Algorítmo para criar usuário e senha.
"""

usuario = input('Digite um nome para usuário: ')
senha = input('Digite uma senha para o usuário: ')

usuario_bd = 'leonardo'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema!! ')
else:
    print('Usuário e senha inválidos!! ')
