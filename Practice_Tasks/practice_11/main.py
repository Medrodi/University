from cmath import pi
# class Car:
#     def __init__(self, color: str, type: str, year: int):
#         self.color = color
#         self.type = type
#         self.year = year
#
#     def start_engine(self):
#         print("Автомобиль заведён")
#
#     def stop_engine(self):
#         print("Автомобиль заглушен")
#
#     def set_color(self, color: str):
#             self.year = color
#     def set_year(self, year: int):
#             self.year = year
#     def set_type(self, type: str):
#             self.type = type
#
# myCar = Car("Чёрный", "Ferari", 2000)
# print(myCar.type, myCar.color, myCar.year)
# myCar.set_year(1980)
# print(myCar.type, myCar.color, myCar.year)
# myCar.set_type("Porshe")
# print(myCar.type, myCar.color, myCar.year)
# myCar.set_color("black")
# print(myCar.type, myCar.color, myCar.year)
#
# myCar.start_engine()
# myCar.stop_engine()

# class Sphere:
#     def __init__(self, radius = 1.0, x = 0.0, y = 0.0, z = 0.0):
#         self.radius = float(radius)
#         self.x = float(x)
#         self.y = float(y)
#         self.z = float(z)
#
#     def get_volume(self):
#         return float(4/3 * pi * self.radius ** 3)
#
#     def get_square(self):
#         return float(4 * pi * self.radius ** 2)
#
#     def get_radius(self):
#         return self.radius
#
#     def get_center(self):
#         return (self.x, self.y, self.z)
#
#     def set_radius(self, r):
#         self.radius = float(r)
#
#     def set_center(self, x, y, z):
#         self.x = float(x)
#         self.y = float(y)
#         self.z = float(z)
#
#     def is_point_inside(self, x, y, z):
#         if (self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2 < self.radius ** 2:
#             return True
#         else:
#             return False
#
#
# s0 = Sphere(0.5) # test sphere creation with radius and default center
# print(s0.get_center()) # (0.0, 0.0, 0.0)
# print(s0.get_volume()) # 0.523598775598
# print(s0.is_point_inside(0 , -1.5, 0)) # False
# s0.set_radius(1.6)
# print(s0.is_point_inside(0, -1.5, 0)) # True
# print(s0.get_radius()) # 1.6

# class SuperStr(str):
#     def __init__(self, s):
#         self.string = s
#     def is_repeatance(self, stroka):
#         if not isinstance(stroka, str):
#             return False
#         elif len([x for x in self.string.split(stroka) if len(x) > 0]) == 0:
#             return True
#         else:
#             return False
#
#     def is_palindrom(self):
#         if self.string == self.string[::-1]:
#             return True
#         else:
#             return False
#
# s = SuperStr("123123123123")
# print(s.is_repeatance("123")) # True
# print(s.is_repeatance("123123")) # True
# print(s.is_repeatance("123123123123")) # True
# print(s.is_repeatance("12312")) # False
# print(s.is_repeatance(123)) # False
# print(s.is_palindrom()) # False
# print(s, type(s)) # 123123123123 (строка)
# print(int(s), type(int(s))) # 123123123123 (целое число)
# print(s + "qwe") # 123123123123qwe
# p = SuperStr("123_321")
# print(p.is_palindrom()) # True


def avarage_grade_student(students: list, course : str) -> float:
    """
    Функция принимает принимаем список студентов и название курса и выводит среднюю оценку за домашние задания
     по всем студентам в рамках конкретного курса
    :param student: список студентов в виде list
    :param course: курс в виде str
    :return: возвращает среднее арифметическое всех оценок
    """
    grades = 0
    count = 0
    for student in students:
        for lists in student.grades.values():
            for rate in lists:
                grades += rate
                count += 1

    rate = grades / count
    return  rate

def avarage_rate_lecture(lectures : list, course : str) -> float:
    """
    Функция avarage_rate_lecture используется для подсчета средней оценки за лекции всех лекторов
    в рамках курса. в качестве аргумента принимаем список лекторов и название курса
    :param lectures: список лекторов в виде списка list
    :param course: название курса в виде строки str
    :return: возвращает среднее
    """
    grades = 0
    count = 0
    for lecture in lectures:
        for lists in lecture.students_grades.values():
            for rate in lists:
                grades += rate
                count += 1
    rate = grades / count
    return  rate

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __int__(self): # возвращает количество изучаемых курсов
        return len(self.courses_in_progress)

    def __bool__(self): # возвращает True, если есть хоть один завершённый курс, иначе False
        if self.finished_courses != []:
            return True
        else:
            return False

    def __float__(self): #возвращает количество оценок студента
        count = 0
        for lists in self.grades.values():
            for rate in lists:
                count += 1
        return float(count)


    def __str__(self):
        grades = 0
        count = 0
        for lists in self.grades.values():
            for rate in lists:
                grades += rate
                count += 1

        rate = grades / count

        courses_progress = ""
        for i in self.courses_in_progress:
            courses_progress += i + ", "
        end_courses = ""
        if self.finished_courses != []:
            for i in self.finished_courses:
                end_courses += i + ", "
        else:
            end_courses = "Отсутствуют"
        return (f"\nИмя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {rate}\n"
                f"Курсы в процессе изучения: {courses_progress}\n"
                f"Завершённые курсы: {end_courses}\n")
    def add_courses(self, course_name):
        if not course_name in self.finished_courses:
            self.finished_courses.append(course_name)
        else:
            print(f"{self.name} уже завершил курс {course_name}")

    def set_rate_lect(self, lecturer, course, grade:int):
        if course in lecturer.courses_attached and course in self.courses_in_progress:
            if 1 <= grade <= 10 and isinstance(grade, int):
                if course in lecturer.students_grades:
                        lecturer.students_grades[course].append(grade)
                else:
                    lecturer.students_grades[course] = [grade]
            else:
                print("Ошибка в данных")
        else:
            print(f"{lecturer.name} {lecturer.surname} не ведёт {course} у {self.name}")

    def start_course(self, course:str):
        if not course in self.courses_in_progress:
            self.courses_in_progress.append(course)
        else:
            print(f"Студент уже изучает {course}")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        student.grades[course] = [grade]


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.students_grades = {}

    def __bool__(self): # возвращает True, если у лектора есть хоть один предмет, еоторый он ведёт, иначе False
        if self.courses_attached != []:
            return True
        else:
            return False

    def __int__(self): # возвращает количество предметов, которые он ведёт
        return len(self.courses_attached)

    def __float__(self): # возвращает отношение количества оценок к кол-ву проводимых курсов
        count = 0
        for lists in self.students_grades.values():
            for rate in lists:
                count += 1
        return count / len(self.courses_attached)


    def __str__(self):
        grades = 0
        count = 0
        for lists in self.students_grades.values():
            for rate in lists:
                grades += rate
                count += 1

        rate = grades / count
        return (f"\nИмя: {self.name} \n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {rate}")
    def add_course(self, course):
        if not course in self.courses_attached:
            self.courses_attached.append(course)

