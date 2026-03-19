class A:
    inteiro = 5
    def metodo(self):
        print(A.inteiro)

class B(A):
    def metodo(self):
        print(A.inteiro)

class C(B):
    inteiro = 15
    def metodo(self):
        print("A")

c = C()