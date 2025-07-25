product_id = int(input("Enter Product ID: "))
product_name = input("Enter Product Name: ")
price = float(input("Enter Price: "))
categories_input = input("Enter Categories (comma-separated): ")
categories = [cat.strip() for cat in categories_input.split(',')]
available_stock = int(input("Enter Available Stock: "))
sold_stock = int(input("Enter Sold Stock: "))
stock_details = (available_stock, sold_stock)
discount_percentage = float(input("Enter Discount Percentage: "))
features_input = input("Enter Product Features (comma-separated): ")
product_features = {feat.strip() for feat in features_input.split(',')}
supplier_name = input("Enter Supplier Name: ")
supplier_contact = input("Enter Supplier Contact Number: ")
supplier_location = input("Enter Supplier Location: ")
supplier_details = {
    "Name": supplier_name,
    "Contact": supplier_contact,
    "Location": supplier_location
}

print("\n1. Using Comma Separation (sep=',')")
print("Product ID, Name, Price:", product_id, product_name, price, sep=',')

print("\n2. Using Percentage Formatting (% operator)")
print("Product Discount: %.2f%%" % discount_percentage)

print("\n3. Using f-strings (f\"\")")
print(f"Product Name: {product_name}")
print(f"Price: ₹{price}")
print(f"Discount: {discount_percentage}%")
print(f"Stock Available: {stock_details[0]} units")

print("\n4. Using .format() method")
print("Supplier Details: Name - {0}, Contact - {1}, Location - {2}".format(
    supplier_details["Name"],
    supplier_details["Contact"],
    supplier_details["Location"]
))

print("\n--- Full Product Summary ---")
print(f"Product ID: {product_id}")
print(f"Categories: {', '.join(categories)}")
print(f"Stock (Available/Sold): {stock_details}")
print(f"Features: {', '.join(product_features)}")
