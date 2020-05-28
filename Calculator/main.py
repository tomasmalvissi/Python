print("Python Calculator")

active = True

def suma(x,y):
    res = x + y
    print(res)    

def resta(x,y):
    res = x - y
    print(res)

def multip(x,y):
    res = x * y
    print(res)

def div(x,y):
    res = x / y
    print(res)

def printear():
    print("Ingrese 1 si quiere ralizar una suma")
    print("Ingrese 2 si quiere ralizar una resta")
    print("Ingrese 3 si quiere ralizar una multiplicación")
    print("Ingrese 4 si quiere ralizar una división")
    print("Ingrese 9 si quiere salir")
    op = input("opcion... ")

printear()
op = input("opcion... ")
num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese un número: "))

while active:
    if op == "1":
        print("{} + {} = ".format(num1, num2,))
        suma(num1, num2)
        printear()
    elif op =="2":
        print("{} - {} = ".format(num1, num2))
        resta(num1,num2)
        printear()
    elif op =="3":
        print("{} * {} = ".format(num1, num2))
        multip(num1,num2)
        printear()
    elif op =="4":
        print("{} / {} = ".format(num1, num2))
        div(num1,num2)                 
        printear()
    elif op == "9":
        print("Finalizado con exito")    
    else:
        print("Seleccione una opcion valida")
