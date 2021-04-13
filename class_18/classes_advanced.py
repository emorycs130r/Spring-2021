# Create a program for mapping who lives where

# Class for houses -- Address, ID, Type, Rooms, Rent

class House():

    def __init__(self, id_, name, type_, rooms, rent):

        self.id = id_
        self.name = name
        self.type = type_
        self.rooms = rooms
        self.rent = rent
    
    
    def print_(self):

        print("The parameters of the house are: ")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Rooms: {self.rooms}")
        print(f"Rent: {self.rent}")
        print("==================")


# Class for people -- ID, HouseID, Type (student, working)


class People():

    def __init__(self, id_, house_id, type_):

        self.id = id_
        self.house_id = house_id
        self.type = type_

    def print_(self):

        print("The parameters of people is")
        print(f"ID: {self.id}")
        print(f"House ID: {self.house_id}")
        print(f"Type: {self.type}")
        print("==============   ")

    def change_house_id(self, house_id):
        
        self.house_id = house_id

if __name__ == "__main__":

    house_1 = House(1, "Appt #10", "Appt", 3, 2000)
    house_1.print_()

    person_1 = People(1, 1, "Student")
    person_1.print_()

    print("Changing houses")
    person_1.change_house_id(2)
    person_1.print_()