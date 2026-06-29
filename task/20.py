# Gretest number of using =nested if 

a=int(input())
b=int(input())
c=int(input())

if a>b:
    if a>c:
        print("The no : ",a)
    else:
        print("The no : ",c)
else:
    if b>c:
        print("The no : ",b)
    else:
        print("The no : ",c)
    