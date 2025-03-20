#  Create an empty list
my_list = []

#  Append elements 10, 20, 30, 40
my_list.extend([10, 20, 30, 40])

#  Insert value 15 at the second position
my_list.insert(1, 15)

#  Extend the list with [50, 60, 70]
my_list.extend([50, 60, 70])

# Remove the last element
my_list.pop()

#  Sort the list in ascending order
my_list.sort()

#  Find and print the index of the value 30
index_of_30 = my_list.index(30)
print(f"Sorted List: {my_list}")
print(f"Index of 30: {index_of_30}")
