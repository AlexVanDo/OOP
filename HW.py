class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.rate_mentors:
                lecturer.rate_mentors[course] += [grade]
            else:
                lecturer.rate_mentors[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rate_mentors = {}


best_student = Student("Ruoy", "Eman", "your_gender")
best_student.courses_in_progress += ["Python", "C++", "Java"]

origin_mentor = Reviewer("Some", "Buddy")
origin_mentor.courses_attached += ["Python", "C++", "Java"]

cool_mentor = Lecturer("George", "Blueberry")
cool_mentor.courses_attached += ["Python", "C++", "Java"]

sec_mentor = Lecturer("Garry", "Catfish")
sec_mentor.courses_attached += ["Python", "JavaScript"]

origin_mentor.rate_hw(best_student, "Python", 10)
origin_mentor.rate_hw(best_student, "Python", 10)
origin_mentor.rate_hw(best_student, "Python", 10)

best_student.rate(cool_mentor, "Python", 10)
best_student.rate(cool_mentor, "C++", 9)
best_student.rate(cool_mentor, "C++", 7)
best_student.rate(cool_mentor, "Java", 10)
best_student.rate(sec_mentor, "Python", 10)
best_student.rate(sec_mentor, "C++", 9)
best_student.rate(sec_mentor, "C++", 7)
best_student.rate(sec_mentor, "Java", 10)

print(best_student.grades)
print(cool_mentor.rate_mentors)
print(sec_mentor.rate_mentors)
