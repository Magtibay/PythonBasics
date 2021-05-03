from student import Student

student1 = Student("John Wall", "Computer Science", 3.1, False)
student2 = Student("Ty", "Business", 3.6, True)

print(student1.gpa)
print(student2.gpa)

print(student1.on_honour_roll())
print(student2.on_honour_roll())