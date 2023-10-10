#multiple discounts calculator

# Get user input
price = float(input("Enter the price of the product: "))
category = input("Enter the category (A, B, or C): ").upper()
units = int(input("Enter the number of units purchased: "))

# Initialize discount variables
category_discount = 0
additional_discount = 0

# Apply category-specific discounts
if category == "A":
    category_discount = 10
elif category == "B":
    category_discount = 5
elif category == "C":
    category_discount = 2

# Apply additional discount for more than 10 units
if units > 10:
    additional_discount = 5

# Calculate the final price
total_discount = category_discount + additional_discount
discounted_price = price - (price * total_discount / 100)

# Display the result
print(f"Price before discount: ${price:.2f}")
print(f"Discount applied: {category_discount}%")
if additional_discount > 0:
    print(f"Additional discount applied (more than 10 units): {additional_discount}%")
print(f"Final price after discounts: ${discounted_price:.2f}")


#Retirement planning machine

# Get user input
current_age = int(input("Enter your current age: "))
retirement_age = int(input("Enter the age at which you plan to retire: "))
desired_amount = float(input("Enter the desired retirement amount: "))

# Calculate the number of years until retirement
years_until_retirement = retirement_age - current_age

# Define the expected annual investment return rate (as a decimal)
annual_return_rate = float(input("Enter the expected annual investment return rate (in percentage): ")) / 100

# Calculate the monthly interest rate
monthly_return_rate = annual_return_rate / 12

# Calculate the number of monthly payments in retirement
months_in_retirement = years_until_retirement * 12

# Calculate the required monthly payment using the formula
monthly_payment = desired_amount / ((1 + monthly_return_rate) ** months_in_retirement - 1) / monthly_return_rate

# Display the result
print(f"To reach your retirement goal, you need to save approximately ${monthly_payment:.2f} per month.")

#burned cals calculator

# Get user input
weight_kg = float(input("Enter your weight in kilograms: "))
duration_minutes = float(input("Enter the duration of the activity in minutes: "))
activity = input("Enter the type of activity (running, swimming, cycling, etc.): ").lower()

# Define calorie burn rates per minute for different activities (in calories per minute per kg)
calories_burn_rates = {
    "running": 0.076,
    "swimming": 0.059,
    "cycling": 0.042,
    
if activity in calories_burn_rates:
    # Calculate the calories burned based on the weight, duration, and activity
    calories_burned = weight_kg * calories_burn_rates[activity] * duration_minutes
    print(f"You burned approximately {calories_burned:.2f} calories while {activity}.")
else:
    print("Sorry, we don't have calorie burn data for that activity.")


#unit conversion machine

# Get user input
quantity = float(input("Enter the quantity: "))
unit_origin = input("Enter the unit of origin (miles, liters, Fahrenheit, etc.): ").lower()
unit_destination = input("Enter the unit of destination (kilometers, gallons, Celsius, etc.): ").lower()

# Define conversion factors for different units
conversion_factors = {
    "miles to kilometers": 1.60934,
    "kilometers to miles": 0.621371,
    "liters to gallons": 0.264172,
    "gallons to liters": 3.78541,
    "fahrenheit to celsius": lambda f: (f - 32) * 5/9,
    "celsius to fahrenheit": lambda c: (c * 9/5) + 32,
    # Add more conversions as needed
}

# Check if the conversion is available
conversion_key = f"{unit_origin} to {unit_destination}"
if conversion_key in conversion_factors:
    # Perform the conversion using the appropriate formula or factor
    if unit_origin == "fahrenheit":
        quantity = conversion_factors[conversion_key](quantity)
    else:
        quantity *= conversion_factors[conversion_key]

    # Display the result
    print(f"{quantity} {unit_origin} is approximately equal to {quantity:.2f} {unit_destination}.")
else:
    print("Sorry, that conversion is not supported.")

