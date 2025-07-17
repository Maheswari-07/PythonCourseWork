#1. String Input
a=input("enter a string:")
print(a)#Output: Hi

#2. Integer Input
b=int(input("Enter a value:"))
print(b)#Output: 2

#3. Float Input
c=float(input("enter a decimal value:"))
print(c)#Output: 3.14

#4.1. Input as List (Space-separated)
names=input("Enter names(space seperated)").split()
print(names)#Output: ['mahi', 'kiran', 'vihan']

#5. Input as List (Comma-separated)
names=input("Enter names(comma seperated)").split(",")
print(names)#Ouput: ['  mahi', ' kiran', ' vihan']

#6. List of Integers
marks = list(map(int, input("Enter marks: ").split()))
print(marks)#Ouput: [53, 98, 68, 80]

#7. List of Floats
marks = list(map(float, input("Enter marks: ").split()))
print(marks)#Output: [23.5, 36.7, 45.8]

#8. Tuple Input
dimensions = tuple(map(int, input("Enter length, width,height: ").split()))
print(dimensions)#Output: (10, 20, 15)

#9. Set Input
selected_ids = set(map(int, input("Enter selected image IDs:").split()))
print(selected_ids)#Output: {101, 102, 103, 104}

#10. Dictionary Input using eval()
profile=eval("Enter dict values:")
print(profile)#Output: {'name': 'sreya', 'age': 30, 'role': 'admin'}

#11. Multiple Inputs with Unpacking
username,password=input("Enter username and password:")
print("Username:",username)#Output: Username: user01
print("Password:",password)#Output: mypassword123
