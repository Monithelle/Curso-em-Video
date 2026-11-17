#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

speed = float(input('Qual a velocidade do carro? '))

if speed > 80:
    print('Você ultrapassou o limite de velocidade! MULTADO!')
    multa = (speed - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))

else:
    print('Você está dentro do limite de velocidade. Tenha um bom dia!')
