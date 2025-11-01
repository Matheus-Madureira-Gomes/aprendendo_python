nome = "Matheus Madureira";
string = "";
tamanho_nome = len(nome);
indice = 0;

while indice < tamanho_nome:
    novo_nome = f"*{nome[indice]}";
    indice += 1;
    string += novo_nome;

print(string)