class Reviewer(Mentor):

    def __str__(self):
        return (f"\nИмя: {self.name} \n"
              f"Фамилия: {self.surname}\n")

    def __int__(self): #возвращает количество курсов, которые ведёт преподаватель
        return len(self.courses_attached)

    def __bool__(self): # возвращает True, если преподавателя зовут Александр Стрельцов
        if self.name == "Александр" and self.surname == "Стрельцов":
            return True
        else:
            return False

    def __call__(self, course: str):
        """
        Функция __call__ выводит сообщение о том, что студенты хотят, что бы преподаватель вёл какой-нибудь
        пердмет
        :param course: название курса
        """
        print(f"Студенты хотят, чтобы {self.name} {self.surname} вёл {course}")


    def add_course(self, course):
        if not course in self.courses_attached:
            self.courses_attached.append(course)
    def rate_student(self, student, course, grade):
        if course in self.courses_attached and course in student.courses_in_progress:
            if course not in student.grades:
                student.grades[course] = [grade]
            else:
                student.grades[course].append(grade)
        else:
            print(f"{self.name} {self.surname} не ведёт {course} у {student.name}")

#Reviewers
reviewer_1 = Reviewer("Александр", "Стрельцов")
reviewer_1.add_course("Python")
reviewer_1.add_course("Анализ данных")

reviewer_2 = Reviewer("Денис", "Лебедев")
reviewer_2.add_course("Информатика")

#Lecturers
lector_1 = Lecturer("Александр", "Закатов")
lector_1.add_course("История")
lector_1.add_course("Философия")

lector_2 = Lecturer("Татьяна", "Катюхина")
lector_2.add_course("Философия")
lector_2.add_course("ОРГ")
lector_2.add_course("История")

#Students
Den = Student("Денис", "Степанов", "М")
Den.start_course("Python")
Den.start_course("История")
Den.start_course("Философия")
Den.start_course("ОРГ")
Den.start_course("Информатика")
Den.add_courses("Введение в программирование")

Andrew = Student("Андрей", "Пучков", "М")
Andrew.start_course("Python")
Andrew.start_course("История")
Andrew.start_course("Философия")
Andrew.start_course("ОРГ")
Andrew.start_course("Информатика")

#Reviewers grades
reviewer_1.rate_student(Den, "Python", 5)
reviewer_1.rate_student(Andrew, "Python", 8)
reviewer_1.rate_student(Andrew, "История", 10)

reviewer_2.rate_student(Andrew, "Информатика", 7)
reviewer_2.rate_student(Den, "Информатика", 3)
reviewer_2.rate_student(Andrew, "Python", 1)


#Students rates
Den.set_rate_lect(lector_1, "История", 10)
Den.set_rate_lect(lector_1, "История", 3)
Den.set_rate_lect(lector_1, "История", 7)
Den.set_rate_lect(lector_2, "История", 5)
Den.set_rate_lect(lector_2, "Философия", 8)
Den.set_rate_lect(lector_2, "История", 3)

Andrew.set_rate_lect(lector_1, "История", 10)
Andrew.set_rate_lect(lector_2, "История", 1)
Andrew.set_rate_lect(lector_2, "Философия", 1)
Andrew.set_rate_lect(lector_2, "Философия", 3)
Andrew.set_rate_lect(lector_2, "Философия", 5)


#Student's magic modules
print(Den)
print(int(Den))
print(bool(Den))
print(float(Den))

print(Andrew)
print(int(Andrew))
print(bool(Andrew))
print(float(Andrew))

#Reviewer's magic modules
print(reviewer_1)
print(int(reviewer_1))
print(bool(reviewer_1))
reviewer_1("Python")

print(reviewer_2)
print(int(reviewer_2))
print(bool(reviewer_2))
reviewer_2("Информатика")

#Lecturer's magic modules
print(lector_1)
print(int(lector_1))
print(bool(lector_1))
print(float(lector_1))

print(lector_2)
print(int(lector_2))
print(bool(lector_2))
print(float(lector_2))

print("Средняя оценка за домашние задания у студентов: ",
      avarage_grade_student([Den, Andrew], "Python"))
print("Средняя оценка за лекции всех лекторов: ",
      avarage_rate_lecture([lector_2, lector_1], "История"))