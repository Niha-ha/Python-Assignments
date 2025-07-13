'''Write a function that sorts a list of strings alphabetically. 
["apple", "banana", "cherry", "kiwi", "grape"]'''


def sort_list_alphabetically(string_list):
    return sorted(string_list)                         

fruits = ["apple", "banana", "cherry", "kiwi", "grape"]
print("Sorted List:", sort_list_alphabetically(fruits))
