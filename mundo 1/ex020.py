# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

student1 = input("Digite o nome do primeiro aluno: ")
student2 = input("Digite o nome do segundo aluno: ")
student3 = input("Digite o nome do terceiro aluno: ")
student4 = input("Digite o nome do quarto aluno: ")
students = [student1, student2, student3, student4]
random.shuffle(students)
print("A ordem de apresentação é:")
print(students)