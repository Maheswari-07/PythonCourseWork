#List defining
my_list = [] 
my_list2 = list()

#List with Elements
numbers = [1, 2, 3, 4, 5] # List of integers
print(numbers) #Output: [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"] # List of strings
print(fruits)#Output: ['apple', 'banana', 'cherry']
mixed = [10, "Python", 3.14, True] # Mixed data types
print(mixed)#Output: [10, 'Python', 3.14, True]

#List with Nested Lists
nested_list = [[1, 2, 3], ["a", "b", "c"], [True, False]]
print(nested_list) #Output:[[1, 2, 3], ['a', 'b', 'c'], [True, False]]
print(nested_list[1][2])#Output:c

#List using list() Constructor
list_from_tuple = list((1, 2, 3)) 
print(list_from_tuple) #Output: [1, 2, 3]
string_to_list = list("Python")
print(string_to_list)#Output: ['P', 'y', 't', 'h', 'o', 'n']

#3. Accessing Elements in a List
#3.1 Using Indexing
my_list = ["Python", "Java", "C++"]
print(my_list[2]) #Output: C++
print(my_list[-1]) #Output: C++
#3.2 Using Slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[0:3]) #Output: [10, 20, 30]
print(numbers[:4]) #Output: [10, 20, 30, 40]
print(numbers[3:]) #Output: [40, 50]
print(numbers[::-1]) #Output: [50, 40, 30, 20, 10]

#4. Modifying Lists
#4.1 Changing Elements
numbers = [10, 20, 30, 40]
numbers[3]=100
print(numbers) #Output: [10, 20, 30, 100]
#4.2 Adding Elements
numbers.append(50)
numbers.extend([1,2,3,4])
numbers.insert(1,13)
print(numbers) #Output: [10, 13, 20, 30, 100, 50, 1, 2, 3, 4]
#4.3 Removing Elements
numbers.remove(1)
print(numbers) #Output: [10, 13, 20, 30, 100, 50, 2, 3, 4]
numbers.pop()
print(numbers) #Output: [10, 13, 20, 30, 100, 50, 2, 3]
numbers.pop(2)
print(numbers) #Output: [10, 13, 30, 100, 50, 2, 3]
del numbers
numbers=[10, 13, 30, 100, 50, 2, 3]
numbers.clear

#5. List Methods
numbers = [3, 1, 4, 1, 5, 9]
print(numbers.count(1)) #Output: 2
print(numbers.index(4)) # Output:2
numbers.sort()
print(numbers) #Output: [1, 1, 3, 4, 5, 9]
numbers.reverse()
print(numbers) #Output: [9, 5, 4, 3, 1, 1]

#6. Copying a List
# Shallow Copy
list1 = [1, 2, 3]
list2 = list1.copy()
print(list2) #output: [1, 2, 3]

#7. Sorting and Reversing Lists
numbers = [5, 3, 8, 2]
numbers.sort() 
print(numbers)# [2, 3, 5, 8]
numbers.sort(reverse=True) 
print(numbers)# [8, 5, 3, 2]
numbers.reverse() # [2, 3, 5, 8]
print(numbers)
