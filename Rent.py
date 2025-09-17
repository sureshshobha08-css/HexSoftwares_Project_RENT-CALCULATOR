# Define variables
monthly_rent = float(input("Enter the base monthly rent: Rs "))
utilities = float(input("Enter the monthly utility cost: Rs"))
months = int(input("Enter the number of months: "))
roommates = int(input("Enter the number of roommates: "))

# Calculate total cost
total_cost = (monthly_rent + utilities) * months

# Cost per roommate
cost_per_person = total_cost / roommates

# Display results
print(f"\nTotal rent including utilities for {months} months: Rs{total_cost:.2f}")
print(f"Each roommate should pay:Rs{cost_per_person:.2f}")
