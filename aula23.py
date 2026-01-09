pessoa = {
    "nome": "Matheus",
    "sobrenome": "Madureira",
    "idade": 20,
    "Endereco":[
        {"rua": "rua_exemplo", "numero": "12"},
        {"rua": "rua_exemplo", "numero": "12"}
    ]
}

print(pessoa["nome"])

for chave in pessoa:
    print(chave, pessoa[chave], sep=": ")