class Carrinho:
    def __init__(self):
        self.produto = []

    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self.produto.append(produto)

    def soma(self):
        return sum([p.preco for p in self.produto])

    def listar_produtos(self):
         for produto in self.produto:
            print(produto.nome, produto.preco)

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
carrinho = Carrinho()
p1 = Produto("Copo Stanley", 50)
p2 = Produto("Lápis", 1.50)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.soma())