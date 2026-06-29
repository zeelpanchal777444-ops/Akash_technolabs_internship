#  Simple calculator 

a=float(input())
b=float(input())

print("Addition /  Substraction /  Multiplication /  Division")

choice =int(input())

match choice:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        print(a/b)
    case _:
        print("Invalid choice")
        