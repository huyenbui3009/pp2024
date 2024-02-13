from domains.student import Student
from domains.course import Course
import zlib
import os 

def student_input(students):
    student_num = int(input("Enter the number of students: "))
    for i in range(student_num):
        student_id = input("Enter the student id: ")
        student_name = input("Enter the student name: ")
        dob = input("Enter day of birth:")
        students[student_id] = Student(student_id, student_name, dob)
    # Write student information to students.txt
    with open("students.txt", 'a') as f:  
        for student_id, student in students.items():
            student_info = f"{student_id}\t {student.get_name()}\t {student.get_dob()}\n"
            f.write(student_info)
    
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
    # Write course information to courses.txt
    with open("courses.txt", 'a') as f:  
        for course_id, course in courses.items():
            course_info = f"{course_id}\t {course.get_name()}\t {course.get_credit()}\n"
            f.write(course_info)
    

def mark_input(students, courses):
    courseID = input("Enter the course ID you want to input marks: ")
    if courseID not in courses.keys():
        print("Invalid Course Id! Please enter a valid one.")
    else:
        filename = r"C:\Users\buing\Downloads\pp2024\check5\marks.txt"
        with open(filename, 'a') as f:  
            f.write(f" Marks for course {courses[courseID].get_name()}({courseID} )\n")
            for studentID, student in students.items():
                new_mark = float(input(f"Enter mark for {student.get_name()}: "))
                student.get_marks()[courseID] = new_mark
                mark_info = f"{studentID}\t \t {new_mark}\n"
                f.write(mark_info)


def compress_data(files, output_file):
    # Open the output file in binary write mode ('wb')
    with open(output_file, 'wb') as f_out:
        # Create a zlib compression object with default compression level
        compressor = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED)

        # Iterate over each input file
        for file in files:
            # Open the current input file in binary read mode ('rb')
            with open(file, 'rb') as f_in:
                # Read the content of the input file
                file_content = f_in.read()
                # Compress the file content using the compressor object
                compressed_data = compressor.compress(file_content)
                
                # Write the compressed data to the output file
                f_out.write(compressed_data)
        
        # Flush any remaining compressed data to the output file
        f_out.write(compressor.flush())



def decompress_data(input_file, output_file):
    with open(input_file, 'rb') as f_in:
        compressed_data = f_in.read()
        decompressed_data = zlib.decompress(compressed_data)
        
        with open(output_file, 'w') as f_out:
            f_out.write(decompressed_data.decode())





    

        