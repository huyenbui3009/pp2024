from domains import student, course
import input
import output

students = {}
courses = {}

input.student_input(students)
input.course_input(courses)
for id, course in courses.items():
    input.mark_input(students, courses)

output.list_students(students)
output.list_courses(courses)
output.show_marks(students, courses)
output.calcGPA_sortdescend(students, courses)
