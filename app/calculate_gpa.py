import data_storage

def page():
    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("GPA Calculation Page\n")
        print("1.Calculate Semester wise GPA\n2.Calculate CGPA\n3.Custom\n4.back\n")

        choice = input("Enter Your Choice: ")
        print("")

        if (int(choice) == 1):
            calculate_SGPA()
            break
        elif(int(choice) == 2):
            calculate_CGPA()
            break
        elif(int(choice) == 3):
            custom_GPA()
            break
        elif(int(choice) == 4):
            break
        else:
            print("Invalid Choice!")




def calculate_SGPA():
    return 0


def calculate_CGPA():
    return 0


def custom_GPA():
    return 0


def back():
    return 0


