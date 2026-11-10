#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math
cateto1 = float(input("Digite o comprimento do primeiro cateto: "))
cateto2 = float(input("Digite o comprimento do segundo cateto: "))
# Calculando o comprimento da hipotenusa usando o Teorema de Pitágoras

hypotenuse = math.hypot(cateto1, cateto2)
print(f'O comprimento da hipotenusa é: {hypotenuse:.2f}')
