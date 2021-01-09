"""
    Python concepts and methods about sets
"""

# Creating set
fruits = {"Apple", "Banana", "Strawberry", "Pineapple", "Orange"}
print("The fruits are:", fruits)

# Another way to create set
colors = set(("Blue", "Red", "Green", "Yellow"))
print("The colors are:", colors)

# Set is a collection unordered and unindexed. Also, isn't possible change sets but it's possible add items
# Sets cannot have two items with the same value

# Set with two items with the same value
countries = {"Brazil", "Argentina", "Italy", "Spain", "Argentina", "Japan"}
print("The countries are:", countries) # Argentina value will appears only once

# Size of set
print("The size of fruits set is:", len(fruits))

# Set can contain different data types (lists and tuples too)
different_types_set = {"Hello", True, 2.5, 1}

# Set methods

# the add() method
colors.add("Purple") # Adding color purple in the colors set
print("Set colors after add:", colors)

numbers = {1, 2, 3, 4, 5}
more_numbers = {4, 5, 6, 7, 8}
# the difference() method
print("The difference between numbers and more_numbers is:", numbers.difference(more_numbers))
# Returns {1, 2, 3} because 4 and 5 is on the two sets (numbers and more_numbers)

# Another way to get the difference between sets is
print("The difference between more_numbers and numbers is:", set(more_numbers - numbers))
# Returns {6, 7, 8} because 4 and 5 is on the two sets (more_numbers and numbers)

# the difference_update method
# This method remove elements that are in both sets
numbers.difference_update(more_numbers)
print("Numbers after difference_update are:", numbers)

# the intersection method
teams = {"Barcelona", "Real Madrid", "Juventus", "Bayern Munchen", "Borussia Dortmund"}
more_teams = {"Borussia Dortmund", "Liverpool", "Arsenal", "Manchester United", "Chelsea"}
print("The intersection of the both teams is:", teams.intersection(more_teams))

# the intersection_update method
# This method remove elements that aren't in other specified set
more_teams.intersection_update(teams)
print("The intersection_update is:", more_teams)

# the copy method
copy_by_numbers = numbers.copy()
print("The copy from numbers set is:", copy_by_numbers)


# The union method
numbers_1 = {x for x in range(1, 11)}
numbers_2 = {x for x in range(11, 21)}
print("The union from two sets is:", numbers_1.union(numbers_2))


# Set comprehension use this syntax {element for element in iterable}
# Example: Concat number value with the word 'Number'
number_prefix_set = {f"Number: {num}" for num in range(30, 41)}
print(number_prefix_set)


# Removing element from set
# The discard() method
names = {"José", "Joaquin", "João"}
print("Names before discard name:", names)
names.discard("José")
print("Names after discard name:", names)

# The remove() method
programming_languages = {"Python", "Javascript", "Ruby", "C++", "Java", "Swift"}
print("Programming Languages before remove:", programming_languages)
programming_languages.remove("C++")
print("Programming Languages after remove:", programming_languages)

# PS: The main difference between discard and remove is: If the element won't be found, remove()
    # will be raise an exception. Otherwise, the discard() will not raise an exception

# The pop() method
# This method remove a random element from the set
print("Programming Languages before pop:", programming_languages)
programming_languages.pop()
print("Programming Languages after pop:", programming_languages)
