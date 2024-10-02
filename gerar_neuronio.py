import random
import pickle
class Gerar_neuronio():
    def gerar_rede(num_camadas, num_nos, nome,  base = False):
        self.base = base
        self.nome = nome
        num_camadas += 2
        num_nos.insert(0, 784)
        num_nos.append(10)
        if base:
            self.escrever_rede_baseada()
        num_nos.reduce(self.escrever_rede, num_nos)
        
    def escrever_rede(self, x, y):
        array = [random.randint(-5, 5) for i in range(x*y)]
        with open(self.nome+".pkl", "wb") as arquivo:
	        pickle.dump(array, arquivo)       

    def escrever_rede_baseada(self, x, y):
        with open(self.base, "rb") as arquivo:
             lista = pickle.load(arquivo)
                   

        