# ---2D Grid--- (list inside list)
num_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(num_grid[0][0])
        #     ^   ^ 
        #  row  colume
# ---Nested Loops--- (loop inside loop)

for row in num_grid:# this loop passes through every loop in num grid. 
    for col in row:# this loop passes through evrry column in a row from first loop giving a number.
        print(col)

#---Try/Except---
try:
    # answer= 10/0
    number = int(input("Enter a number : "))
    print(number)
except ZeroDivisionError as  err :
    print(err)
except ValueError :
    print("invalid input")

#---Read/Write Files---

students = open("students","r")
for student in students.readlines():
    print(students)
students.close()

write = open("new_students","w")
write.write("Sayali - FE")
write.close()

#---Modules---
import Modules_example

print(Modules_example.roll_dice(10))
# modules are just pre-writen code so mod come pre-install 
# and meany others are found on websites like:Python docx

#---Class and Object---
from Class_student import Student

student1 = Student("Jim","FE",7.86,False)
student2 = Student("Pam","SE",6.34,True)
        #class(name,year,cgpa,is_on_probition)
print(student2.cgpa)

