'''

Create a dictionary from the following list of students with grade: 

bob - A
alice - B+
luke - B
eric - C

Get input of name from user using the "input()" and use it to display grade. 
If the name isn't present, display "Student not found" -- INGORE


'''

def get_grade(student_name):

    temp_dict = {
        "bob": "A",
        "alice": "B+",
        "luke": "B",
        "eric": "C"
    }

    student_names = temp_dict.keys()

    if student_name in student_names:
        return temp_dict[student_name]
    else:
        return "Student Not Found"

def get_grade_1(student_name):

    temp_dict = {
        "bob": "A",
        "alice": "B+",
        "luke": "B",
        "eric": "C"
    }

    grade = temp_dict.get(student_name, "Student Not Found")

    return grade
    
if __name__ == "__main__":

    name = input("Enter student name: ")
    grd = get_grade(name)
    print(f"The grade is: {grd}")