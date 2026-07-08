# The marksheet ,total, percentage = using list ,tuple, dic... 

marks=[]

for i in range(5):
    mark=int(input(f"Enter marks of Subject {i+1} : "))
    marks.append(mark)


marks_tuple=tuple(marks)

total=sum(marks_tuple)
percentage=total/len(marks_tuple)

if percentage>=90:
    grade = "A+"
elif percentage>=80:
    grade = "A"
elif percentage>=70:
    grade = "B"
elif percentage>=60:
    grade = "C"
elif percentage>=50:
    grade = "D"
else:
    grade = "Fail"
    
print()
print(marks)
    
result={
    "marks":marks_tuple,
    "Total":total,
    "Percentage":percentage,
    "Grade":grade
}
print()
print("______MARKSHEET______")
for key,value in result.items():
    print(key," : - ",value)