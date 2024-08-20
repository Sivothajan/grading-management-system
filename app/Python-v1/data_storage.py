import json

data = {}


def save_data(course_code, semester, course_credit, course_gpv):
        data[course_code] = {
        "Semester":semester,
        "Course Credit":course_credit, 
        "Course GPV":course_gpv
    }
        

def save_data_json():
    data_json = json.dumps(data)
    f = open("data_json.json", "w")
    f.write(data_json)
    f.close()
    print("Exit Successfully!")

