# my_programs.py

def merge_lists():
    print("🧠 Program: Merge Two Lists")
    print("""
def merge_lists(l1, l2):
    return l1 + l2
""")
    print("🧪 Test Case 1: merge_lists([1,2],[3,4]) -> [1,2,3,4]")
    print("🧪 Test Case 2: merge_lists(['a'],['b','c']) -> ['a','b','c']")
    print("📝 Explanation: Uses '+' operator to concatenate two lists.")


def remove_negatives():
    print("🧠 Program: Remove Negative Numbers from List")
    print("""
def remove_negatives(lst):
    return [x for x in lst if x >= 0]
""")
    print("🧪 Test Case 1: remove_negatives([-1,2,-3,4]) -> [2,4]")
    print("🧪 Test Case 2: remove_negatives([0,-5,10]) -> [0,10]")
    print("📝 Explanation: Uses list comprehension to filter out negatives.")


def sort_ascending():
    print("🧠 Program: Sort List Ascending")
    print("""
def sort_ascending(lst):
    return sorted(lst)
""")
    print("🧪 Test Case 1: sort_ascending([3,1,2]) -> [1,2,3]")
    print("🧪 Test Case 2: sort_ascending([5,4,6]) -> [4,5,6]")
    print("📝 Explanation: Uses Python's built-in sorted() in ascending order.")


def sort_descending():
    print("🧠 Program: Sort List Descending")
    print("""
def sort_descending(lst):
    return sorted(lst, reverse=True)
""")
    print("🧪 Test Case 1: sort_descending([3,1,2]) -> [3,2,1]")
    print("🧪 Test Case 2: sort_descending([5,4,6]) -> [6,5,4]")
    print("📝 Explanation: Uses sorted() with reverse=True for descending order.")


def remove_key_dict():
    print("🧠 Program: Remove Key from Dictionary")
    print("""
def remove_key(d, key):
    if key in d:
        del d[key]
    return d
""")
    print("🧪 Test Case 1: remove_key({'a':1,'b':2}, 'a') -> {'b':2}")
    print("🧪 Test Case 2: remove_key({'x':5,'y':6}, 'z') -> {'x':5,'y':6}")
    print("📝 Explanation: Checks if key exists and deletes it using del.")


def dict_from_lists():
    print("🧠 Program: Create Dictionary from Two Lists")
    print("""
def dict_from_lists(keys, values):
    return dict(zip(keys, values))
""")
    print("🧪 Test Case 1: dict_from_lists(['a','b'],[1,2]) -> {'a':1,'b':2}")
    print("🧪 Test Case 2: dict_from_lists(['x','y'],[9,8]) -> {'x':9,'y':8}")
    print("📝 Explanation: Uses zip() to pair keys and values, then dict().")


def union_sets():
    print("🧠 Program: Union of Two Sets")
    print("""
def union_sets(s1, s2):
    return s1 | s2
""")
    print("🧪 Test Case 1: union_sets({1,2},{2,3}) -> {1,2,3}")
    print("🧪 Test Case 2: union_sets({'a'},{'b'}) -> {'a','b'}")
    print("📝 Explanation: Uses '|' operator to combine unique elements.")


def intersection_sets():
    print("🧠 Program: Intersection of Two Sets")
    print("""
def intersection_sets(s1, s2):
    return s1 & s2
""")
    print("🧪 Test Case 1: intersection_sets({1,2},{2,3}) -> {2}")
    print("🧪 Test Case 2: intersection_sets({'a','b'},{'b','c'}) -> {'b'}")
    print("📝 Explanation: Uses '&' operator to find common elements.")


def difference_sets():
    print("🧠 Program: Difference of Two Sets")
    print("""
def difference_sets(s1, s2):
    return s1 - s2
""")
    print("🧪 Test Case 1: difference_sets({1,2,3},{2}) -> {1,3}")
    print("🧪 Test Case 2: difference_sets({'a','b'},{'b'}) -> {'a'}")
    print("📝 Explanation: Uses '-' operator to subtract elements of one set from another.")


def symmetric_difference_sets():
    print("🧠 Program: Symmetric Difference of Two Sets")
    print("""
def symmetric_difference_sets(s1, s2):
    return s1 ^ s2
""")
    print("🧪 Test Case 1: symmetric_difference_sets({1,2},{2,3}) -> {1,3}")
    print("🧪 Test Case 2: symmetric_difference_sets({'a','b'},{'b','c'}) -> {'a','c'}")
    print("📝 Explanation: Uses '^' operator to find elements in either set but not both.")
