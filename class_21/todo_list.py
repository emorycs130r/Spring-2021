from util import get_id
import arrow
import csv


STATUS_DICT = {
    0: "Created",
    1: "In Progress",
    2: "Completed",
    3: "Deleted"
}

class TodoList():
    
    def __init__(self, id_, task):

        self.id = get_id(id_)
        self.task = task
        self.status = "Created"
        self.priority = 4 # First change
        self.date_created = arrow.now('US/Eastern')
        self.date_modified = arrow.now('US/Eastern')

    # Write a function to print the todo object
    def print_(self):
        print(f"{self.id}")
        print(f"Task: {self.task}")
        print(f"Status: {self.status}")
        print(f"Priority: {self.priority}")
        print(f"Date Created: {self.date_created}")
        print(f"Date Modified: {self.date_modified}")

    def dict_(self):

        todo_dict = {
            'id': self.id,
            'task': self.task,
            'status': self.status,
            'date_created': str(self.date_created),
            'date_modified': str(self.date_modified), 
            'priority': self.priority
        }
        return todo_dict
    
    def modify_(self, todo_dict):
        
        self.id = todo_dict['id']
        self.task = todo_dict['task']
        self.status = todo_dict['status']
        self.date_created = arrow.get(todo_dict['date_created'])
        self.date_modified = arrow.get(todo_dict['date_modified'])
        if 'priority' in todo_dict.keys():
            self.priority = int(todo_dict['priority'])
        else:
            self.priority = 4
    
    def modify_status(self, new_status):

        self.status = new_status
        self.date_modified = arrow.now('US/Eastern')
    
    def modify_task(self, new_task):

        self.task = new_task
        self.date_modified = arrow.now('US/Eastern')


def convert_to_dictionary(list_of_todo):

    return [x.dict_() for x in list_of_todo]

def write_list_to_file(todo_dictionary):
    
    csv_fd = open('todo_list.csv', 'w')
    csv_writer = csv.DictWriter(csv_fd, fieldnames=list(todo_dictionary[0].keys()))
    csv_writer.writeheader()
    csv_writer.writerows(todo_dictionary)

    csv_fd.close()

def read_data_from_file():

    try: 
        csv_fd = open('todo_list.csv', 'r')
    except Exception as e:
        return []
    
    csv_reader = csv.DictReader(csv_fd)

    list_todos = []
    for row in csv_reader:
        temp_todo = TodoList(-1, "Dummy")
        temp_todo.modify_(row)
        list_todos.append(temp_todo)
    return list_todos


def create_new_todo(todo_list_array, task):
    
    new_id = len(todo_list_array)
    todo_object = TodoList(new_id, task)
    todo_list_array.append(todo_object)
    return todo_list_array

if __name__ == "__main__":

    # todo_object_1 = TodoList(0, "Finish grading Assignment 5")
    # todo_object_2 = TodoList(1, "Finish grading Project 2")
    # todo_object_3 = TodoList(2, "Finish cooking for dinner")
    # todo_object_4 = TodoList(3, "Work on project paper draft")
    # todo_object_5 = TodoList(4, "Water the plants")

    # list_todos = [todo_object_1, todo_object_2, todo_object_3, todo_object_4, todo_object_5]
    # todo_dict = convert_to_dictionary(list_todos)

    # write_list_to_file(todo_dict)
    # print(todo_object_1.__dict__)
    # print(todo_object_1.dict_())
    todo_lists = read_data_from_file()
    print(todo_lists)


