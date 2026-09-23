student_name = input("Enter Your Name")
gpa = float(input("Enter Your GPA"))
credit_hours = int(input("Enter Your Credit Hours"))

if gpa >=3.8 and credit_hours>=12:
    classification="Dean List"
elif gpa>=3.5 and credit_hours>=12:
    classification="Honor Roll"
elif gpa>=2.0:
    classification="Good Standing"
else:
    classification="Academic Probation"    
print(classification)