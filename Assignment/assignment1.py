# -----------------------------
# Ajio Product Listing & Order Summary
# -----------------------------

# Input Section

# Product Details
product_id = int(input("Enter Product ID: "))
product_name = input("Enter Product Name: ")
brand_name = input("Enter Brand Name: ")
price = float(input("Enter Product Price: ₹"))
size_input = input("Available Sizes (comma-separated): ")
sizes = [s.strip().upper() for s in size_input.split(',')]

color = input("Enter Product Color: ")
discount_percent = float(input("Enter Discount Percentage: "))

# Stock Details
available_units = int(input("Enter Available Stock Units: "))
sold_units = int(input("Enter Sold Units: "))
stock = (available_units, sold_units)

# Product Tags (Set)
tags_input = input("Enter Product Tags (comma-separated): ")
tags = set(tag.strip().title() for tag in tags_input.split(','))

# Seller Info (Dictionary)
seller_name = input("Enter Seller Name: ")
seller_location = input("Enter Seller Location: ")
seller_contact = input("Enter Seller Contact Number: ")
seller_info = {
    "Name": seller_name,
    "Location": seller_location,
    "Contact": seller_contact
}

# Order Details
ordered_quantity = int(input("Enter Quantity to Order: "))
payment_method = input("Enter Payment Method (Card/UPI/COD): ").strip()

# Calculations
discounted_price = price - (price * discount_percent / 100)
total_price = discounted_price * ordered_quantity

# -----------------------------
# Output Section
# -----------------------------

print("\n--- Ajio Product Summary ---")

# 1. Comma Separation
print("\n1. Using Comma Separation (sep=','):")
print("Product ID, Name, Brand:", product_id, product_name, brand_name, sep=', ')

# 2. Percentage Formatting
print("\n2. Using Percentage Formatting (% operator):")
print("Discount Applied: %.2f%%" % discount_percent)

# 3. Using f-strings
print("\n3. Using f-strings:")
print(f"Product: {product_name} by {brand_name}")
print(f"Color: {color}")
print(f"Available Sizes: {', '.join(sizes)}")
print(f"Price after discount: ₹{discounted_price:.2f}")
print(f"Ordered Quantity: {ordered_quantity}")
print(f"Total Payable Amount: ₹{total_price:.2f}")
print(f"Payment Method: {payment_method}")
print(f"Stock Available: {stock[0]} units")

# 4. Using .format() method
print("\n4. Using .format() method:")
print("Seller Info: Name - {}, Location - {}, Contact - {}".format(
    seller_info['Name'], seller_info['Location'], seller_info['Contact']))

# Additional Details
print("\nOther Product Tags: {}".format(", ".join(tags)))
print("Sold Units So Far: {}".format(stock[1]))

print("\n--- Thank you for shopping with Ajio! ---")

