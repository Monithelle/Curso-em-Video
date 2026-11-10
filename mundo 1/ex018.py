#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
angle = float(input("Digite o valor do ângulo: "))
sine = math.sin(math.radians(angle))
cosine = math.cos(math.radians(angle))
tangent = math.tan(math.radians(angle))
print(f'O ângulo de {angle}° tem o SENO de {sine:.2f}')
print(f'O ângulo de {angle}° tem o COSSENO de {cosine:.2f}')
print(f'O ângulo de {angle}° tem a TANGENTE de {tangent:.2f}')
