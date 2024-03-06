class Student:
    global gradebook_lect
    gradebook_lect = {}

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate(self, lecturer, course, grade):
        if course not in gradebook_lect:
            gradebook_lect[course] = {}

        if (
            isinstance(lecturer, Lecturer)
            and course in lecturer.courses_attached
            and (course in self.courses_in_progress or course in self.finished_courses)
        ):
            if course in lecturer.rate_mentors:
                lecturer.rate_mentors[course] += [grade]
            else:
                lecturer.rate_mentors[course] = [grade]

            if course in gradebook_lect:
                if lecturer.name not in gradebook_lect[course]:
                    gradebook_lect[course].setdefault(lecturer.name, [])
                    gradebook_lect[course][lecturer.name].append(grade)
                if lecturer.name in gradebook_lect[course]:
                    for name in gradebook_lect[course]:
                        if name == lecturer.name:
                            gradebook_lect[course][lecturer.name].append(grade)
            elif course not in gradebook_lect:
                gradebook_lect[course] = {lecturer.name: grade}

    def averating(self):
        total = 0
        count = 0
        for grade in self.grades.values():
            count += len(grade)
        for i in self.grades.values():
            for num in i:
                total += num
        return round(total / count, 1)

    def __str__(self):

        return (
            f"Имя: {self.name}\nФамилия: {self.surname}\n"
            + f"Средняя оценка за лекции: {self.averating()}\n"
            + f'Курсы в процессе изучения: {", ".join(self.courses_in_progress, )}\n'
            + f'Завершенные курсы: {", ".join(self.finished_courses)}'
        )

    def __eq__(self, other):
        return self.averating() == other.averating()

    def __ne__(self, other):
        return self.averating() != other.averating()

    def __lt__(self, other):
        return self.averating() < other.averating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    global gradebook_stud
    gradebook_stud = {}

    def rate_hw(self, student, course, grade):
        if course not in gradebook_stud:
            gradebook_stud[course] = {}
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and (
                course in student.courses_in_progress
                or course in student.finished_courses
            )
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]

            if course in gradebook_stud:
                if student.name not in gradebook_stud[course]:
                    gradebook_stud[course].setdefault(student.name, [])
                    gradebook_stud[course][student.name].append(grade)
                if student.name in gradebook_stud[course]:
                    for name in gradebook_stud[course]:
                        if name == student.name:
                            gradebook_stud[course][student.name].append(grade)
            elif course not in gradebook_stud:
                gradebook_stud[course] = {student.name: grade}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rate_mentors = {}

    def averating(self):
        total = 0
        count = 0
        for grade in self.rate_mentors.values():
            count += len(grade)
        for i in self.rate_mentors.values():
            for num in i:
                total += num

        return round(total / count, 1)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.averating()}"

    def __eq__(self, other):
        return self.averating() == other.averating()

    def __ne__(self, other):
        return self.averating() != other.averating()

    def __lt__(self, other):
        return self.averating() < other.averating()


def average_for_studens(course):
    total = 0
    count = 0
    for students in gradebook_stud[course]:
        for grade in gradebook_stud[course][students]:
            total += grade
            count += 1
    return (
        f"Средняя оценка, за домашние задания по {course} {round(total / count, 1)}"
    )


def average_for_lecturer(course):
    total = 0
    count = 0
    for lecturer in gradebook_lect[course]:
        for grade in gradebook_lect[course][lecturer]:
            total += grade
            count += 1
    return f"Средняя оценка, за лекции по {course} {round(total / count, 1)}"


def data_and_print_test_for_code():
    best_student = Student("Ruoy", "Eman", "your_gender")
    best_student.courses_in_progress += ["Python", "C++", "Java"]

    other_student = Student("Martyn", "Zoydberg", "your_gender")
    other_student.courses_in_progress += ["Python"]
    other_student.finished_courses += ["Java"]

    origin_mentor = Reviewer("Some", "Buddy")
    origin_mentor.courses_attached += ["Python", "C++", "Java"]

    cool_mentor = Lecturer("George", "Blueberry")
    cool_mentor.courses_attached += ["Python", "C++", "Java"]

    sec_mentor = Lecturer("Garry", "Catfish")
    sec_mentor.courses_attached += ["Python", "Java"]

    bad_student = Student("Harold", "Dumb", "your_gender")
    bad_student.courses_in_progress += ["Python"]

    origin_mentor.rate_hw(best_student, "Python", 10)
    origin_mentor.rate_hw(best_student, "C++", 10)
    origin_mentor.rate_hw(best_student, "Java", 10)

    origin_mentor.rate_hw(other_student, "Python", 9)
    origin_mentor.rate_hw(other_student, "Java", 10)

    origin_mentor.rate_hw(bad_student, "Python", 3)

    best_student.rate(cool_mentor, "Python", 10)
    best_student.rate(cool_mentor, "C++", 7)
    best_student.rate(cool_mentor, "Java", 10)
    best_student.rate(sec_mentor, "Python", 10)
    best_student.rate(sec_mentor, "Java", 9)
    other_student.rate(sec_mentor, "Java", 10)
    other_student.rate(sec_mentor, "Python", 10)
    other_student.rate(cool_mentor, "Java", 10)
    other_student.rate(cool_mentor, "Python", 10)
    bad_student.rate(cool_mentor, "Python", 1)
    bad_student.rate(sec_mentor, "Python", 1)

    print(origin_mentor, "\n")
    print(cool_mentor, "\n")
    print(sec_mentor, "\n")
    print(best_student, "\n")
    print(other_student, "\n")
    print(bad_student, "\n")
    print(cool_mentor < sec_mentor, "\n")
    print(best_student > other_student, "\n")
    print(average_for_lecturer("Python"), average_for_studens("C++"), sep="\n")


data_and_print_test_for_code()
