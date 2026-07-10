# Take numbers based on number create n munber of files with content 

n=int(input("Enter number of files : "))

content = input("Enter content for files : ")

for i in range(1,n+1):
    filename = "File" + str(i) + ".txt"
    
    file = open(filename,"w")
    file.write(content)
    file.close()
    
print(n,"Files created successfully ! ")