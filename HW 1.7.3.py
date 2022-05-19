# 1. Перегрузите магический метод __str__ у всех классов.
# У проверяющих он должен выводить информацию в следующем виде:

# print(some_reviewer)
# Имя: Some
# Фамилия: Buddy

# У лекторов:
# print(some_lecturer)
# Имя: Some
# Фамилия: Buddy
# Средняя оценка за лекции: 9.9

# А у студентов так:
# print(some_student)
# Имя: Ruoy
# Фамилия: Eman
# Средняя оценка за домашние задания: 9.9
# Курсы в процессе изучения: Python, Git
# Завершенные курсы: Введение в программирование

# 2. Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания.


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

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
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

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


student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

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

