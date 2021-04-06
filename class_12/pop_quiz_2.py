'''

Create a list of dictionaries with all your classes and print if the class is on Tu Th. Dictionary format should be:

{
    class_code:"CS130R"
    class_name: "Python Programmnig"
    days: "TuTh" or "MoWe"
}


'''

def check_class():

    class_list = [
        {'class_code':"CS130R",'class_name': "Python Programmnig",'days': "TuTh"},
        {'class_code':"CS170",'class_name': "Java Programmnig",'days': "MoWe"},
        {'class_code':"MA101",'class_name': "Algebra 101",'days': "TuTh"}
    ]
    for class_ in class_list:
        if class_["days"] == "TuTh":
            print(class_)

if __name__ == "__main__":
    check_class()