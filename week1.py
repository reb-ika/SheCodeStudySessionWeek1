class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade    
class StudentSystem:
    def __init__(self):
        self.students=[]
    def add_student(self,student):
        self.students.append(student)
    def remove_student(self,student):
        self.students.remove(student)
    def get_student(self,name):
        for student in self.students:
            if student.name==name:
                return student
        return None
    def get_all_students(self):
        return self.students
#example usage
student1=Student("John",15,"A")
student2=Student("Jane",16,"B")
student3=Student("Bob",17,"C")
system=StudentSystem()
system.add_student(student1)
system.add_student(student2)
system.add_student(student3)
print(system.get_all_students())
system.remove_student(student2)
print(system.get_all_students())
print(system.get_student("John"))
print(system.get_student("Jane"))
print(system.get_student("Bob"))
print(system.get_student("Alice"))