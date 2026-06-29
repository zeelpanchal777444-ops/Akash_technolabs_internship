# 1. calculate area of rec  L*B

L=int(input("Enter the number : "))
B=int(input("Enter the number : "))

print(f"No 1 is : {L} \n No 2 is {B}")

rec= L * B
print(f"Area of  Rectangle : {rec}")

print("\n...............................................\n")

# 2.Calculate area of a square

L=int(input("Enter the number : "))
print(f"The number is : {L}")

s=L*L
print("Area of square : ",s)

print("\n...............................................\n")

# 3.Calculate area of a circle 

pi=3.14
r=int(input("Enter the number : "))
print(f"The number is : {r}")

c=pi*r*r
print("Area of circle : ",c)

print("\n...............................................\n")

# 4.Calculate avareage of 5 

n1=int(input("Enter the number : "))
n2=int(input("Enter the number : "))
n3=int(input("Enter the number : "))
n4=int(input("Enter the number : "))
n5=int(input("Enter the number : "))

ans=(n1+n2+n3+n4+n5)/5
print(f"The number is n1 {n1} \n n2 {n2} \n n3 {n3} \n n4 {n4} \n n5 {n5}")

print("The Total of the avg of sum is  : ",ans)

print("\n...............................................\n")

# 5.Calculate simple interest 

p=int(input("Enter the number : "))
r=int(input("Enter the number : "))
t=int(input("Enter the number : "))

print(f"The no of P is {p} \n R is {r} \n T is {t}")

i=(p*r*t)/100

print("\n The simple_interest is : ",i)

# 6.Take 3 numbers and find square and cubes 

a=int(input("Enter no 1 : "))
b=int(input("Enter no 2 : "))
c=int(input("Enter no 3 : "))

print(f"\nThe no 1 is {a} no 2 is {b} no 3 is {c}")

ans1=a*a
ans2=a*a*a

ans3=b*b
ans4=b*b*b

ans5=c*c
ans6=c*c*c

print(f" no a sqr : {ans1}\n no b cube : {ans2}\n no b sqr :  {ans3}\n no b cube : {ans4}\n no c sqr :  {ans5}\n no c cube : {ans6}")

print("\n...............................................\n")

# 7.Enter the temperature in fahrenheit and convert in it to celsius 

F=int(input("Enter the temperature :"))

C=((F-32)*5)/9
print("The temperature convert into celsius",C)

print("\n...............................................\n")

# 8.Odd or Even

a=int(input("Enter the no : "))

if(a%2==0):
    print("The no is even")
else:
    print("The no is odd")
    
print("\n...............................................\n")

# 9.leap year or not 

year=2024

if(year%4==0 and year%100!=0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")

print("\n...............................................\n") 

#10.smallest number using coditional opeartor 

a=int(input("Enter no 1 : "))
b=int(input("Enter no 2 : "))

if a < b and a > b:
    print("The no is small",a)
else:
    print("The no is small",b)



