#o asterisco diz que o argumento é um array de todos os argumentos que serão passados dentro da func
def print_people(*people):
    for person in people:
        print("This person is ", person)


print_people("Nick","Dan","Jack","King","Smiley")

def do_math(num1,num2):
    return num1+num2

sum = do_math(5,7)
print(sum)

