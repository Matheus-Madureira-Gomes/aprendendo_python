def multiplicar (*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(1, 3)
print(multiplicacao)

def par_ou_impar (multiplicacao):
    if multiplicacao % 2 == 0:
        return print(f"A multiplicação dos números é Par. ")
    else:
        return print(f"A multiplicação dos números é Ímpar. ")
par_ou_impar(multiplicacao)