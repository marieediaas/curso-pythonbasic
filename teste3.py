
#if statements
check = "Yo"

if check==False:
    print("It is false")
elif check == "Hamburguer":
    print("Yummm, hamburguer")
elif check == "Yo":
    print("Hey")
else:
    print("It is actually true")



#for/while loops

numbers=['Marie',"Iasmin","Sílvia","Neto"]

for item in numbers:
    print(item)

run = True
current = 1

while run:
    if current == 100 :
        run = False
    else:
        print(current)
        current += 1
