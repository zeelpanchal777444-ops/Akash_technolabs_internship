# Average and Grade

n1=int(input("Enter the number : "))
n2=int(input("Enter the number : "))
n3=int(input("Enter the number : "))
n4=int(input("Enter the number : "))
n5=int(input("Enter the number : "))

ans=(n1+n2+n3+n4+n5)/5
print(f"The number is n1 {n1} \n n2 {n2} \n n3 {n3} \n n4 {n4} \n n5 {n5}")

print("The Total of the avg of sum is  : ",ans)

if ans < 50:
    print("Grade F")
elif ans <=50: 
    print("Grade D")
elif ans <=60:
    print("Grade C")
elif ans <=70:
    print("Grade B")
elif ans <=80:
    print("Grade A")
elif ans <=90:
    print("Grade A+")
else:
    print("Fail")