import validate_input
import data_storage 


def new():
    while True:
        semester = input("\nEnter Semester Number: ")
        if semester not in validate_input.allowed_semester:
            print("Invalid Semester")
        else:
            break

    while True:
        course_code = input("Enter Course Code: ")
        if course_code not in validate_input.allowed_course_code:
            print("Invalid Course Code!")
        else:
            break

    while True:
        course_credit = int(input("Enter Course Credit: "))
        if course_credit not in validate_input.allowed_credit:
            print("Invalid Course Credit!")
        else:
            break

    while True:
        course_gpv = float(input("Enter Course GPV: "))
        if course_gpv not in validate_input.allowed_gpv:
            print("Invalid GPV!")
        else:
            break
    
    data_storage.save_data(course_code, semester, course_credit, course_gpv)   

