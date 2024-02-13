from domains import student, course
import input
import output
import os
students = {}
courses = {}


input.student_input(students)
input.course_input(courses)
for id, course in courses.items():
    input.mark_input(students, courses)

import os
import input
a = os.path.join(r"C:\Users\buing\Downloads\pp2024\pw5","students.txt")
b= os.path.join(r"C:\Users\buing\Downloads\pp2024\pw5","courses.txt")
c= os.path.join(r"C:\Users\buing\Downloads\pp2024\pw5","marks.txt")
file_list = [a,b,c]

output_file = "students.dat"
input.compress_data(file_list, output_file)

import os
e= os.path.join(r"C:\Users\buing\Downloads\pp2024\pw5","students.dat")
f= os.path.join(r"C:\Users\buing\Downloads\pp2024\pw5","students.txt")
def check_and_decompress():
    if os.path.exists(e):
        input.decompress_data(e, f)

output.list_students(students)
output.list_courses(courses)
output.show_marks(students, courses)
output.calcGPA_sortdescend(students, courses)
