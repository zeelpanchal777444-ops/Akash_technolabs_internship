# Take 5 numbers from user in array and print data in asc and desc order

import array as arr 

arrdata = arr.array("i",[])
n=int(input("Enter the number of element : "))

for i in range(n):
    n1=int(input("Enter the value : "))
    arrdata.append(n1)
    
print(arrdata)

asc = arrdata[:]
for i in range(n):
    for j in range(i+1,n):
        if asc[i] > asc[j]:
            temp = asc[i]
            asc[i]=asc[j]
            asc[j]=temp
print("Ascending Order : ",asc)


for i in range(n):
    for j in range(i+1,n):
        if asc[i] < asc[j]:
            temp = asc[i]
            asc[i] = asc[j]
            asc[j] = temp
            
print("Descending Order : ",asc)
