#Arithmetic Operators
a = 10
b = 30
print("Addition:",a + b) # Output: Addition: 40
print("Subtraction:",a - b) # Output: Subtraction: -20
print("Multiplication:",a * b) # Output: Multiplication: 300 
print("Division:",a / b) # Output: Division: 0.3333333333333333
print("Floor Division:",a // b) # Output: Floor Division: 0
print("Modulus:",a % b) # Output: Modulus:10
print("Exponentiation:",a ** b) # Output: Exponentiation: 1000000000000000000000000000000

#2. Comparison Operators
x = 20
y = 15
print(x == y) # Output: False
print(x != y) # Output: True
print(x > y) # Output: True
print(x < y) # Output: False
print(x >= 10) # Output: True
print(y <= 5) # Output: True

#3. Assignment Operators
x = 20
x+=5
print(x)# Output:25
print(x-5)# Output:20
print(x*5)# Output:125
print(x/5)# Output:5.0
print(x)# Output:25

#4. Logical Operators
x = 10
y = 20
print(x > 5 and y < 30) # Output: True 
print(x > 15 or y < 30) # Output: True 
print(not (x > 5)) # Output: False 

#5. Membership Operators
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits) # Output: True
print("grape" not in fruits) # Output: True
print("banana" not in fruits) #Output: False

#6. Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b) # Output: True (Both refer to the same object)
print(a is c) # Output: False (Different objects with the same content)
print(a is not c) # Output: True

#7. Bitwise Operators
x = 6 # Binary: 0101
y = 3 # Binary: 0011
print(x & y) # Output: 2 
print(x | y) # Output: 7 
print(x ^ y) # Output: 5 
print(~x) # Output: -7 
print(x << 1) # Output: 12 
print(x >> 1) # Output: 3
