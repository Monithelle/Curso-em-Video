#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
wage = float(input("Qual o salário do funcionário? R$ "))
print(f'O funcionário que ganhava R$ {wage:.2f}, com um aumento de 15%, vai ganhar R$ {(wage + ((wage * 15 )/ 100)):.2f}.')
