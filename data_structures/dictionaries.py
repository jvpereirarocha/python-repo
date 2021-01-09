"""
    Python concepts and methods about dictionaries
"""

# Creating a dictionary
person = {
    "name": "João",
    "last_name": "Rocha",
    "date_of_birth": "1997-02-27",
    "profession": "Programmer"
}

# Type of dict: <class 'dict'>
print(type(person))

# Accessing items from dictionary
name = person["name"]
print("The name is:", name)

#Another way is:
profession = person.get("profession")
print("The profession is:", profession)

# Get keys from dictionary
all_keys = person.keys() # Returns a type dict_keys
print("Keys from dictionary:", all_keys)
print(type(all_keys))

# Get values from dictionary
all_values = person.values() # Returns a type dict_values
print("Values from dictionary:", all_values)

# Get key/values from dictionary
keys_values = person.items() # Returns a type dict_items with tuples of key and value
print("Key/values from dictionary:", keys_values)


# Loop dictionaries
for p in person:
    print("p:", p) # Returns each key from dict
print("\n\n")

for k in person.keys():
    print("k:", k) # Also returns each key from dict
print("\n\n")

for v in person.values():
    print("v:",v) # Returns each value from dict
print("\n\n")

for key, value in person.items():
    print(f"The key is '{key}' and the value is '{value}'")

print("\n\n")

# Changing dictionaries
print("Dict before change:", person)
person["name"] = "João Victor" # Changing the value from the key name
print("Dict after change:", person)

# update() method
print("Last Name before update:", person['last_name'])
person.update({"last_name": "Pereira Rocha"}) # dict.update({key:new_value})
print("Last Name after update:", person['last_name'])


# Removing keys from dictionaries
# pop() method
print("Dict before pop:", person)
person.pop("date_of_birth") # dict.pop(key)
print("Dict after pop:", person)

#popitem method
print("Before popitem method:", person)
person.popitem() # In versions before 3.7 from python, a random item is removed. In python 3.7 or greather, the last element is removed
print("After popitem method:", person)

# del keyword
# To remove a specific key, it is possible use the keyword del. See below:
print("Before del keyword:", person)
del person['last_name']
print("After del keyword:", person)

# Also it is possible delete all the dictionary with keyword del. See below:
print("Before del all the dict:", person)
del person
# print("After del all the dict:", person) # Will raise an Exception NameError

# clear() method
team = {
    "name": "Borussia Dortmund",
    "country": "Germany"
}
print("Dict before clear method:", team)
team.clear()
print("Dict after clear method:", team)

# fromkeys method
keys = ("name", "name_again", "one_more_name")
values = "Joao"
data = dict.fromkeys(keys, values) # set from the keys name, name_again and one_more_name the value Joao
print("data:", data)

#copy dict
person1 = {"name": "Joao", "age": 23}
person2 = person1.copy() # Create a copy from a specified dict
print("The person1 is:", person1)
print("The person2 is:", person2)
