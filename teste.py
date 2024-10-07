from keras.datasets import mnist # type: ignore
(x_treino, y_treino),(x_teste, y_teste) = mnist.load_data()
aa = (9, 59, 599, 5999, 599999)
cont = 0
for aaa in aa:
    for i in y_treino[0:aaa]:
        if i == 0:
            cont += 1
    print(cont, aaa)