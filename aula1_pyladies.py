#Aula de Programação Orientada a objetos. Ministrada por Juliana Ferreira, membra do PyLadies Brasil.
#Adicionando métodos


#criação da classe
class Pyladies:
    def __init__(self, nome_e,qtd_membras_e,tem_homens_e):    #e de entrada
        self.nome = nome_e                                    #atributo nome recebe a variável nome_e
        self.qtd_membros = qtd_membras_e
        self.tem_homens = tem_homens_e
        #print("Atributos foram armazenados")

    def Dar_curso(self):                                      #utiliza-se def para criar os métodos
        print("Para dar um curso você precisará de: ...")     #é necessário usar self como parâmetro

    def Apresenta_todas_infos(self):
        print(f"\n{self.nome}\n{self.qtd_membros}\n{self.tem_homens}")

pyladies_mt = Pyladies("PyLadies Mato Grosso",6,False)        #instanciando o objeto

pyladies_mt.Dar_curso()
pyladies_mt.Apresenta_todas_infos()






