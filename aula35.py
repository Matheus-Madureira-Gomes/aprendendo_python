def soma_duas_listas(list1, list2):
    intervalo = min(len(list1), len(list2))
    nova_lista = [ (list1[i] + list2[i]) for i in range(intervalo) ]
    return nova_lista

l1 = [1, 2, 3, 4, 5, 6]
l2= [ 1, 2, 3]
print(soma_duas_listas(l1, l2))aula