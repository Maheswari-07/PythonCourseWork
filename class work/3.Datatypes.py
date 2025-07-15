#Data Types
#1. Numeric Types
#a.int
a=10
print(a)
print(type(a))
#b.float
b=1.2
print(b)
print(type(b))
#c.complex
c=5+2j
print(c)
print(type(c))

#2. Sequence Types
#a. str 
a="Python"
print(a)
print(type(a))
#b. list
cart_items = ["Shoes", "T-shirt", "Headphones"]
print(cart_items)
print(type(cart_items))
#c. tuple
warehouse_location = (12.9716, 77.5946)
print(warehouse_location)
print(type(warehouse_location))

#3. Set Types
#a. set
available_sizes = {"S", "M", "L", "XL"}
print(available_sizes)
print(type(available_sizes))
#b. frozenset
frozen_tags = frozenset(["Sale", "Limited Edition","Trending"])
print(frozen_tags)
print(type(frozen_tags))

#4. Mapping Type
#a. dict
product_details = {
"name": "Wireless Mouse",
"brand": "Logitech",
"price": 899.99,
"rating": 4.5
}
print(product_details)
print(type(product_details))

#5. Boolean Type
is_logged_in = True
is_payment_successful = False
is_in_stock = True
print(is_logged_in)
print(is_payment_successful)
print(is_in_stock)

#6. None Type
tracking_number = None
delivery_partner = None
print(tracking_number)
print(delivery_partner)
