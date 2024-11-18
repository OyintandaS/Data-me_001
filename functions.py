# TODO: Implement the following functions based on the descriptions.

def reverse_list(lst):
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    lst = [3, 2, 1]  # Implement this
    lst[1:1:-1]
    return lst

def count_occurrences(lst, element):
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    element = 0
    lst = ["There were so many ducks at the ducks show"]
    for i in lst:
        if i == "ducks":
            element += 1
        return element

def get_keys_with_value(dct, value):
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    dct = {"a":1,
           "b":2,
           "c":3
           
        }  # Implement this
    for key, value in dct:
        return key

def merge_sorted_lists(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
lst1 = [1, 2, 3] # Implement this
lst2 = [4, 5, ]
lst1.merge(lst2) 

def find_second_largest(numbers):
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
    pass  # Implement this

def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    str1 = "listen"  # Implement this
    str2 = "silent"
    for i in str1:
        if i in str2:
            return True
        else:
            False


def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    pass  # Implement this


def remove_duplicates(lst):
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    lst = [1, 2, 3, 1, 1, 6, 7, 8, 9, 1, 1] # Implement this
    j = 1
    for i in lst:
        if j == i:
            j.remove(j)
        return lst

def find_common_elements(lst1, lst2):
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    pass  # Implement this