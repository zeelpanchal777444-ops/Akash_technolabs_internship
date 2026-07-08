# Using loop 

my_dic={1:'Mango' , 2:'Banana' , 3:'Orange' , 4:'Cherry'}

for x in my_dic:
    print("Key is - ", x ,"Value is - ",my_dic[x])
    
print("\n--------------------------------------\n")
    
# Use the for loop along with the items() method

print("using items() method ")

for x in my_dic.items():
    print(x)
    print()
print("\n--------------------------------------\n")
    
# key and value method 
for x in my_dic.keys():
    print(x)
    print()
    
for x in my_dic.values():
    print(x)
    print()

