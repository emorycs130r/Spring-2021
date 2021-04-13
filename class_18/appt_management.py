from classes_advanced import House, People
import random

def init_houses():

    house_list = []
    random.seed(42)
    for i in range(10):
        
        house_1 = House(f"{i+1}", f"Appt {i+i}", "Appt", random.randint(1,3), random.randint(1000, 2000))
        house_list.append(house_1)

    return house_list


def init_people():

    people_list = []
    random.seed(42)

    type_list = ["Student", "Working"]
    for i in range(100):

        person_1 = People(f"{i+1}", random.randint(1, 10), type_list[random.randint(0,1)])
        people_list.append(person_1)
    
    return people_list


# def print_people_id(people_list, id_):

#     for person in people_list:
#         if person.id == id_:
#             person.print_()

def find_people_in_apartment(house_list, people_list, appt_no):
    
    house_1 = None
    for house in house_list:
        if appt_no in house.name:
            house_1 = house
    
    house_1.print_()

    for person in people_list:
        # print(person.print_())
        if str(person.house_id) == house_1.id:
            person.print_()
        # input()
    


if __name__ == "__main__":

    houses_list = init_houses()

    # for house in houses_list:
    #     house.print_()

    people_list = init_people()
    # for person in people_list:
    #     person.print_()

    find_people_in_apartment(houses_list, people_list, "Appt 12")