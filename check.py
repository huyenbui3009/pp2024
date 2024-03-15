# import multiprocessing as mp
# import time 

# def counter(num):
#     count=0
#     while count<num:
#         count +=1

# def main():
#     a=mp.Process(target=counter, args=(500000))
#     a.start()
#     a.join()



import curses
import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

class ECT:
    def __init__(self, ects):
        self.ects = ects

class StudentMarkManagement:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.students = {}
        self.courses = {}
        self.marks = {}
        self.ects = {}

    def add_student(self):
        self.stdscr.clear()
        self.stdscr.addstr("Enter Student ID: ")
        self.stdscr.refresh()
        student_id = self.stdscr.getstr().decode()
        self.stdscr.addstr("Enter Full Name: ")
        self.stdscr.refresh()
        name = self.stdscr.getstr().decode()
        self.stdscr.addstr("Enter Date of Birth (dd/mm/yyyy): ")
        self.stdscr.refresh()
        dob = self.stdscr.getstr().decode()
        self.students[student_id] = Student(student_id, name, dob)

    def add_course(self):
        self.stdscr.clear()
        self.stdscr.addstr("Enter Course ID: ")
        self.stdscr.refresh()
        course_id = self.stdscr.getstr().decode()
        self.stdscr.addstr("Enter Course Name: ")
        self.stdscr.refresh()
        course_name = self.stdscr.getstr().decode()
        self.courses[course_id] = Course(course_id, course_name)
        
    def enter_ect(self):
        for course_id, course in self.courses.items():
            self.stdscr.clear()
            self.stdscr.addstr(f"Entering ECTs for {course.course_name}\n")
            self.stdscr.refresh()
            self.stdscr.addstr(f"Enter ECTs for {course.course_name}: ")
            self.stdscr.refresh()
            ect = int(self.stdscr.getstr().decode())
            self.ects[course_id] = ECT(ect)            

    def enter_mark(self):
        for course_id, course in self.courses.items():
            self.stdscr.clear()
            self.stdscr.addstr(f"Entering marks for {course.course_name}\n")
            self.stdscr.refresh()
            self.stdscr.addstr(f"\nEntering marks for {course.course_name}\n")
            self.stdscr.refresh()
            self.marks[course_id] = {}
            for student_id, student in self.students.items():
                self.stdscr.addstr(f"Enter mark for {student.name} (ID: {student_id}) (Decimal number please, example: 19.00): ")
                self.stdscr.refresh()
                mark = float(self.stdscr.getstr().decode())
                self.marks[course_id][student_id] = mark

    def calculate_gpa(self, student_id):
        gpa_list = []
        sum_ects = sum(self.ects[course_id].ects for course_id in self.ects)
        self.stdscr.addstr("Total ECTs: " + str(sum_ects) + "\n")
        self.stdscr.refresh()
        for course_id, course_marks in self.marks.items():
            if student_id in course_marks:
                mark = course_marks[student_id]
                ect = self.ects[course_id].ects
                gpa_list.append((mark * ect) / sum_ects)
        return np.round(np.sum(gpa_list), 2)

    def sort_students_by_gpa(self):
        sorted_students = sorted(self.students.values(), key=lambda x: self.calculate_gpa(x.student_id), reverse=True)
        return sorted_students

    def summary_table(self):
        header_line = "ID         Name                Date of Birth   "
        for course_id, course in self.courses.items():
            header_line += f"{course.course_name[:10]} (ECTs: {self.ects[course_id].ects}) "
        self.stdscr.addstr(header_line + "\n")
        self.stdscr.addstr('-' * len(header_line) + "\n")
        for student_id, student in self.students.items():
            student_row = f"{student.student_id:<10}{student.name:<20}{student.dob:<18}"
            for course_id in self.courses:
                mark = math.floor((self.marks.get(course_id, {}).get(student_id, 'N/A')) *10) / 10
                student_row += f"{mark:<18}"
            self.stdscr.addstr(student_row + "\n")
        self.stdscr.addstr('-' * len(header_line) + "\n")
        self.stdscr.refresh()

def main(stdscr):
    stdscr.clear()
    system = StudentMarkManagement(stdscr)
    while True:
        stdscr.clear()
        stdscr.addstr("1. Add Student\n")
        stdscr.addstr("2. Add Course\n")
        stdscr.addstr("3. Enter ECTs\n")
        stdscr.addstr("4. Enter Marks\n")
        stdscr.addstr("5. Summary Table\n")
        stdscr.addstr("6. Sort Students by GPA\n")
        stdscr.addstr("7. Exit\n")
        stdscr.addstr("Enter your choice: ")
        stdscr.refresh()
        choice = stdscr.getstr().decode()
        stdscr.clear()
        
        if choice == '1':
            system.add_student()
        elif choice == '2':
            system.add_course()
        elif choice == '3':
            system.enter_ect()
        elif choice == '4':
            system.enter_mark()
        elif choice == '5':
            system.summary_table()
            stdscr.addstr("\nPress any key to continue...")
            stdscr.refresh()
            stdscr.getch()
        elif choice == '6':
            stdscr.clear()
            sorted_students = system.sort_students_by_gpa()
            stdscr.addstr("\nSorted Students by GPA:\n")
            for student in sorted_students:
                stdscr.addstr(f"ID: {student.student_id}, Name: {student.name}, GPA: {system.calculate_gpa(student.student_id)}\n")
            stdscr.addstr("\nPress any key to continue...")
            stdscr.refresh()
            stdscr.getch()
        elif choice == '7':
            break

if __name__ == "__main__":
    curses.wrapper(main)