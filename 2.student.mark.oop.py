class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__marks = {}

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def get_marks(self):
        return self.__marks


class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name


class MarkManagement:
    def __init__(self):
        self.__students = {}
        self.__courses = {}

    def student_input(self):
        student_num = int(input("Enter the number of students: "))
        for i in range(student_num):
            student_id = input("Enter the student id: ")
            student_name = input("Enter the student name: ")
            dob = input("Enter day of birth:")
            self.__students[student_id] = Student(student_id, student_name, dob)

    def course_input(self):
        course_num = int(input("Enter the number of courses:"))
        for i in range(course_num):
            course_id = input("Enter the course id: ")
            if course_id in self.__courses.keys():
                print("Course already exists. Skipping...")
                continue
            course_name = input("Enter the course name: ")
            self.__courses[course_id] = Course(course_id, course_name)

    def mark_input(self):
        courseID = input("Enter the course ID you want to input marks: ")
        if courseID not in self.__courses.keys():
            print("Invalid Course Id! Please enter a valid one.")
        else:
            for studentID, student in self.__students.items():
                new_mark = float(input(f"Enter mark for {student.get_name()}: "))
                student.get_marks()[courseID] = new_mark

    def list_students(self):
        for id, student in self.__students.items():
            print("\n ID:", id)
            print("\tName : ", student.get_name())
            print("\tDate Of Birth : ", student.get_dob())

    def list_courses(self):
        for id_key, course in self.__courses.items():
            print("CourseID:", id_key, "Course name:", course.get_name())

    def show_marks(self):
        course_id = input("Enter course id to show mark: ")
        if course_id not in self.__courses:
            print("The course is not available")
            return
        else:
            for student_id_key, student_object in self.__students.items():
                if course_id in student_object.get_marks():
                    print(f"{student_object.get_name()}: {student_object.get_marks()[course_id]}")
                else:
                    print(student_id_key, ": not available")


########### RUN CODE
test_object = MarkManagement()
test_object.student_input()
test_object.course_input()
test_object.mark_input()
test_object.list_students()
test_object.list_courses()
test_object.show_marks()

# if __name__ == "__main__":
#     marks_manager = MarkManagement()
#     marks_manager.run()