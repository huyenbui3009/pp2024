from domains.student import Student
from domains.course import Course
import pickle
import threading
import zipfile


def student_input(students):
    student_num = int(input("Enter the number of students: "))
    for i in range(student_num):
        student_id = input("Enter the student id: ")
        student_name = input("Enter the student name: ")
        dob = input("Enter day of birth:")
        students[student_id] = Student(student_id, student_name, dob)
    
def course_input(courses):
    course_num = int(input("Enter the number of courses: "))
    for i in range(course_num):
        course_id = input("Enter the course id: ")
        if course_id in courses.keys():
            print("Course already exists. Skipping...")
            continue
        course_name = input("Enter the course name: ")
        course_credit = int(input("Enter the course credit: "))
        courses[course_id] = Course(course_id, course_name, course_credit)
    

def mark_input(students, courses):
    while True:
        courseID = input("Enter the course ID you want to input marks: ")
        if courseID not in courses.keys():
            print("Invalid Course Id! Please enter a valid one.")
        else:      
            for studentID, student in students.items():
                new_mark = float(input(f"Enter mark for {student.get_name()}: "))
                student.get_marks()[courseID] = new_mark
            break

def save(data, files):
    print("this is background save thread running")
    for i, file in enumerate(files):
        with open(file, 'wb') as f:
            pickle.dump(data[i], f)
    
    
def load(files):
    print("this is background load thread running")
    with threading.Lock():
        for file in files:
            with open(file, 'rb') as f:
                loaded_data= pickle.load(f)
            for key, value in loaded_data.items():
                print(value.get_id(),"\t", value.get_name(), "\t", "\t")
    
def compress(files):
        try:
            with zipfile.ZipFile('students.dat','w') as z:
                for file in files:
                    z.write(file)
        except Exception as e:
            print(str(e))

    
 








    

        