#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
temperature = float(input("Informe a temperatura em °C: "))
fahrenheit = (temperature * 9/5) + 32
kelvin = temperature + 273.15
print(f'A temperatura de {temperature:.1f}°C corresponde a {fahrenheit:.1f}°F e {kelvin:.2f}K.')

