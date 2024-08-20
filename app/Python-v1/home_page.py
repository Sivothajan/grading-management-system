import add_courses
import calculate_gpa
import remove_courses
import data_storage

while True:
    print("**********************************************************************")
    print("Welcome to the GPA Calculator!\n")

    print("1.Add Courses\n2.Calculate GPA\n3.Remove Courses\n4.Exit\n")

    choice = input("Enter your Choice: ")
    print("")

    if(int(choice) == 1):
        add_courses.new()
    elif(int(choice) == 2):
        calculate_gpa.page()
    elif(int(choice) == 3):
        remove_courses.remove()
    elif(int(choice) == 4):
        data_storage.save_data_json()
        print("Exited!")
        break
    else:
        print("Invalid Choice!")
        
