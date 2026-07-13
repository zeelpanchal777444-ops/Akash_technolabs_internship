# User input for array

import array as arr

arrdata = arr.array("i",[])

n=int(input("Enter the values of element : "))

for i in range(n):
    n1=int(input("Enter the value : "))
    arrdata.append(n1)
    
print(arrdata)

print(type(arrdata))