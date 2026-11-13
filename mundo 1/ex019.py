#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
name1 = str(input("Digite o nome do primeiro aluno: "))
name2 = str(input("Digite o nome do segundo aluno: "))
name3 = str(input("Digite o nome do terceiro aluno: "))
name4 = str(input("Digite o nome do quarto aluno: "))
students = [name1, name2, name3, name4]
chosen = random.choice(students)
print(f"O aluno escolhido foi: {chosen}")
