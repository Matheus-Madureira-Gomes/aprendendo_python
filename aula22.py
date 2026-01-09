numero = int(input("Digite um número "))

def duplica (numero):
    numero_duplicado = numero * 2
    return print(f"O número duplicado é {numero_duplicado}")

def triplica (numero):
    numero_triplicado = numero * 3
    return print(f"O número triplicado é {numero_triplicado}")

def quadruplica (numero):
    numero_quadruplicado = numero * 4
    return print(f"O número quadruplicado é {numero_quadruplicado}")

duplica(numero), triplica(numero), quadruplica(numero)





def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
