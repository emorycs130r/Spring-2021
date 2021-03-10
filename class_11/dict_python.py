
id_card = {
    "name": "Vish",
    "phno": "1234567890",
    "addr": "400 Dowman Drive",
    "assgn_1": 40
}

# 3 Keys: name --> Vish, phno --> 1234567890, addr --> 400 Dowman Drive

# print(id_card["name"])
phone_number = "phno"
# print(id_card[phone_number])
# print(id_card["addr"])

print(type(id_card))

id_card["blood"] = "O" # Can only do if id_card already exists

# print(id_card["blood"])

print(id_card)

id_card["assgn_2"] = 50

id_card["name"] = "Bob"

print(id_card)