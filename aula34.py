def zipper(l1, l2):
    intervalo = min(len(l1), len(l2))
    return [
        (l1[i], l2[i]) for i in range(intervalo)
    ]


list1 = ["Salvador", "Belo Horizonte", "São Paulo"]
list2 = ["BA", "MG", "SP", "Rj"]
print(zipper(list1, list2))
        