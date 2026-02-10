pessoa = { "nome": "matheus", "idade": 20 }

# Usamos kwargs para receber argumentos nomeados
def mostrar_chaves(**kwargs):
    # kwargs é um dicionário, então iteramos sobre suas chaves
    for chave, valor in kwargs.items():
        print(chave, valor)

# Usamos ** para desempacotar o dicionário ao chamar a função
mostrar_chaves(**pessoa)