# Variable to use and declared the data

# Assiging mulltiple values in variables 

a,b,c=10,10.30,"Zeel"
print(f"The Variable of {a} {b} {c}")

print("\n---------------------------------------------------\n")

# Same value in multiple variables

a=b=c= 10
print(f"{a} {b} {c}")

print("\n---------------------------------------------------\n")

# DataTypes 

# 1.String 

name= "Zeel Panchal"
print(name)

print("\n---------------------------------------------------\n")

# Single Line & Multilines Strings {In using both single & double quotes}

n="Zeel"
n2=""" Zeel
       Panchal """
       
n3='Zeel'
n4='''Zeel
      panchal'''
      
print(f"Name of {n} , {n2} , {n3} , {n4}")

print("\n---------------------------------------------------\n")

# Sting print in slicing

name= "Zeel Panchal"
print(name)
print(name[0])
print(name[0:5])
print(name[6:])
print(name*2)

print("\n---------------------------------------------------\n")

# Check DataTypes using type()

a=10
b=10.50
c="Zeel-panchal"
d=1+2j

print("A Type is : ",type(a))
print("B Type is : ",type(b))
print("C Type is : ",type(c))
print("D Type is : ",type(d))

print("\n---------------------------------------------------\n")

# implicite type conversion
# In implicite method pyhton automaticlly convert data type to another,..
a=10
b=20.20
c=a+b

print("A Type is ",type(a), "Value is ",a)
print("A Type is ",type(b), "Value is ",b)
print("A Type is ",type(c), "Value is ",c)

# Explicite Type conversion 
# Tn this type user covert the data of the objects that reqiured data type 
# So we use built in function like int() , float() , str() ,etc

print("\n---------------------------------------------------\n")

x=int(2.8)
y=float(10)
z=str(2)

print(f"{x} {y} {z}")

print("\n---------------------------------------------------\n")

a=10
print(type(a))

a="10"
print(type(a))

b=int(a)
print(type(b))

print("\n---------------------------------------------------\n")


# Int and int type caste

a=10
b=int("10")
c=a+b
print(c)


print("\n---------------------------------------------------\n")

# Number to String conversion 

n1=10
n2=20.50
n3=10+5j

print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))
print(n1+n2)
print()

print("\n---------------------------------------------------\n")

n1=str(n1)
n2=str(n2)
n3=str(n3)

print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))
print(n1+n2)

print("\n---------------------------------------------------\n")

# List to tuple conversion

value=[10, 20, 30.5, "Hello", "World"]

print("List Values")
print(value)

print("\n---------------------------------------------------\n")

# list to tuple conversion 
ans=tuple(value)

print("Tuple values " )
print(ans)
print(type(ans))

print("\n---------------------------------------------------\n")

# Tuple to list conversion

value=(10,20,30.5,"Hello","World")

print("Tuple values ")
print(value)

print("\n---------------------------------------------------\n")

# Tuple to list conversion 

ans=list(value)

print("List values")
print(ans)
print(type(ans))

print("\n---------------------------------------------------\n")

# Dictionary to list / tuple conversion

mydata={1: 10, 20.5 : 100, 'key':"Hello"}
print(mydata)
print(type(mydata))
print()

print("\n---------------------------------------------------\n")

# Dictionary to list conversion

new_list1=list(mydata.values())
print(new_list1)
print(type(new_list1))
print()

print("\n---------------------------------------------------\n")

# Dictionary to tuple conversion
new_list2=tuple(mydata.values())
print(new_list2)
print(type(new_list2))
print()
