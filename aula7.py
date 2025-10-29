numero = input("Digite um número inteiro: ");

try:
    numero_int = int(numero.);
    par_ou_impar = numero_int % 2
    if par_ou_impar == 0:
        print("Seu número é par");
    else:
        print("Seu número é ímpar");
except:
    print("Caractere inválido, deve ser número inteiro (Maior que 0 e sem ponto flutuante)");