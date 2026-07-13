# Maximum and minimum 

import array as arr 

arrdata = arr.array("i",[])
n=int(input("Enter the number of element : "))

for i in range(n):
    n1=int(input("Enter the value : "))
    arrdata.append(n1)
    
print(arrdata)

max_n =arrdata[0]
min_n =arrdata[0]

for i in arrdata:
    if i > max_n:
        max_n = i
        
    if i < min_n:
        min_n = i

print("Maximum : ",max_n)
print("Minimum : ",min_n)