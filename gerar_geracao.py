import os
import gerar_neuronio
import shutil
class Geracao:
    def __init__(self, num_individuos, num_gen, num_nos, cont_levels, individuo_base):
        nova_pasta = "geracao %s"%str(num_gen)
        os.makedirs(nova_pasta)
        for i in range(0, num_individuos):
            if i == 0:
                shutil.copy(individuo_base, nova_pasta+"/ind_0.pkl")
                continue
            individuo = gerar_neuronio.Gerar(num_nos, str('ind_'+str(i)), nova_pasta, num_gen,cont_levels, individuo_base)
