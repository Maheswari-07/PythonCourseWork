#1.Converting to int
int_a=2
print(float(int_a))#Output:2.0
print(str(int_a))#Output:2
print(bool(int_a))#Output:True

#2. Converting to float
float_a=3.14
print(int(float_a))#Output:3
print(str(float_a))#Output:3.14
print(bool(float_a))#Output:True

#3. Converting to string
string_a="Hello"
print(list(string_a))#Output:['H', 'e', 'l', 'l', 'o']
print(tuple(string_a))#Output:('H', 'e', 'l', 'l', 'o')
print(set(string_a))#Output:{'l', 'e', 'o', 'H'}

#4. Converting to list
list_a=[1,2,3,4]
print(bool(list_a))#Output: True
print(tuple(list_a))#Output: (1, 2, 3, 4)
print(set(list_a))#Output: {1, 2, 3, 4}
print(str(list_a))#Output: [1, 2, 3, 4]

#5. Converting to tuple
tuple_a=(1,2,3,4)
print(bool(tuple_a)) #Output: True
print(list(tuple_a))#Output: [1, 2, 3, 4]
print(set(tuple_a))#Output: {1, 2, 3, 4}
print(str(tuple_a))#Output: (1, 2, 3, 4)

#6. Converting to set
set_a={1,2,3,4}
print(bool(set_a))#Output: True
print(list(set_a))#Output: [1, 2, 3, 4]
print(tuple(set_a))#Output: (1, 2, 3, 4)
print(str(set_a))#Output: {1, 2, 3, 4}

#7. Converting to dictionary
dict_a={"name":"mahi","age":21}
print(str(dict_a))#Output: {'name': 'mahi', 'age': 21}
print(bool(dict_a))#Output: True
print(list(dict_a))#Output: ['name', 'age']
print(tuple(dict_a))#Output: ('name', 'age')
print(set(dict_a))#Output: {'age', 'name'}

#8. Coverting to boolean
bool_a=False
print(str(bool_a))#Output: False
print(int(bool_a))#Output: 0
print(float(bool_a))#Output: 0.0

#9.Dictionary Conversion
d=[('name','mahi'),('course','Python')]
print(dict(d))#Output: {'name': 'mahi', 'course': 'Python'}
