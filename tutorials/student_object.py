class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.id = student_id

    def change_id(self, new_student_id):
        self.id = new_student_id

    def print(self):
        print("{} - {}".format(self.name, self.id))


name = input("What's your name? ")
student_id = input("What is your current student ID? ")
student = Student(name, student_id)
student.print()

change = input("Do you want to change your student ID? (Yes/No) ")

if change == "Yes":
    student.change_id(input("Enter your new student ID: "))
    student.print()
    print("Congrats! You have changed your student ID successfully.")
else:
    print("Well, you can continue using your current student ID.")
