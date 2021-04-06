import random

def generate_grade_dict():

    student_names = ["Bob", "Alice", "John", "Jane", "Alex"]
    grades = ["A", "B+", "B-", "A", "B"]

    random.seed(10)
    random_list = []
    for i in range(5):
        grade_temp = dict()
        grade_temp["id"] = random.randint(0,10)
        grade_temp["name"] = student_names[random.randint(0,4)]
        grade_temp["grade"] = grades[random.randint(0,4)]
        random_list.append(grade_temp)
    
    return random_list