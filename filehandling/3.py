# Take name , email , moblie , address of 5 users and store in textfile

n = int(input("Enter number of users: "))

file = open("users.txt", "w")

for i in range(1,n+1):
    print("Enter details of user",i)
    
    name = input("Enter name : ")
    email = input("Enter email : ")
    mobile = input("Enter mobile : ")
    address = input("Enter address : ")
    
    file.write("user : - " + str(i) + "\n")
    file.write("user : - " + name + "\n")
    file.write("user : - " + email + "\n")
    file.write("user : - " + mobile + "\n")
    file.write("user : - " + address + "\n")
    
file.close()
    
print("Data stored successfully ! ")
    