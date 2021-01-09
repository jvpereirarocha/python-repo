"""
    Python Tuples concepts and methods
"""

# Creating tuples
names = ("Aaron", "James", "Jack", "Harry")

# Another way to create tuples
countries = tuple(("Brazil", "England", "Germany", "Italy"))
print(countries)

# Returning specific element from tuple
print("The first element from tuple is: ", names[0])
print("The last element from tuple is: ", names[-1])

# Tuples are immutables. Is not possible add or remove elements in the tuples

# Getting the size from the tuple
print("The size from the tuple is: ", len(names))

# Countig appears from one specific element
count_brazil_appears = countries.count("Brazil")
print(f"Brazil appears {count_brazil_appears} time in the tuple")

# Searching for the first occurrence of the value 'Italy'
italy_position = countries.index("Italy")
print(f"Italy is in the position {italy_position}")

# If the element appears twice or more times in the tuple then index method will return the first occurrence
