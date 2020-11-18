#Projeto 1: Calculadora
import re

print("CALCULADORA DA DISCÓRIDA")
print("por Marie Dias.\n")

print("Digite 'parar' para sair\n")
prev = 0
run = True


def performMath():
    global prev
    global run
    # Estamos modificando a variável run apenas dentro da função.
    # Se deixarmos assim, mesmo que o usuário escolha sair da calculadora, a execução não será finalizada,
    # pois fora da função a variável booleana run ainda recebe o valor True.
    # Assim, ao tornar run global, mesmo que a modifiquemos dentro da func, este valor será modif globalmente.

    equation = ""
    if prev == 0:
        equation = input("Digite a equação: ")
    else:
        equation = input(str(prev))


    if equation == 'parar':
        print("Tchau!")
        run= False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]','',equation)
        #a variável terá apenas valores que excluam os caracteres entre os colchetes
        #assim, previne-se algum erro que possa surgir pelo uso da built in eval

        if prev==0:
            prev = eval(equation)
            #evaluate permite que o programa execute um código python "dentro de si"
        else:
            prev = eval(str(prev) + equation)


while run:
    performMath()
