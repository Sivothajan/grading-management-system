import data_storage

def remove():
    print("----------------------------------------------------------------------")
    print("Welcome to the Course Removal Page.\n\n(Enter letter 'b' to back.)\n")

    while True:
        course_code = str(input("Enter Course Code: "))
        if course_code.lower() == 'b':
            break
        if course_code in data_storage.data:
            del data_storage.data[course_code]
            break
        else:
            print(f"The Course Code: {course_code} is not exist!")

