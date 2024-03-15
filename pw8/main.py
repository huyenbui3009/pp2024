from domains import student, course
import input
import output
import pickle
import threading
import time
students = {}
courses = {}
data=[students, courses]

input.student_input(students)
input.course_input(courses)
for id, course in courses.items():
    input.mark_input(students, courses)
    

files=["student.pickle", "course.pickle"]
threadsave= threading.Thread(target=input.save, args=(data, files,))
threadcompress= threading.Thread(target=input.compress, args=(files,))
threadload= threading.Thread(target=input.load, args=(files,))

threadsave.start()
threadload.start()
threadcompress.start()
print("\n this is main thread doing some stuff ")
threadsave.join()
threadload.join()
threadcompress.join()

time.sleep(10)
print("main thread finished")


# output.list_students(students)
# output.list_courses(courses)
# output.show_marks(students, courses)
# output.calcGPA_sortdescend(students, courses)
