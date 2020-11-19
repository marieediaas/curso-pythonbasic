#Aula de Programação Orientada a objetos. Ministrada por Juliana Ferreira, membra do PyLadies Brasil.
#Exercício 1:Doguinhos

'''
#criação da classe
class Pyladies:
    def __init__(self, nome_e,qtd_membras_e,tem_homens_e):    #e de entrada
        self.nome = nome_e                                    #atributo nome recebe a variável nome_e
        self.qtd_membros = qtd_membras_e
        self.tem_homens = tem_homens_e
        #print("Atributos foram armazenados")

    def Dar_curso(self):                                      #utiliza-se def para criar os métodos
        print("Para dar um curso você precisará de: ...")     #é necessário usar self como parâmetro

    def Apresenta_todas_inf   os(self):
        print(f"\n{self.nome}\n{self.qtd_membros}\n{self.tem_homens}")

pyladies_mt = Pyladies("PyLadies Mato Grosso",6,False)        #instanciando o objeto

pyladies_mt.Dar_curso()
pyladies_mt.Apresenta_todas_infos()

'''

class Doguinhos:
    def __init__(self,nome_e,peso_e,altura_e,raca_e):
        self.nome = nome_e
        self.peso = peso_e
        self.altura = altura_e
        self.raca = raca_e

    def Anda(self):
        print("O doguinho está andando...")

    def Come(self):
        print("O doguinho está comendo...")

    def Infos(self):
        print(f"\n{self.nome}\n{self.peso} Kg\n{self.altura} cm\n{self.raca}")

    def Late(self):
        print("AU, AU, AU!")

doguinho1 = Doguinhos("Ted",27,60,"Boxer")
doguinho2 = Doguinhos("Entropia",4,20,"Maltês")
doguinho3 = Doguinhos("Pluft",5,36,"Pinscher")

doguinho1.Infos()
doguinho1.Anda()
doguinho2.Infos()
doguinho2.Come()
doguinho3.Infos()
doguinho3.Late()




