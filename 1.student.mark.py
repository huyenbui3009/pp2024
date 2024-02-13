#-------------------------------------------INPUT FUNCTIONS----------------------
students={}
def student_input():
    student_num= int(input("Enter the number of students: "))
    for i in range(student_num):
        student_id= input("Enter the student id: ")
        student_name=input("Enter the student name: ")
        dob= input("Enter day of birth:")
        students[student_id]={"name": student_name, "DoB": dob}
    return  students
student_input()

courses={}
def course_input():
    course_num= int(input("Enter the number  of courses:"))
    for  i in range(course_num):
        course_id= input("Enter the course id: ")
        if course_id in courses.keys():
            print("Course already exists. Skipping...")
            continue
        course_name= input("Enter the course name: ")
        courses[course_id]={"name": course_name}
    
course_input()


marks = {}
def mark_input():
    courseID = input("Enter the course ID you want to input marks: ")
    if courseID not in courses.keys():
        print("Invalid Course Id! Please enter a valid one.")
    else:
        for studentID in students:
            if studentID not in marks:
                marks[studentID] = {}  # Initializing
            newmark = float(input(f"Enter mark for the student {students[studentID]['name']}: "))
            marks[studentID][courseID] = newmark
    return marks
mark_input()
#--------------------------------------------LIST FUNCTIONS ----------------------

def listcourse():
    for id, course in courses.items():
        print(id,":", course["name"])
def liststudent():
    for id, info in students.items():
        print("\n ID:", id)
        name=info['name']
        dob=info['DoB']
        print("\tName : ", name.title())
        print("\tDate Of Birth : ", dob.title())

def showmarks():
    courseid= input("enter course id to show mark: ")
    if courseid not in courses:
        print("The course is not available")
        return
    else:
        for studentid, mark in marks.items():
            if courseid in mark:
                print(f"{students[studentid]['name']}: {marks[studentid][courseid]}")
            else:
                print(studentid + ": No mark available ")

listcourse()
liststudent()
showmarks()



