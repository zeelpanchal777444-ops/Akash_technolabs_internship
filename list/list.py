# List print

print("List print")
mylist1=[10,20,30,40,50,60,70,80]
mylist2=[10,"c",99,25.50,"PHP"]

print(mylist1)
print(mylist2)

print("\n.........................................................\n")

# positive and negative index

print("positive and negative index")
print(mylist1[1])
print(mylist2[-1])

print("\n.........................................................\n")

# print list using slice 

print("print list using slice ")
print(mylist1[2:5])
print(mylist1[2:4:5])
print(mylist1[3:])

print("\n.........................................................\n")

# list modify

print("list modify")
mylist1[0]=5
print(mylist1)

print("\n.........................................................\n")

# Length

print("Length")
print(len(mylist1))

print("\n.........................................................\n")

# List operations + *

print("List Operations (+ , *)")
concat_list=mylist1+mylist2
print(concat_list)

print("\n.........................................................\n")

print(mylist1*2)