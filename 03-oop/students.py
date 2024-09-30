
class Student:
    def __init__(self) -> None:
        self.id = 0
        self.name = None
        self.major = None
        self.gpa = 0

    def __str__(self) -> str:
        return self.name + ", GPA:" + str(self.gpa)
    
    def set_gpa(self, value):
        if value >= 0 and value <= 4:
            self.gpa = value
        else:
            print("Error, invalid gpa")

    
class PhDStudent(Student):
    def __init__(self) -> None:
        super().__init__()
        self.thesis = "N/A" 

    def __str__(self) -> str:
        return super().__str__() + " Thesis: " + self.thesis





a = Student()
a.name = "George"
a.set_gpa(3.6)
a.gpa = 1000101

b = Student()
b.name = "Ahmad"
b.set_gpa(3.1)

c = PhDStudent()
c.name = "Mike"
c.thesis = "Social Networks in Society"

print(a)
print(b)
print(c)