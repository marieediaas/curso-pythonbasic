def my_function(str1,str2):
    print(str1)
    print(str2)


my_function("This is argument one.","This is argument two.")
my_function("Soup.", "Rice.")

def my_function_something(name = "Someone",age="Unknown"):
    #print("My name is " + name + "and my age is" + str(age))
    #Foi preciso converter age em string porque acima estamos concatenando vários tipos em uma só string
    print("My name is ", name, "and my age is", age)

my_function_something() #Se nenhum argumento é passado, ele imprime os valores defaults passado na função
my_function_something("Nick",27) #Quando passamos valores para as variáveis da função, estes são priorizados
my_function_something(age=27)
my_function_something(None,27) #None é uma palavra-chave que pode substituir o primeiro argumento
my_function_something(27) #Nesse caso ele vai usar o valor passado como argumento para subst. a primeira var da func
my_function_something(age= 27, name="Nick") #utilizando palavras-chave podemos mudar a ordem em que apresentamos os valores das variáveis


