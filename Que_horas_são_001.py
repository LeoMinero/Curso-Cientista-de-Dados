"""
Faça um programa que pergunte a hora ao usuário e, baseando_se no horário descrito, 
exiba a saudação apropriada. Ex:
Bom dia 0 - 11. 
Boa tarde 12 - 17
Boa noite 18 - 23
"""""

horas = int(input('Que horas são?? '))

while horas:
    if horas <= 11:
        print('Bom dia!!')
        break

    elif horas <= 17:
        print('Boa tarde!!')
        break

    elif horas <= 23:
        print('Boa noite!!')
        break

    else:
        print('Hora inválida!! Digite um horário entre "0 e 23"!! ')

    horas = int(input('Que horas são?? '))
