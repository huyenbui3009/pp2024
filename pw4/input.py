from domains.student import Student
from domains.course import Course

def student_input(students):
    student_num = int(input("Enter the number of students: "))
    for i in range(student_num):
        student_id = input("Enter the student id: ")
        student_name = input("Enter the student name: ")
        dob = input("Enter day of birth:")
        students[student_id] = Student(student_id, student_name, dob)

def course_input(courses):
    course_num = int(input("Enter the number of courses:"))
    for i in range(course_num):
        course_id = input("Enter the course id: ")
        if course_id in courses.keys():
            print("Course already exists. Skipping...")
            continue
        course_name = input("Enter the course name: ")
        course_credit=int(input("Enter the course credit: "))
        courses[course_id] = Course(course_id, course_name, course_credit)


def mark_input(students, courses):
        courseID = input("Enter the course ID you want to input marks: ")
        if courseID not in courses.keys():
            print("Invalid Course Id! Please enter a valid one.")
        else:
            for studentID, student in students.items():
                new_mark = float(input(f"Enter mark for {student.get_name()}: "))
                student.get_marks()[courseID] = new_mark