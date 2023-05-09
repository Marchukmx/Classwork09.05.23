#Симулятор навчального закладу (база даних)
class School:
     def __init__(self, name, students):
        self.name = name
        self.students = students #Список студентів
     def admit_student(self, student):
        self.students.append(student)
        print(f'{student.name} був додани до школи {self.name}') #Дописати, коли створено клас студентів
class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    def promote(self):
        self.grade += 1
        print(f"{self.name} був підвищений до рангу {self.grade}")
    def demote(self):
        self.grade -= 1
        print(f"{self.name} був понижений до рангу {self.grade}")
    def __str__(self):
        return f"{self.name} - Ранг {self.grade}"