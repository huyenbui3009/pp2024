from domains import student, course
import input
import output
import pickle
import threading
import time
import tkinter as tk

students = {}
courses = {}
data=[students, courses]
def run_student_input():
    students = {}
    input.student_input(students)
    print("Student input completed.")

def run_course_input():
    courses = {}
    input.course_input(courses)
    print("Course input completed.")

def run_mark_input():
    input.mark_input(students, courses)
    print("Mark input completed.")

def run_save():
    data = [students, courses]
    files = ["student.pickle", "course.pickle"]
    input.save(data, files)
    print("Data saved.")

def run_compress():
    files = ["student.pickle", "course.pickle"]
    input.compress(files)
    print("Data compressed.")

def run_load():
    files = ["student.pickle", "course.pickle"]
    input.load(files)
    print("Data loaded.")

def start_threads():
    threads = []

    # Create threads for each task
    threads.append(threading.Thread(target=run_student_input))
    threads.append(threading.Thread(target=run_course_input))
    threads.append(threading.Thread(target=run_mark_input))
    threads.append(threading.Thread(target=run_save))
    threads.append(threading.Thread(target=run_compress))
    threads.append(threading.Thread(target=run_load))

    # Start threads
    for thread in threads:
        thread.start()

    # Wait for threads to finish
    for thread in threads:
        thread.join()

def main():
    root = tk.Tk()
    root.title("Student Management System")
    root.geometry("1200x1000")

    # Create GUI elements
    label = tk.Label(root, text="Welcome to Student Management System")
    label.pack()

    btn_start = tk.Button(root, text="Start", command=start_threads)
    btn_start.pack()

    root.mainloop()

if __name__ == "__main__":
    main()