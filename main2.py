import melhor_da_geracao
import gerar_geracao
import gerar_neuronio
import os
import shutil
from keras.datasets import mnist # type: ignore
(x_treino, y_treino),(x_teste, y_teste) = mnist.load_data()
x_treino = list(x_treino)

contador = 0

num_ind = 10 #int(input("número de individuos por geração: "))
num_cam = 2 #int(input("número de camadas internas: "))
num_nos = [40, 20]
"""for i in range(num_cam):
    ii = int(input("número de nós na camada %i: "%i))
    num_nos.append(ii)"""
config = (num_ind, num_nos)

levels = (9, 59, 599, 5999, 59999)
cont_levels = 0

while True:
    contador += 1
    if contador == 1:
        gerar_neuronio.escrever_rede(num_cam, 'inicial', config[1])
        melhor_individuo = 'inicial.pkl'
    if contador > 1:
        melhor_individuo = 'geracao %i/'%(contador-1) + melhor_individuo
    gerar_geracao.Geracao(config[0], contador, config[1],cont_levels, melhor_individuo)
    aaa = melhor_da_geracao.Pegar(contador, x_treino[0:levels[cont_levels]], y_treino[0:levels[cont_levels]], config[1])
    print(aaa.resultados)
    print("Level :", cont_levels)
    if aaa.resultados[max(aaa.resultados, key=aaa.resultados.get)] == (1,6,64,651,6520)[cont_levels]:
        cont_levels += 1
        print("passou de nivel")
        if aaa.resultados[max(aaa.resultados, key=aaa.resultados.get)] > 6579:
            print("treinamento concluido com sucesso")
            break
    if cont_levels > len(levels)-1:
        cont_levels -= 1
    melhor_individuo = max(aaa.resultados, key=aaa.resultados.get)
    if contador > 1:
        shutil.rmtree("/home/pedro/Documentos/GitHub/GLAUBER/geracao %i"%(contador-1))

