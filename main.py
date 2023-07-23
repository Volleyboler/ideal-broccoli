
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        name_string = f"Имя: {self.name}"
        surname_string = f"Фамилия: {self.surname}"
        average_grade_string = f"Средняя оценка за домашние задания: {self.get_average_grade()}"
        courses_in_progress_string = ", ".join(self.courses_in_progress)
        courses_in_progress_string_message = f"Курсы в процессе изучения: {courses_in_progress_string}"
        finished_courses_string = ", ".join(self.finished_courses)
        finished_courses_string_message = f"Завершенные курсы: {finished_courses_string}"
        return "\n".join([name_string, surname_string, average_grade_string, courses_in_progress_string_message,
                          finished_courses_string_message])

    def __lt__(self, other):
        if self.get_average_grade() < other.get_average_grade():
            return True
        else:
            return False

    def __gt__(self, other):
        if self.get_average_grade() > other.get_average_grade():
            return True
        else:
            return False

    def __eq__(self, other):
        if self.get_average_grade() == other.get_average_grade():
            return True
        else:
            return False

    def add_course(self, course_name):
        self.courses_in_progress.append(course_name)

    def add_finished_course(self, course_name):
        if course_name in self.courses_in_progress:
            self.courses_in_progress.remove(course_name)
            self.finished_courses.append(course_name)
            return True
        return False

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def get_average_grade(self):
        summ = 0
        amount = 0
        if len(self.grades.values()) > 0:
            for value in self.grades.values():
                summ += sum(value)
                amount += len(value)
            return round(summ / amount, 1)
        else:
            return 0


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_course(self, course_name):
        self.courses_attached.append(course_name)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        name_string = f"Имя: {self.name}"
        surname_string = f"Фамилия: {self.surname}"
        average_grade_string = f"Средняя оценка за лекции: {self.get_average_grade()}"
        return "\n".join([name_string, surname_string, average_grade_string])

    def __lt__(self, other):
        if self.get_average_grade() < other.get_average_grade():
            return True
        else:
            return False

    def __gt__(self, other):
        if self.get_average_grade() > other.get_average_grade():
            return True
        else:
            return False

    def __eq__(self, other):
        if self.get_average_grade() == other.get_average_grade():
            return True
        else:
            return False

    def get_average_grade(self):
        summ = 0
        amount = 0
        if len(self.grades.values()) > 0:
            for value in self.grades.values():
                summ += sum(value)
                amount += len(value)
            return round(summ / amount, 1)
        else:
            return 0


class Reviewer(Mentor):

    def __str__(self):
        return f"Имя: {self.name}""\n"f"Фамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"


def get_average_of_hole_course(course, *stud_or_lect):
    '''
    :param course:
    :param stud_or_lect:
    :return: average grade per course rounded to the first decimal place
    None - if stud_or_lect is not instance class Student or Lecturer
    '''
    summ = 0
    amount = 0
    for man in stud_or_lect:
        if isinstance(man, Student) or isinstance(man, Lecturer):
            lenght = len(man.grades[course])
            if lenght > 0:
                summ += sum(man.grades[course])
                amount += lenght
        else:
            return None
    return round(summ / amount, 1)


first_student = Student("Ben", "Black", "male")
second_student = Student("Anna", "White", "female")

first_student.add_course("Python")
first_student.add_course("C++")
first_student.add_finished_course("C++")
second_student.add_course("Python")
second_student.add_finished_course("C#")


first_lecturer = Lecturer("Michael", "Botch")
second_lecturer = Lecturer("Anna", "Black")

first_lecturer.add_course("Python")
second_lecturer.add_course("Python")
second_lecturer.add_course("C++")


first_reviewer = Reviewer("Ivan", "Red")
second_reviewer = Reviewer("Iren", "Adler")

first_reviewer.add_course("Python")
first_reviewer.add_course("C#")
second_reviewer.add_course("Python")

first_student.rate_lec(first_lecturer, "Python", 10)
first_student.rate_lec(first_lecturer, "Python", 5)
first_student.rate_lec(first_lecturer, "Python", 8)
first_student.rate_lec(first_lecturer, "Python", 7)

second_student.rate_lec(second_lecturer, "Python", 5)
second_student.rate_lec(second_lecturer, "Python", 2)
second_student.rate_lec(second_lecturer, "Python", 3)
second_student.rate_lec(second_lecturer, "Python", 4)

first_reviewer.rate_hw(first_student, "Python", 2)
first_reviewer.rate_hw(first_student, "Python", 3)
first_reviewer.rate_hw(first_student, "Python", 6)
first_reviewer.rate_hw(first_student, "Python", 4)

second_reviewer.rate_hw(second_student, "Python", 10)
second_reviewer.rate_hw(second_student, "Python", 8)
second_reviewer.rate_hw(second_student, "Python", 10)
second_reviewer.rate_hw(second_student, "Python", 9)

print(first_student)
print(second_student)

print(first_student > second_student)
print(first_student < second_student)
print(first_student == second_student)


print(first_lecturer)
print(second_lecturer)

print(first_lecturer > second_lecturer)
print(first_lecturer < second_lecturer)
print(first_lecturer == second_lecturer)

print(first_reviewer)
print(second_reviewer)


print(get_average_of_hole_course("Python", first_student, second_student))

print(get_average_of_hole_course("Python", first_lecturer, second_lecturer))