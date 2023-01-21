

# parent class User
class User:
    email = ""
    password = ""

    def logIn(self):
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            # email and password must match in order to log in
            print("Welcome back!")
        else :
            print ("The email or password associated with this account is incorrect.")


# child class Teacher
class Teacher(User):
    teacher_id = "0"
    subject = "Math"

    def logIn(self):
        entry_id = input("Enter your Teacher ID: ")
        entry_password = input("Enter your password: ")
        if (entry_id == self.teacher_id and entry_password == self.password):
            # teachers will use their teacher id instead of email to log in to account
            print("Welcome back!")
        else :
            print("The ID or password associated with this account is incorrect.")


# child class Student
class Student(User):
    student_id = "1"
    grade_point_average = 3.75

    def logIn(self):
        entry_id = input("Enter your Student ID: ")
        entry_password = input("Enter your password: ")
        if (entry_id == self.student_id and entry_password == self.password):
            # students will use student id to log in to account
            print("Welcome back!")
        else :
            print("The ID or password associated with this account is incorrect.")

newUser = User()
newUser.logIn()

teacher = Teacher()
teacher.logIn()

student = Student()
student.logIn()
