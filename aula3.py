num1 = 0
num2 = 1
n = int(input("Quantos números da sequência de Fibonacci você quer? "))

contador = 0

while contador < n:
    print(num1)
    resultado = num1 + num2
    num1 = num2
    num2 = resultado
    contador += 1
