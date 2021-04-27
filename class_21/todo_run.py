from todo_list import TodoList, create_new_todo, read_data_from_file, write_list_to_file, convert_to_dictionary, STATUS_DICT


def run():
    
    todo_array = read_data_from_file()
    while True:
        print("1. Create \n2. Read \n3. Update \n4. Delete \n5. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            print("Create new Todo")
            task = input("Enter new task: ")
            todo_array = create_new_todo(todo_array, task)
        
        if choice == 2:
            print('1. Read all record \n2. Search for criteria \n3. Priority')
            read_choice = int(input("Enter your choice: "))
            if read_choice == 1:
                for todo in todo_array:
                    print(f"{todo.id}, {todo.task}, {todo.status}, {todo.priority}")

            if read_choice == 2:
                
                print("0. Created \n1. In progress \n2. Completed \n3. Deleted")
                status_choice = int(input("Enter your choice: "))
                for todo in todo_array:
                    if STATUS_DICT[status_choice] == todo.status:
                        todo.print_()
                        print("================")
            if read_choice == 3:
                print("Enter a priority (1 - 10)")
                priority_choice = int(input("Enter your choice: "))
                for todo in todo_array:
                    if priority_choice < todo.priority:
                        todo.print_()
                        print("================")
                # Print items of priority more than user's input. 
                


        if choice == 3:
            print("Modifying status.")
            id_ = input("Enter the ID you want to modify: ")

            print("1. Status \n2. Task")
            modify_choice = int(input("Enter modifying choice: "))
            if modify_choice == 1:
                new_status = int(input("1. In Progress \n2. Completed \n3. Deleted\n"))
                for row in todo_array:
                    if row.id == id_:
                        row.modify_status(STATUS_DICT[new_status])
                        print("Successfuly modified the status")

            if modify_choice == 2:
                new_task = input("Enter the new task for the ID")
                for row in todo_array:
                    if row.id == id_:
                        row.modify_task(new_task)
                        print("Successfuly modified the task")
            # Modify this block such that you're modifying the task or status for a particular ID. 

        if choice == 5:
            todo_list_dict = convert_to_dictionary(todo_array)
            write_list_to_file(todo_list_dict)
            print("Exiting application. Bye!")
            exit()

if __name__ == "__main__":
    run()