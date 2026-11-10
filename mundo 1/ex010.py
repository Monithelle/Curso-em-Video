#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
money = input('Quanto dinheiro você tem na carteira? R$ ')
dollar = float(money) / 5.20
print(f'Com R$ {money}, você pode comprar US$ {dollar:.2f}.')