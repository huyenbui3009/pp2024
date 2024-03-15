from domains import student, course
import input
import output
import pickle
students = {}
courses = {}

data= [students, courses]

input.student_input(students)
input.course_input(courses)
for id, course in courses.items():
    input.mark_input(students, courses)

files=["students.pickle", "courses.pickle"]
input.save(data, files)

new_stu = input.load("students.pickle")
new_course = input.load("courses.pickle")

if new_stu is not None:
    students.update(new_stu)
if new_course is not None:
    courses.update(new_course)

input.compress(files, "PYTHON")


# output.show_marks(students, courses)
# output.calcGPA_sortdescend(students, courses)
