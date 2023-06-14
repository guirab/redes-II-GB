import random
import time

class Transmissor:
    def __init__(self, id):
        self.id = id
        self.tempo_inicio_sensing = random.uniform(0.0, 2.0)
        self.duracao_sensing = random.uniform(0.5, 2.0)

    def verificar_meio(self):
        return random.choice([True, False])  # Simula o meio de transmissão ocupado ou livre

    def colisao_detectada(self):
        print(f"Colisão detectada no transmissor {self.id}")

    def backoff_algorithm(self, tentativa):
        espera = random.randint(0, (2 ** tentativa) - 1)
        print(f"Transmissor {self.id} esperando por {espera} segundos")
        time.sleep(espera)  # Espera um tempo exponencial truncado

    def transmitir(self, dados):
        # Espera o tempo de início do sensing
        time.sleep(self.tempo_inicio_sensing)
        print(f"Transmissor {self.id} começou o sensing")

        # Realiza o sensing por um tempo específico
        time.sleep(self.duracao_sensing)

        if self.verificar_meio():
            self.colisao_detectada()
            tentativa = 0

            while tentativa < 10:  # Limite máximo de tentativas
                self.backoff_algorithm(tentativa)
                if not self.verificar_meio():
                    break
                tentativa += 1
            else:
                print(f"Transmissor {self.id} não conseguiu transmitir após várias tentativas")
        else:
            print(f"Transmissor {self.id}, dados {dados} transmitidos com sucesso")

# Criando os transmissores
transmissor1 = Transmissor(1)
transmissor2 = Transmissor(2)

# Definindo os dados dos quadros
dados_transmissor1 = "batatinha"
dados_transmissor2 = "dj maiquinhos"

# Iniciando a simulação
transmissor1.transmitir(dados_transmissor1)
transmissor2.transmitir(dados_transmissor2)
