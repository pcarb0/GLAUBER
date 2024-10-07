import os
import pickle

class Pegar():
    def __init__(self, num_gen, lista_de_teste, lista_de_resposta, num_nos):
        num_nos.append(2)
        caminho_pasta = 'geracao '+str(num_gen)
        itens = os.listdir(caminho_pasta)
        self.resultados = {}
        for individuo in itens:
            acertos = 0
            for numero33 in range(len(lista_de_resposta)):
                if lista_de_resposta[numero33] != 0:
                    continue
                numero = lista_de_teste[numero33]
                with open(caminho_pasta + '/' +individuo, "rb") as arquivo:
                    real_individuo = pickle.load(arquivo)
                real_numero = []

                for lista_numero in numero:
                    for i in lista_numero:
                        real_numero.append(i/255)

                matriz_final = []
                lista_matriz = []

                for elem_individuo in real_individuo[0]:
                    for i in real_numero:
                        lista_matriz.append(i*elem_individuo)

                lista_matriz = Pegar.agrupar_matriz(lista_matriz, num_nos[0])
                matriz_final.append(lista_matriz)      

                for i in range(1, len(real_individuo)):
                    lista_matriz = []
                    for ii in real_individuo[i]:
                        for iii in matriz_final[i-1]:
                            lista_matriz.append(ii*iii)
                    lista_matriz = Pegar.agrupar_matriz(lista_matriz, num_nos[i])
                    matriz_final.append(lista_matriz)

                bigclock = matriz_final[-1]

                resposta = bigclock.index(max(bigclock))
                if resposta == 0:
                    acertos += 1
            self.resultados.setdefault(individuo, acertos)

    def agrupar_matriz(matriz, n):
        matriz2 = [0] * n
        for i in range(n):
            for ii in range(i, len(matriz), n):
                matriz2[i] += matriz[ii]
        return matriz2
        


                        