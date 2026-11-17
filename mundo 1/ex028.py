#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 10 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
number = randint(0, 10) #sorteio

print('Pensei em um número entre 0 e 10. Tente adivinhar...')

jogador = int(input('Qual é o seu palpite? ')) #palpite do jogador

if jogador ==number:
    
    print('Parabéns! Você acertou!')

else:
    
    print('Você errou! Eu pensei no número {} e não no {}!'.format(number, jogador))