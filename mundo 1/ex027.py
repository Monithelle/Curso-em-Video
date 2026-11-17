#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
name = str(input('Digite o nome da pessoa: ')).strip()
print('O primeiro nome da pessoa é: {}'.format(name.split()[0]))
print('O último nome da pessoa é: {}'.format(name.split()[-1]))