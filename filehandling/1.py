# Take a file name and content add into file 

filename  = input("Enter file name : ")
content = input("Enter Content : ")

file = open(filename,"a")
file.write(content+"\n")
file.close()

print("Content added successfully ! ")