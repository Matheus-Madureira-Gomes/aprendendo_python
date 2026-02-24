@protected
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f"A {self.nome} já está filmando")
            return
        print(f"A {self.nome} está filmando...")
        self.filmando = True

    def parar_filmar(self):
        if self.filmando:
            print(f"A {self.nome} parou de filmar ")
            self.filmando = False

        print(f"A {self.nome} não está filmando")

    def fotografar(self):
        if not self.filmando:
            print(f"A {self.nome} está fotografando...")

        print(f"A {self.nome} não pode fotografar filmando")

c1 = Camera("Canon")
c2 = Camera("Samsung")

c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()

print()

c2.parar_filmar()
c2.filmar()
c2.filmar()
c2.fotografar()
c2.parar_filmar()
c2.fotografar()
