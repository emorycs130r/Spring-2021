'''

Search for the grade of a student in class. 

'''
from util import generate_grade_dict


def search_student_details(student_name):
    
    student_list = generate_grade_dict()
    print(student_list)
    for student in student_list:
        if student['id'] == student_name:
            return student
        
    return False


if __name__ == "__main__":
    result = search_student_details(7)
    if not result:
        print("Student not found")
    else:
        print(f"The student is: {result}")
