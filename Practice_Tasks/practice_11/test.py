class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if course in self.courses_attached:
            if course in self.grades:
                self.grades[course][student] = grade
            else:
                self.grades[course] = {student: grade}

class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if course in student.courses_in_progress and course in self.courses_attached:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]

student1 = Student("Денис", "Степанов", "Мужской")
reviewer1 = Reviewer("Алиса", "Чернявская")
lecturer1 = Mentor("Андрей", "Ушаков")

student1.courses_in_progress.append("Информатика")

reviewer1.courses_attached.append("Информатика")
lecturer1.courses_attached.append("Информатика")

reviewer1.rate_student(student1, "Информатика", 5)
reviewer1.rate_student(student1, "Информатика", 9)

student1.rate_lecturer(lecturer1, "Информатика", 9)

print(reviewer1.name,reviewer1.surname,student1.grades)
print(lecturer1.name,lecturer1.surname,lecturer1.grades)