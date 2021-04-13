

class ContactCard():

    def __init__(self, id, name, addr, phno):

        self.id = id
        self.name = name
        self.ph_no = phno
        self.address = addr
        self.is_active = True

    def print_(self): # Can't use print because its a keyword
        
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.ph_no}")
        print(f"Is Active: {self.is_active}")


    def deactivate(self):
        self.is_active = False
    
    def change_phone(self, phone):

        self.ph_no = phone
    

def print_outside(contact_object):
    
    print(f"ID: {contact_object.id}")
    print(f"Name: {contact_object.name}")
    print(f"Address: {contact_object.address}")
    print(f"Phone Number: {contact_object.ph_no}")
    print(f"Is Active: {contact_object.is_active}")


def print_contact_list(contact_list):
    
    for contact in contact_list:
        contact.print_()
        print("==================")


def deactivate_id(contact_list, id_):

    for contact in contact_list:

        if contact.id == id_: # self.id
            contact.deactivate()

        '''
        if contact.ph_no == phno:
            contact.deactivate()
        '''

# Write a function to update the phone number of a particular ID

def modify_phone_by_id(contact_list, id_, phno):

    for contact in contact_list:
        if contact.id == id_:
            contact.change_phone(phno)
    
    

if __name__ == "__main__":

    contact_1 = ContactCard(1, "John", "Address 1", "1234567890")
    contact_2 = ContactCard(2, "John", "Address 1", "1234567890")
    contact_3 = ContactCard(3, "John", "Address 1", "1234567890")
    contact_4 = ContactCard(4, "John", "Address 1", "1234567890")
    contact_5 = ContactCard(5, "John", "Address 1", "1234567890")
    contact_6 = ContactCard(6, "John", "Address 1", "1234567890")

    contact_list_ = [contact_1, contact_2, contact_3, contact_4, contact_5, contact_6]

    print_contact_list(contact_list_)

    deactivate_id(contact_list_, 2)

    print_contact_list(contact_list_)
