#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distance = float(input('Digite a distância da viagem em km: '))

if distance <= 200:
    price = distance * 0.50
else:
    price = distance * 0.45
    print('O preço da passagem é R${:.2f}'.format(price))
