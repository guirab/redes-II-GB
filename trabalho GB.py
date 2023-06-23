import random
import time
import threading

class Canal:
    def __init__(self):
        self.ocupado = False
        self.lock = threading.Lock()

    def verificar_meio(self):
        with self.lock:
            return self.ocupado

    def ocupar(self):
        with self.lock:
            self.ocupado = True

    def desocupar(self):
        with self.lock:
            self.ocupado = False

class Transmissor(threading.Thread):
    def __init__(self, id, canal, tamanho):
        super().__init__()
        self.id = id
        self.colisoes = 0
        self.canal = canal
        self.tamanho = tamanho

    def backoff(self):
        espera = random.randint(0, (2 ** self.colisoes) - 1)
        print(f'Transmissor {self.id}: meio ocupado. Realizando backoff. Esperando {espera} segundos.')
        time.sleep(espera)

    def transmitir(self):
        while True:
            if self.canal.verificar_meio():
                self.colisoes += 1
                self.backoff()
            else:
                self.canal.ocupar()
                print(f'Transmissor {self.id}: meio livre. Enviando dados. Tempo de transmissão: {self.tamanho} segundos.')
                time.sleep(self.tamanho)
                print(f'Transmissor {self.id}: dados enviados com sucesso.')
                self.canal.desocupar()
                break

    def run(self):
        self.transmitir()

canal = Canal()
transmissor1 = Transmissor(1, canal, 10)
transmissor2 = Transmissor(2, canal, 15)
transmissor3 = Transmissor(3, canal, 10)
transmissor4 = Transmissor(4, canal, 10)

transmissor1.start()
transmissor2.start()
transmissor3.start()
transmissor4.start()

transmissor1.join()
transmissor2.join()
transmissor3.join()
transmissor4.join()
