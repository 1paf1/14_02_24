class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Subject: {self.subject}"


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}"


class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

    def __str__(self):
        return f"Subject: {self.name}, Teacher: {self.teacher}"


class Faculty:
    def __init__(self, name, subjects=None):
        self.name = name
        self.subjects = subjects if subjects else []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def __str__(self):
        return f"Faculty: {self.name}"


class Academy:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.subjects = []
        self.faculties = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def add_faculty(self, faculty):
        self.faculties.append(faculty)

    def __str__(self):
        return f"Academy: {self.name}"



if __name__ == "__main__":
    teacher1 = Teacher("John Doe", 35, "Mathematics")
    teacher2 = Teacher("Jane Smith", 40, "Physics")

    student1 = Student("Alice Johnson", 20, "S123")
    student2 = Student("Bob Wilson", 22, "S456")

    subject1 = Subject("Mathematics", teacher1)
    subject2 = Subject("Physics", teacher2)

    faculty1 = Faculty("Science", [subject1, subject2])

    academy = Academy("My Academy")
    academy.add_teacher(teacher1)
    academy.add_teacher(teacher2)
    academy.add_student(student1)
    academy.add_student(student2)
    academy.add_subject(subject1)
    academy.add_subject(subject2)
    academy.add_faculty(faculty1)

    # Виведення інформації
    print(academy)

    print("\nTeachers:")
    for teacher in academy.teachers:
        print(teacher)

    print("\nStudents:")
    for student in academy.students:
        print(student)

    print("\nSubjects:")
    for subject in academy.subjects:
        print(subject)

    print("\nFaculties:")
    for faculty in academy.faculties:
        print(faculty)
