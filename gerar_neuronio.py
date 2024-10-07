import random
import pickle
class Gerar():
    def __init__(self, num_nos, nome, local, gen, level, base = False):
        self.gen = gen
        self.faixa = 5
        if level <= 1:
            self.faixa = 1000
        num_nos1 = num_nos.copy()
        num_camadas = len(num_nos1)
        self.local = local
        self.base = base
        self.nome = nome
        num_camadas += 2
        self.num_camadas = num_camadas
        num_nos1.insert(0, 784)
        num_nos1.append(2)
        self.num_nos1 = num_nos1
        if base:
            self.escrever_rede_baseada()
        else:
            self.escrever_rede()
               

    def escrever_rede_baseada(self):
        with open(self.base, "rb") as arquivo:
             lista_base = pickle.load(arquivo)
        nova_lista = []
        for i in lista_base:
            nova_lista2 = []
            for ii in i:
                iii = random.randint(ii-self.faixa, ii+self.faixa)
                nova_lista2.append(iii)
            nova_lista.append(nova_lista2)
        with open(self.local+"/"+self.nome+".pkl", "wb") as arquivo2:
            pickle.dump(nova_lista, arquivo2)
                               
def escrever_rede(num_camadas, nome, num_nos):
    lista2 = []
    num_nos1 = num_nos.copy()
    num_nos1.insert(0, 784)
    num_nos1.append(2)
    num_camadas += 2
    for i in range(0, num_camadas-1):
        lista1 = [random.randint(-5, 5) for ii in range(num_nos1[i]*num_nos1[i+1])]
        lista2.append(lista1)
    with open(nome+".pkl", "wb") as arquivo:
        pickle.dump(lista2, arquivo)
        