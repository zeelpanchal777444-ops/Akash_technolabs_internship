# value take from user 

mydic={}

count=int(input("How many Records u want ? "))

for i in range(0,count):
    mykey=input("Enter key : ")
    mydic[mykey]=input("Enter the value : ")
    
print(mydic)
print("\n--------------------------------------\n")

# another method take value from user

mydic1={}

n=int(input("Enter no : "))
for i in range(n):
    k,v=input("Enter key value : - ").split()
    mydic1[k]=[v]
    
print(mydic1)
print("\n--------------------------------------\n")

# create dic using built in fun -dict()

print("create dic using built in fun -dict()")

mydic2=dict([(1,'raj') , (2,'me')])
print(mydic2)