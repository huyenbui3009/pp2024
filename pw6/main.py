from domains import student, course
import input
import output
import pickle
students = {}
courses = {}


input.student_input(students)
input.course_input(courses)
for id, course in courses.items():
    input.mark_input(students, courses)


import pickle
# Unpickling (deserialization)
with open('marks.txt', 'rb') as file:
    loaded_data=pickle.load(file)
for key, value in loaded_data.items():
    print(value.get_id(),"\t", value.get_name(), "\t", value.get_dob(), "\t", value.get_marks())

output.list_students(students)
output.list_courses(courses)
output.show_marks(students, courses)
output.calcGPA_sortdescend(students, courses)
