def append_on_list(lista, escolha):
    lista.append(escolha)

def see_list(lista):
    print("\n--- MINHA LISTA ---")
    if not lista:
        print("A lista está vazia.")
    for item in lista:
        print(item)
    print("-------------------\n")

def desfazer(lista, stack_list):
    if lista:
        last_item_removed = lista.pop() 
        stack_list.append(last_item_removed)
    else:
        print("Nada para desfazer.")

def refazer(lista, stack_list):
    if stack_list:
        last_item_recovered = stack_list.pop()
        lista.append(last_item_recovered)
    else:
        print("Nada para refazer.")

lista = []
stack_list = []

while True:
    print("Comandos: listar, desfazer, refazer")
    escolha = input("Digite uma tarefa ou comando: ").strip().lower()

    if escolha == 'listar':
        see_list(lista)
    
    elif escolha == 'desfazer':
        desfazer(lista, stack_list)
        see_list(lista)
    
    elif escolha == 'refazer':
        refazer(lista, stack_list)
        see_list(lista)
    
    else:
        append_on_list(lista, escolha)
        stack_list.clear()
