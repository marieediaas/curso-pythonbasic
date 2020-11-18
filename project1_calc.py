#Projeto 1: Calculadora
import re

print("CALCULADORA DA DISCÓRIDA")
print("por Marie Dias.\n")

print("Digite 'parar' para sair\n")
prev = 0
run = True


def performMath():
    global run
    # Estamos modificando a variável run apenas dentro da função.
    # Se deixarmos assim, mesmo que o usuário escolha sair da calculadora, a execução não será finalizada,
    # pois fora da função a variável booleana run ainda recebe o valor True.
    # Assim, ao tornar run global, mesmo que a modifiquemos dentro da func, este valor será modif globalmente.
    
    equation = input("Digite a equação: ")
    if equation == 'parar':
        run= False
    else:
        equation = re.sub('[a-zA-Z,.:() + " "]','',equation)
        #a variável terá apenas valores que excluam os caracteres entre os colchetes
        prev = equation
        print("Você digitou:", prev)


while run:
    performMath()
