# Cálcular distância a percorrer

distancia = float(input('Digite qual distância irá percorrer: '))
velocidade = float(input('Digite a velocidade média que irá dirigir: '))
tempo = distancia / velocidade * 60
print('O tempo estimado é: %1.0f' %(tempo), 'minutos')
