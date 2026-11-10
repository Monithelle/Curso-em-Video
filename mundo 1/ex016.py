#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
value = float(input("Digite um valor: "))
print(f'O valor digitado foi {value} e a sua porção inteira é {math.trunc(value)}.')
