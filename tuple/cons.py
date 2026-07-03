# list convert into tuple 

mylist=[]
n=int(input("Enter number of element : "))

for i in range(0,n):
    myvalue=input("Enter the value : ")
    # Append 
    
    mylist.append(myvalue)
    print(mylist)
    print()
    
print("..........................................\n")
    
print("Convert the list into tuple\n")
    
mytuple=tuple(mylist)
print(mytuple)