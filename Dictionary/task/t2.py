# Three number sorting ...

numbers=[]

for i in range(3):
    num=int(input(f"Enter the number {i+1} : "))
    numbers.append(num)
    
numbers.sort()
print(numbers)


numbers_tuple=tuple(numbers)
print("_____________________________")
print(numbers_tuple)
data={
    "Ascending Order " : numbers_tuple
}
print("___________Sorted numbers__________")
print(data)