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

file_list = ["student.txt", "courses.txt", "marks.txt"]
output_file = "students.dat"
input.compress_data(file_list, output_file)
# Directory to store the compressed file
new_directory = r"C:\Users\buing\Downloads\pp2024\pw5\result"
destination = os.path.join(new_directory, output_file)
os.rename(output_file, destination)


def check_and_decompress():
    if os.path.exists('students.dat'):
        input.decompress_data('students.dat', '.')

output.list_students(students)
output.list_courses(courses)
output.show_marks(students, courses)
output.calcGPA_sortdescend(students, courses)
