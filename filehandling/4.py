# take marks and subject from user and create file and write using filehandling concept 

n=int(input("Enter the number of subjects : "))

file = open("marks.txt","w")

for i in range(1, n+1):
    subject = input("\nEnter subject Name : ")
    marks = input("Enter the marks : ")
    
    file.write("Subject : "+ subject + "\n")
    file.write("Marks : "+ marks + "\n\n")

file.close()

file = open("marks.txt","r")

print("\n -- student Marks -- \n\n")
print(file.read())


file.close()

