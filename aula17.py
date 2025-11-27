x = input("Digite um valor para x: ")
y = input("Digite um valor para y: ")

def soma(x, y):
    try:
        x_int = int(x)
        y_int = int(y)
    except:
        print("Digite um número inteiro")
    soma = x_int + y_int
    print(soma)

soma(x, y)
