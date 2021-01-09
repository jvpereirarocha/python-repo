"""
    Python list concepts and methods
"""
numbers = [x for x in range(0, 11)] # Numbers from 0 to 10 # Generate a list with 100 numbers

print("First element: ", numbers[0]) # First element from list
print("Last element: ", numbers[-1]) # Last element from list
print("Another way to show the last element: ", numbers[len(numbers) - 1]) # Another way to get the last element from list

number_two = numbers.count(2) # How many times the number two appears?
print("Number two: ", number_two)


names = ['Josh', 'Harry', 'James', 'George']

# Removing element
print("The list from names before remove is: ", names)
names.remove('Josh')
print("The list from names after remove is: ", names)
names.pop(2) # Removing element at the position 3
print("Names after pop the element at the position 2: ", names)

#Inserting element
names.append('Aaron') # Insert the element at the last position
print("The list after append is: ", names)
names.insert(2, "Joseph") # insert(position, element)
print("The list after insert at the position 2 is: ", names)

#Slice elements
excludes_the_last = names[:len(names)-1]
print(excludes_the_last) # Showing the elements from list, excluding the last
excludes_the_first = names[1:] # Showing the elements from list, excluding the first
print(excludes_the_first)

#Get the index from element
get_index = names.index('Aaron')
print(get_index) # Returns 3 because Aaron is in the position 3

# Copying the list
names_two = names.copy()
print("The copy from the list names: ", names_two)

# Reversing the list
names_two.reverse()
print("The reversed list names_two is: ", names_two)

# Extending the list
more_numbers = [x for x in range(11, 21)]
numbers.extend(more_numbers) # list.extend(iterable)
print("Numbers: ", numbers)

# Sorting the list
names.sort(reverse=False) # If is true, then the order is reversed
print("Sorting the list name: ", names) #alphabetical order
