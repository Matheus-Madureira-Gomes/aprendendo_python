from time import sleep
from threading import Thread


class MeuThread(Thread):
    def __init__(self, texto: str, tempo: int):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)

t1 = MeuThread('Hello, world', 5)
t1.start()
for i in range(10):
    print(i)
    sleep(1)

'''
def vai_demorar(texto: str, tempo: int):
    sleep(tempo)
    print(texto)

t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 5))
t1.start()
'''





