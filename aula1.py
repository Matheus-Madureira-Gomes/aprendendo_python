peso = int(input("Qual seu peso em kg ?"));
altura = float(input('Qual sua altura em metros ?'));

imc = peso / (altura * altura);

if imc >= 40:
    print("Você está em Obesidade grau III");
elif imc >= 35:
    print("Você está em Obesidade grau II");
elif imc >= 30:
    print("Você está em Obesidade grau I");
elif imc >= 25:
    print("Você está em Sobrepeso");
elif imc >= 18.5:
    print("Você está no peso ideal");
else:
    print(f"Você está em Magreza {imc}");

