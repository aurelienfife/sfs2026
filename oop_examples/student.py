# Create your own class
# Create student, with a name, subject, an age
# And a method "study" and a method "sleep"
class student:
    # The __init__ method is the "constructor"
    # Every method definition takes at least 1 
    # parameter: "self"
    def __init__(self, name, subject, age):
        self.name = name
        self.subject = subject
        self.age = age

    # The methods
    def study(self):
        print(self.name, "is studying.")

    def sleep(self):
        print(self.name, "is sleeping")

student_list = []

student_list.append(student("Dylan", "Cyber", 45))
student_list.append(student("Panashe", "Cyber", 36))

for s in student_list:
    print(s.name, "studies", s.subject)
    s.study()
    s.sleep()
