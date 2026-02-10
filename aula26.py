perguntas = [
    {
        "Pergunta": "Quanto é 5 + 5",
        "Opções": ['4', '6', '8', '10'],
        "Resposta": '10'
    },
    {
        "Pergunta": "Quanto é 30 / 5",
        "Opções": ['4', '6', '8', '10'],
        "Resposta": '6'
    },
    {
        "Pergunta": "Quanto é 15 + 5",
        "Opções": ['10', '12', '15', '20'],
        "Resposta": '20'
    },
]
contador_acertos = 0
for pergunta in perguntas:
    print(pergunta["Pergunta"])

    for indice, opcao in enumerate(pergunta["Opções"], start=1):
        print(f"{indice}) {opcao}")
        
    resposta = int(input("Escolha uma opção "))
    resposta_escolhida = pergunta["Opções"][resposta - 1]

    if resposta_escolhida == pergunta["Resposta"]:
            print("Você acertou!!")
            contador_acertos += 1
    else:
            print("Você errou !")
        
print(f"Você acertou {contador_acertos} questões")        

    


