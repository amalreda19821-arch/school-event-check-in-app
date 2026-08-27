#School Event Check-in App

#shows a short welcome message
print("Welcome to school event for 2026")

#make the first letter of the student name capital
def clean_name(name):
    student = name.title()
    return student

#making a for loop for 4 student
for i in range(4):
    student_name = input("Enter your name: ")
    student_grade = input("Enter your grade: ")

#print the name of each student by capital letter
    cleanStudent_name = clean_name(student_name)
    print(cleanStudent_name)

#making the id for each student

    student_id = student_name[:3].upper() + student_grade
    print("your id is " + student_id)
    
    
#making the group for each student

#the coonditional for the group of each student
    if int(student_grade) <= 8:
        group = "Junior Group"
    elif int(student_grade) > 8:
        group = "Senior Group"

    print("your group is " + group)
    print(".........__________.........")
    
print("Check-in complete")
