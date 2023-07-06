class Student:
    def __init__(self,name:str,age:int,grades:iter):
        self.name = name
        self.age = age
        self.grades = list(grades)

    def calculate_scholadship(self) -> float:
        return sum(self.grades) / len(self.grades) * 17

    def add_grades(self,grade:int):
        self.grades.append(grade)

    def clear_grades(self,grade:int):
        self.grades.clear()


ruslan = Student('ruslan',19,[5,4,5,4,4])
print(ruslan.calculate_scholadship())
print('hehehehehehehehehehehehehehehehehehehehehehehehhehehehehehehehehehe')







