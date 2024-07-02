import main_quest as mq
horcrux_of_koshchei = mq.horcrux_of_koshchei

## YOUR CODE HERE



# HINTS

## Function to check the TYPE of the object (list, dict, string, etc.):
# type(horcrux_of_koshchei)

# Some DICTIONARY methods to access keys, values, or key-value pairs:
# Full list of dictionary methods: https://www.w3schools.com/python/python_ref_dictionary.asp

# my_dict.keys() - lists keys of the dictionary
# my_dict.values() - lists values of the dictionary
# my_dict.items() - lists key-value pairs of the dictionary

# Access VALUES of the KEYS in the dictionary:
# my_dict["key_name"] - access by key name
# my_dict["rabbit"]["duck"]["egg"] - access `egg` inside `duck`, inside `rabbit`, inside `my_dict` object

# Access LISTS embedded inside the DICTIONARY:
# my_dict = {'key_name': ['index zero', 'index one', 'index two']}
# my_dict["key_name"][1] == "index one"

# Code Examples:
# print(type(horcrux_of_koshchei))
# print('====>> Items:\n', horcrux_of_koshchei.items() )
# print('====>> Values:\n', horcrux_of_koshchei.values() )
# print('====>> Keys:\n', horcrux_of_koshchei.keys() )

# More Hints:

# Use the type() function to understand what kind of object you are dealing with:
# e.g., type(horcrux_of_koshchei['Buyan Island']) might return <class 'dict'> or <class 'list'>

# Explore nested objects step by step, and keep track of where you are:
# e.g., 
#       island = horcrux_of_koshchei['Buyan Island']
#       oak_tree = island['Ancient Oak']
#       rabbit = oak_tree[0]['rabbit']


# Remember to use print statements to debug and see the structure of each object:
# print(island) # prints whole object
# print(island.keys()) # list keys of an object
# print(oak_tree)
# print(rabbit)


# Keep in mind that lists are indexed by numbers, and dictionaries are accessed by keys.
# You may need to combine these approaches to navigate through complex structures.

# Have fun exploring, and good luck finding the needle to defeat Koshchei the Immortal!
