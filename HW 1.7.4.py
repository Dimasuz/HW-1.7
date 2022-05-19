# Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:
# 1. для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);
# 2. для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список лекторов и название курса).


class Student:
    class_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.class_list.append(self)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and grade in range(
                1, 11):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):  # определение средней оценки
        s = 0
        n = 0
        for i in self.grades.values():
            s += sum(i)
            n += len(i)
        return s / n

    def __str__(self):
        print_student = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {round(self.average_rating(), 1)}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return print_student

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_rating() < other.average_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    class_list = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.class_list.append(self)

    def __str__(self):
        print_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(Student.average_rating(self), 1)}'
        return print_lecturer

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return Student.average_rating(self) < Student.average_rating(other)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress and grade in range(
                1, 11):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        print_reviewer = f'Имя: {self.name}\nФамилия: {self.surname}'
        return print_reviewer

    # так было бы проще реализовать подсчет средней оценки по курсу у всех студентов и лекторов, но тогда надо вызывать не список и курс, как в задании, а класс и курс


# def average_all(klass, course):
#         s = 0
#         n = 0
#         for i in klass.class_list:
#             s += sum(i.grades[course])
#             n += len(i.grades[course])
#         return s / n

def average_all(klass_list, course):
    s = 0
    n = 0
    for i in klass_list:
        s += sum(i.grades[course])
        n += len(i.grades[course])
    return s / n


student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.add_courses('Введение в программирование')

student_2 = Student('Danya', 'Groune', 'your_gender')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']

mentor_1 = Mentor('Some1', 'Buddy1')
mentor_1.courses_attached += ['Python']
mentor_1.courses_attached += ['Git']

mentor_2 = Mentor('Some2', 'Buddy2')
mentor_2.courses_attached += ['Python']
mentor_2.courses_attached += ['Git']

reviewer_1 = Reviewer('Petr1', 'Pupkin1')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']

reviewer_2 = Reviewer('Petr2', 'Pupkin2')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']

lecturer_1 = Lecturer('Vasiliy', 'Ivanov')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']

lecturer_2 = Lecturer('Oleg', 'Petrov')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']

reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Git', 7)

reviewer_2.rate_hw(student_1, 'Python', 7)
reviewer_2.rate_hw(student_1, 'Python', 5)
reviewer_2.rate_hw(student_1, 'Git', 6)

student_1.rate_hw(lecturer_1, 'Python', 9)
student_2.rate_hw(lecturer_1, 'Git', 7)

student_1.rate_hw(lecturer_2, 'Python', 7)
student_2.rate_hw(lecturer_2, 'Git', 6)

print(reviewer_1)
print()
print(reviewer_2)
print()
print(lecturer_1)
print()
print(lecturer_2)
print()
print(student_1)
print()
print(student_2)

print()
print('Сравнение студентов:', student_1 < student_2)
print('Сравнение лекторов:', lecturer_1 > lecturer_2)

# это вызов функции подсчета средней оценки по курсу у всех студентов и лекторов по вызову класса и курса
# print()
# print('Средняя оценка всех студентов по курсу Python:', average_all(Student, 'Python'))
# print('Средняя оценка всех лекторов по курсу Python:', average_all(Lecturer, 'Python'))

print()
student_list = Student.class_list  # объявление списка всех студентов
print('Средняя оценка всех студентов по курсу Python:', average_all(student_list, 'Python'))
lecturer_list = Lecturer.class_list  # объявление списка всех лекторов
print('Средняя оценка всех лекторов по курсу Python:', average_all(lecturer_list, 'Python'))
