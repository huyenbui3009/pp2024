import math
import numpy as np

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
    def __init__(self, id, name, credit):
        self.__id = id
        self.__name = name
        self.__credit= credit

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
    
    def get_credit(self):
        return self.__credit

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
            course_credit=int(input("Enter the course credit: "))
            self.__courses[course_id] = Course(course_id, course_name, course_credit)

    def mark_input(self):
        for studentID, student_object in self.__students.items():
            for courseID, course_object in self.__courses.items():
                print(f"Enter mark for course {course_object.get_name()} ")
                new_mark = float(input(f"{student_object.get_name()} : "))
                student_object.get_marks()[courseID] = (math.floor(new_mark * 10)) / 10

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
    
    def calcGPA_sortdescend(self):
        course_ids= np.array(list(self.__courses.keys()))
        course_credits= np.array([credit.get_credit() for credit in self.__courses.values()])
        credit_sum= sum(course_credits)
        student_gpas = []
        for id, student_object in self.__students.items():
            student_marks = np.array([student_object.get_marks().get(course_id, 0) for course_id in course_ids])
            # use built-in method for dict to return value with key=course_id and return=0 if not found
            gpa = np.dot(student_marks, course_credits)/credit_sum
            student_gpas.append((id, student_object.get_name(), gpa))
            #list of tuples
        
        sorted_students = sorted(student_gpas, key=lambda x: x[2], reverse=True)
        # Display the sorted list                sort based on third element: gpa
        print("\nSorted Students by GPA (Descending Order):")
        for student_info in sorted_students:
            print(f"ID: {student_info[0]}, Name: {student_info[1]}, GPA: {student_info[2]}")

        

########### RUN CODE
test_object = MarkManagement()
test_object.student_input()
test_object.course_input()
test_object.mark_input()
test_object.calcGPA_sortdescend()

