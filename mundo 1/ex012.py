#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
price = float(input("Qual o preço do produto? R$ "))
print(f'O produto que custava R$ {price:.2f}, na promoção com desconto de 5% vai custar R$ {price - (price * 5 / 100):.2f}.')