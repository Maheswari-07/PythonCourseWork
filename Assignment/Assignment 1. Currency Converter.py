#Input Collection

conversion_id = int(input("Enter Conversion ID: "))
user_name = input("Enter Your Name: ")
from_currency = input("Enter From Currency (e.g., USD): ")
to_currency = input("Enter To Currency (e.g., INR): ")
amount = float(input("Enter Amount to Convert: "))
conversion_rate = float(input("Enter Conversion Rate: "))
fee_percent = float(input("Enter Fee Percentage: "))
supported_currencies = set(input("Enter Supported Currencies (comma-separated): ").split(","))
conversion_history = (amount, amount * conversion_rate)
agent_details = {
    "agent_name": input("Enter Agent Name: "),
    "agent_contact": input("Enter Agent Contact Number: "),
    "agent_location": input("Enter Agent Location: ")
}

# 1. Comma Separation
print("\n--- Conversion Summary ---")
print("Conversion ID, User, Amount:", conversion_id, user_name, amount, sep=",")

# 2. Percentage Formatting
print("Fee Applied: %.2f%%" % fee_percent)

# 3. f-strings
converted_amount = amount * conversion_rate
fee_amount = (fee_percent / 100) * amount
print(f"\nFrom: {from_currency}")
print(f"To: {to_currency}")
print(f"Amount: {amount}")
print(f"Conversion Rate: {conversion_rate}")
print(f"Converted Amount (Before Fee): {converted_amount}")
print(f"Fee Amount: ₹{fee_amount}")

print(f"Supported Currencies: {', '.join([cur.strip() for cur in supported_currencies])}")

# 4. .format() method
print("\nAgent Details: Name - {}, Contact - {}, Location - {}".format(
    agent_details["agent_name"], agent_details["agent_contact"], agent_details["agent_location"]
))
