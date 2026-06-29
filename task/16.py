# Maximuum number of three numbers = without using the nested if /logical operators 

a=int(input())
b=int(input())
c=int(input())

max_num=a

if b>max_num:
    max_num=b
if c>max_num:
    max_num=c

print("Maximum number is : ",max_num)