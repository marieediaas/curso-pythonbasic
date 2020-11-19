#Aula de Programação Orientada a objetos. Ministrada por Juliana Ferreira, membra do PyLadies Brasil.
#Adicionando atributos

#criação da classe
class Pyladies:
    def __init__(self, nome_e, qtd_membros_e,tem_homens_e):    #e de entrada
        self.nome = nome_e #atributo nome recebe a variável nome_e
        self.qtd_membros = qtd_membros_e
        self.tem_homens = tem_homens_e
        print("Atributos foram armazenados")

pyladies_mt = Pyladies("PyLadies Mato Grosso",6,False)

print('\n', pyladies_mt.nome)
print('\n',pyladies_mt.qtd_membros)
print('\n',pyladies_mt.tem_homens)



