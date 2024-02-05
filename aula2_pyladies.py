class Pyladies:
    def __init__(self, nome, qtd_membras, tem_homens):

        #Ao colocar __ na frente do atributo, estamos tornando-o privado,
        #ou seja, não se pode modificá-lo fora da classe
        self.__nome = nome
        self.__qtd_membras = qtd_membras
        self.__tem_homens = tem_homens


    def apres_as_infos(self):
        print(f"\nNome: {self.__nome}\nQuantidade de membras:"
              f" {self.__qtd_membras}\nTem homens: {self.__tem_homens}")


pyladies_mt = Pyladies("PyLadies Mato Grosso",6,False)


#Se tentarmos modificar os atributos fora da classe, não dará certo, pois eles estão privados
pyladies_mt.nome = "Super Maravilhosas"

pyladies_mt.apres_as_infos()

#Além disso, só conseguimos visualizar os atributos porque pedimos isso dentro da classe
#com a função apres_as_infos. Se pedíssemos fora, não daria certo
#O encapsulamento de atributos e métodos evitam o vazamento do seu escopo
#A leitura e alteração de um atributo encapsulado podem ser feitas através de getters (função get()) e setters (função set())
#Parei no 14:05