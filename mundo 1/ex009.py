#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
multiplication_table = int(input("Digite um número para ver sua tabuada: "))
for i in range(1, 11):
    print("{} x {} = {}".format(multiplication_table, i, multiplication_table * i))
    