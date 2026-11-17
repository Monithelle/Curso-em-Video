#

number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))

if number1 > number2 and number1>number3:
    print("O maior número é: {}".format(number1))
elif number2 > number1 and number2 > number3:
    print("O maior número é: {}".format(number2))
else:
    print("O maior número é: {}".format(number3))